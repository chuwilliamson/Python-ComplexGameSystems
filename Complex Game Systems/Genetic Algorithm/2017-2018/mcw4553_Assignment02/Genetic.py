#File: Genetic.py
import Chromosome
import operator
import CNF
from Chromosome import *
from CNF import *
'''
    =======================================================================
    Encoding table      Class       Hair Color      Agenda          Fears
        ===================================================================
            00          Rogue       Black           Gold            Prison                
            01          Warrior     Brown           Fame            Spiders
            10          Mage        Grey            Knowledge       Idiocy
            11          Wildcard    Blonde          Evil            Noobs
        ===================================================================
    '''

'''
    Get Input: 
        Ex: Enter an expression to solve.
        Ex: (!a ^ b) v (c ^ d) v (e ^ !f) v (g ^ h)
            Solution: 01 11 10 00 (Warrior, Blonde, Knowledge, Noobs)
                a = 0       c = 1       e = 1       g = 1          
                b = 1       d = 1       f = 0       h = 1
    Get the clauses. 
        Ex: cnf = (!a + b) (c + d) (e + !f) (g + h)
    Get the variable count. 
        Ex: 8
    Initialize chromosomes based on the variable count. 
        Chromosome length based on number of variables. 
        Number of chromosomes is arbitrary. 
        Ex: C1.gene = 10 11 11 00; 
            C2.gene = 11 00 00 00;
            C3.gene = 11 11 00 01;
            C4.gene = 00 01 10 10;
    Evaluate fitness by summing the number of true clauses in each chromosome
        Ex: C1.fitness = f t f f >>1
            C2.fitness = f f f f >>0
            C3.fitness = f t f f >>1 
            C4.fitness = f f t f >>1
    Select parents based on fitness.
        Ex: select(C1) and select(C3)
    Perform Crossover on C1 and C3.
        Ex: Breed(C1, C3)
    ===Genetic Algorithm===
        time t = 0
        initialize population P(t)  
        repeat
            evaluate each member of P(t)
            select member of P(t)  based on fitness
            produce offspring using genetic operators
            replace, based on fitness, members of P(t) with these
            t+=1
        until solved
    
    === ===
    '''
#Function: run
#Parameters: cnf, debug 
#Description: cnf is the string representation of the cnf to be solved, debug is a boolean that will enable all print statements if true. Performs the algorithm as described in the system architecture.
#Return: the number of generations it took to solve the expression
def run(cnf, debug):
    t = 0
    f = 0
    
    population = generate_population("", t, cnf, debug)
    population = sorted(population,key = lambda p: p.fitness, reverse = True)
    
    print("Solving for", cnf.expression)
    totalFitness = 0
    
    while True:        
        fitnesses = calc_fitnesses(population)         
        selection = get_selection(fitnesses, cnf)   
        offspring = create_offspring(selection, t, debug)        
        population = replace_population(offspring)
        fitnessGoal = population[0].fitness
        if(debug):
            print("Fitness Goal:", cnf.numClauses, "@Generation", t)
            
        if(fitnessGoal == cnf.numClauses):
            winner = population[0]
            print("====Solved=====\n",cnf.expression,"\n@ GENERATION", t,"with",winner.genes,"\n")            
            break;
        
        t += 1
        if(t % 100 == 0):
            print("@",t,"generations no solution")
            
        if(t >= 1000):
            print("no solution found :( try again b/c rng is rng...")
            break
        
        #restart loop
    return t

#Function: generate_population
#Parameters:  id gen cnf debug
#Description: id is the unique identifier for this chromosome, gen is the generation this chromosome was created, cnf is the expression to be solved, debug is the boolean for showing print statements. Generates a population based on the number of variables /2.
#Return: list of chromosomes
#generate a population of Chromosomes
#returns a list of Chromosomes
def generate_population(id, gen, cnf, debug):
    pop = []
    genCount = int(len(cnf.variables) / 2 )
    
    if (genCount <= 2):
        if(debug):
            print("Initial population too low... doubling it")
        genCount = 4
        
    for i in range(0, genCount):
        c = Chromosome(str(id) + str(i), gen, cnf, False, "")
        pop.append(c)    
        
    return pop

