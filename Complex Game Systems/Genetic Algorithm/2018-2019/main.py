'''let's read from a file in python'''
'''1. read from the file 
   2.store what you read into a variable and print it
analyze the string and variablize all useful information'''

from random import *

from CNF import *
from functions import *
from Gene import *
from Parser import *


def run(*args):        
    value = args[0]
    p = Parser("info.txt")
    conjuncts = []

    for line in p.lines: 
        cnf = CNF(line)   
        conjuncts.append(cnf)


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
        population.append(Gene(random_gene(genelength)))
    #we are finished with algo whenever we get a member of the population to have a fitness of 100%
    while True:
        for gene in population:
            '''map the variables [1100, 0011]'''
            clauses = cnf.map_variables(gene._bits)            
            for clause in clauses:
                res = eval(clause)

            

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
