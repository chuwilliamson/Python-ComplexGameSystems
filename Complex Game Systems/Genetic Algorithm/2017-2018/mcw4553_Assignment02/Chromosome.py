import random
import operator
import math

class Chromosome:
    def __init__(self, id, generation, cnf, elite, genes):
        #Name: id
        #Description: identifier for the chromosome
        self.id = id 
        #Name: generation
        #Description: which iteration of the loop is this chromosome part of
        self.generation = generation
        #Name: cnf
        #Description: the expression this Chromosome will evaluate to
        self.cnf = cnf     
        #Name: genes
        #Description: the variable representation Ex: 10001
        self.genes = genes
        #Name: geneCount
        #Description: the length of the genes
        self.geneCount = len(self.cnf.variables)
        #Name: fitness
        #Description: number of correct disjuncts that this chromosome matches
        self.fitness = 0
        #Name: literals
        #Description: dictionary of variables to the genes.  #literals dictionary a:1 b:0 c:1
        self.literals = {}
        #Name: geneClauses
        #Description: clauses associated with this chromosome. Ex:(1*1)
        self.geneClauses = []
        #Name: Elite
        #Description: Is this Chromosome an elite. This was used in previous implementation whenever we cared about the state of this object
        self.Elite = elite   
        #Name: fitness_ratio
        #Description: value between 1-100 that gives a weight of correctness vs all other genes
        self.fitness_ratio = 0
        #Name: minRange
        #Description: the lower bound of the fitness ratio
        self.minRange = 0
        #Name:max Range
        #Description: the upper bound of the fitness ratio
        self.maxRange = 0 
        #begin the setup for this objects genes
        self.setGenes(genes) 
    
    #Function: display
    #Parameters: self
    #Description: display relevant information for this object
    #Return: n/a 
    def display(self):
        print("===== Chromosome", self.id, "=====")
        print("Generation:", self.generation)
        print("CNF:", self.cnf.expression)
        print("Clauses:", self.cnf.clauses)
        print("Variables:", self.cnf.variables)
        print("Genes:", self.genes)
        print("Gene Count:", self.geneCount)
        #print("Gene Literals:", self.literals)
        print("Gene Clauses:", self.geneClauses)
        print("Fitness:",self.fitness)
        print("Fitness Ratio:",self.fitness_ratio)
        #print("Elite: " , self.Elite)
        print("=========================\n")
        
    #Function: setGenes
    #Parameters: string genes
    #Description: takes in strings for manual assignment or performs random assignment based on the variable length.
    #Return: n/a    
    def setGenes(self, genes):
        if(genes != ""):
            if(len(genes) != len(self.cnf.variables)):
                print("Bit length to variables problem for", self.id)
                return 
            else:
                self.genes = genes
                self.mapGenes()
                self.evalFitness()
        else:            
            #random binary assignment
            
            for i in range(0, self.geneCount):
                tmp = str(random.randint(0,1))
                self.genes += tmp
                
            self.mapGenes()
      
    #Function: mapGenes
    #Parameters: self 
    #Description: Maps the genes to the variables. Appending to the literals dictionary. Sorts the resulting list by the variable. This is only for organized output information
    #Return: n/a      
    def mapGenes(self):
        #create a dictionary of the variables with the key of the gene
        for i,k in zip(self.cnf.variables, self.genes):
            self.literals.update([(i,k)])
            
        #map the variables of the clause to the gene
        for clause in self.cnf.clauses:
            self.geneClauses.append(self.mapVars(clause))
            
        #sort the literals dictionary by the variable
        self.literals = sorted(self.literals.items(), key=operator.itemgetter(0))
 
    #Function: mapVars
    #Parameters: Clause Ex: (a * b)
    #Description: Takes a clause and replaces the appropriate variable with it.
    #Return: list with variables replaced Ex: (1 * 0)       
    def mapVars(self, clause):        
        tmpClause = clause        
        for c in clause: #for each character in the clause         
            if(c in self.cnf.variables):#check if its in variables                
                tmpClause = tmpClause.replace(c, self.literals.get(c))                
                
        return tmpClause
    #Function: evalFitness
    #Parameters: self
    #Description: evaluates the clauses of this gene using bitwise operations
    #Return: n/a    
    #~ Not ^ XOR | Or & And
    #evaluate the fitness and clear elite flags
    def evalFitness(self):
        self.Elite = False
        self.fitness = 0
        for i in self.geneClauses:             
            if(eval(i)):
                self.fitness +=1
    #Function: set_fitness_ratio
    #Parameters: tf
    #Description: tf is the total fitness of the population this chromosome is associated with. divide the fitness value by the total fitness to get the weight of this chromosome
    #Return: n/a        
    def set_fitness_ratio(self, tf):
        self.fitness_ratio =  round(self.fitness / tf, 3)

        
    #Function: set_fitness_range
    #Parameters: chrom  
    #Description: chrom is a reference to the previous chromosome to calculate the minimum and maximum bounds for the current chromosome. It is initially set to 0 then set to the current member as it evaluates. This is to ensure the correct ranges are calculated
    #Return: n/a 
    def set_fitness_range(self, chrom):
        self.minRange = round(chrom, 2)
        self.maxRange = round(self.fitness_ratio + chrom, 3)
        if(self.maxRange >= .99):
            self.maxRange = math.ceil(self.maxRange)
    
    #Function: displayGenes
    #Parameters: self
    #Description: displays only gene information
    #Return: n/a
    def displayGenes(self):
        print("======ID:", self.id,"=====Genes:", self.genes,"Fitness:", self.fitness, "nFitness Range:",self.minRange,"->",self.maxRange)
     
'''
f'(x) = fitness ratio
f'(1) = 100
f'(0) = 50
f'(-1) = 0
f'(x) = 50(f(x) + 1)
fitness based on number of correct clauses
'''