'''let's read from a file in python'''
'''1. read from the file 
   2.store what you read into a variable and print it
analyze the string and variablize all useful information'''

from Parser import *
from CNF import *
from Parser import *
from random import *

def run(*args):        
    value = args[0]
    p = Parser("info.txt")
    conjuncts = []

    for line in p.lines: 
        cnf = CNF(line)   
        conjuncts.append(cnf)

def crossover(genes, pivot):
    value1 = str(genes[0])
    value2 = str(genes[1])
    
    head1,tail1 = value1[:pivot], value1[pivot:]        
    head2,tail2 = value2[:pivot], value2[pivot:]         
    str1 = "{}{}".format(head1, tail2)
    str2 = "{}{}".format(head2, tail1)
    return (str1, str2)

def mutate(gene, rate):
    value = str(gene)
    newvalue = ""
    for v in value:          
        actualvalue = v      
        if random() <= rate:
            actualvalue = '1' if v is '0' else '0'
        newvalue += str(actualvalue)
    return newvalue

def random_gene(strlen):
    value = ""
    for _ in range(strlen):
        value += str(randint(0, 1))
    return value

def genetic_algorithm(conjunct):
    
    '''we run the algorithm on a conjunct
    begin
        set time t:=0
        initialize the population P(t)
        while the termination condition is not met do
            begin
                evaluate fitness of each member of the population P(t)
                select members from population P(t) based on fitness
                produce the offspring of these pairs using genetic operators
                replace, based on fitness, candidates of P(t), with these offspring
                set time t:= t+1
    '''
    '''chromosome is the population'''
    '''the members are genes'''
    
    cnf = CNF(conjunct)    
    t = 0    
    populationlength = 25
    genelength = len(cnf.variables)
    population = []
    for _ in range(populationlength):
        population.append(random_gene(genelength))
    finished = False
    while not finished:
        for member in population:
            cnf.map_variables(member)
            cnf._fitness
            
    
def tests():
    g1 = '111000'
    g2 = '010111'
    print crossover([g1, g2], 3)
    print mutate(g1, 1)
    print mutate(g1, 0)
    
if __name__ == "__main__":            
    expressions = Parser('info.txt').lines
    for expression in expressions:
        genetic_algorithm(expression) 