#Function: calc_fitnesses
#Parameters:  pop is the list of chromosomes to be evaluated for fitness
#Description: evaluates population based on number of correct disjuncts with respect to the expression.
#Return: sorted chromosome population by fitness values
#calculates the strongest of the population based on fitness
#and returns the most fit
def calc_fitnesses(pop):           
    tf = 0
    count = 0
    for i in pop:
        i.id = str(count)
        i.evalFitness()
        tf += i.fitness
        count += 1
        
    prev = 0
    pop = sorted(pop, key = lambda p: p.fitness, reverse = True)
    for i in pop:
        i.set_fitness_ratio(tf)
        i.set_fitness_range(prev)
        prev = i.maxRange
    return pop

#Function: get_selection
#Parameters:  fit cnf
#Description: fit is the list of chromosomes after their fitness values have been calculated, cnf is the current expression.  Randomly selects members of the population based on their contribution to the overall fitness. This is to ensure more randomness and giving chromosomes with a low initial fitness ratio to be selected
#Return: list of selected chromosomes. the size of this list is the same size of the initial population
#returns a list of the parents
def get_selection(fit, cnf):
    sel = [] 
    
    new_gen_size = cnf.numClauses
    #clamp size to 4
    if(new_gen_size <= 2):
        new_gen_size = 4
    
    for loop in range(0, new_gen_size):
        rNum = random.randint(0, 100)
        rNum /= 100        
        #print("Random Selection",loop,"is", rNum)        
        for i in fit:
            if (rNum >= i.minRange and rNum <= i.maxRange):
                sel.append(i)                
                #print("selecting", i.id)
                break
            
    return sel

#Function: create_offspring
#Parameters:  selection, t, debug
#Description: selection is the randomly selected list, t is the generation count, debug is for printing. 
#Return: list of offspring from resulting crossover and mutation
#takes the random selected population and generates offspring from them
def create_offspring(selection, t, debug):
    children = []
    subchildren = []
    upperBound = len(selection)
    if(debug):
        print("===Selection===")
    for i in selection:
        if(debug):
            i.displayGenes()
            
    if(len(selection) % 2 == 1):
        upperBound = len(selection) - 1
    else:
        upperBound = len(selection)
        
    for i in range(0, upperBound, 2):        
        first = i
        second = i + 1
        p1 = selection[first]                
        p2 = selection[second]
        
        parents = [(p1), (p2)]
        if(debug):
            print("====Parents====")
        for i in parents:
            if(debug):
                i.displayGenes()
            
        geneLength = len(p1.genes)
    
        crossoverPoint = random.randint(0, geneLength)
        if(debug):
            print("crossover @", crossoverPoint)
        
        subchildren = crossover(t, p1, p2, crossoverPoint, debug)
        
        for i in subchildren:
            if(debug):
                i.displayGenes()
            children.append(i)
        subchildren = []
    if(debug):
        print("====SELECTION====")
        for i in selection:
            i.displayGenes()
            
        print("====CHILDREN====")
        for i in children:
            i.displayGenes()
            
    return children

#Function: crossover
#Parameters:  t, dad, mom, randNum, debug
#Description: t is the generation, dad is the chromosome that will crossover with mom, randNum is for the random crossover point, debug is for printing. Generate a random number then use that number as a crossover point to perform crossover. for example: random = 2 dad = 0011 mom = 1100 the resulting children will be 0000 and 1111.
#Return: list of two chromosomes from resulting crossover operations
#does a crossover on two Chromosomes
#return a list of two Chromosomes containing the result of crossover
def crossover(t, dad, mom, randNum, debug):
    dadPt1, dadPt2, momPt1, momPt2 = ("",) *4

    dadGenes = dad.genes
    momGenes = mom.genes

    for i in range(0, randNum):
        dadPt1 += dadGenes[i]
        momPt1 += momGenes[i]
        
    for i in range(randNum, len(dadGenes)):
        dadPt2 += dadGenes[i]
        momPt2 += momGenes[i]

    child1 = Chromosome("child1", t, dad.cnf, False, dadPt1 + momPt2)
    child2 = Chromosome("child2", t, dad.cnf, False, momPt1 + dadPt2)
    if(child1.genes == child2.genes and (t % 3) == 0):
        child1.genes = mutate(child1, debug)
        
    children = [(child1), (child2)]
    
    for i in children:
        i.evalFitness()
    
    return children

#Function: replace_population
#Parameters:  offspring
#Description: sorts the offspring by fitness value. This can be taken out but was left in for program integrity
#Return: sorted offspring by fitness values
def replace_population(offspring):
    #return sorted list based on fitness
    #the first element of this list will be checked by fitness
    #if it is the num clauses we have an answer
    return sorted(offspring, key = lambda p: p.fitness, reverse = True)

#Function: mutate
#Parameters: child debug
#Description: selects a random point in a chromosomes gene and flips it. 
#Return: gene with bit flipped
def mutate(child, debug):
    genes = list(child.genes)
    mutatePoint = random.randint(0, len(child.genes) - 1)    
    if(debug):
        print("mutate point = ", mutatePoint, " length of genes =", len(child.genes))
    if(genes[mutatePoint] == "1"):
        genes[mutatePoint] = "0"
    else:
        genes[mutatePoint] = "1"
        
    return "".join(genes)

#Function: test_crossover
#Parameters:  n/a
#Description: solo function to test the crossover functionality
#Return: n/a
def test_crossover():
    cnf = CNF("(a * b) + (c * d)")
    dad = Chromosome(1, 0, cnf, True, "")
    mom = Chromosome(2, 0, cnf, True, "")
    parents = [(dad), (mom)]
    children = crossover(0,dad, mom, 2, debug)
    for i in parents:
        print(i.genes)

    for i in children:
        print(i.genes)
        
#Function: test_offspring
#Parameters:  n/a
#Description: solo function to test the offspring functionality
#Return: n/a
def test_offspring():
    cnf1 = CNF("(a * b) + (c * d) + (e * f)")
    dad = Chromosome(1, 0, "(a * b) + (c * d) + (e * f)", True, "")
    mom = Chromosome(2, 0, "(a * b) + (c * d) + (e * f)", True, "")
    parents = [(dad), (mom)]
    offspring = create_offspring(parents)

#Function: test_cnf
#Parameters: n/a  
#Description: solo function to test the cnf functionality
#Return: n/a
def test_cnf():
    cnf = CNF("(a * b) + (c * d) + (e * f)")
    cnf.display()

#Function: test_chromosome
#Parameters: n/a  
#Description: solo function to test the chromosome functionality
#Return: n/a
def test_chromosome():
    cnf = CNF("(a * b) + (c * d) + (e * f)")
    chro = Chromosome(1, 0, cnf, 0, "")
    chro.display()

#Function: test_replace
#Parameters: n/a  
#Description: solo function to test the replace functionality
#Return: n/a
def test_replace():
    cnf = CNF("(a * b) + (c * d) + (e * f)")
    #cnf = CNF("(!a * b) + (c * d) + (e * !f) + (g * h) + (i * j) + (k * l) + (m * n) + (o * p) + (q * r) + (s * t) + (u * v) + (w * x) + (y * z)")
    pop = generate_population("initial ", 0, cnf)
    #for i in pop:
        #i.display()
    #manual parent set
    pop[0].setElite()
    pop[1].setElite()
    #manual add
    child1 = Chromosome("child " + str(1), 0,cnf, False, '101111')
    child2 = Chromosome("child " + str(2), 0,cnf, False, '000001')
    children = [(child1), (child2)]
    #for i in children:
        #i.display()
    replace_population(pop, children)
    
    
#test_crossover()
#test_offspring()
#end test crossover
#test_cnf()
#test_chromosome()
#test_replace()






        
    
    