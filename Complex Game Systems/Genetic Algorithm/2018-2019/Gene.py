from functions import *
from CNF import *

class Gene(object):
    def __init__(self, bits=None, cnf = None):
        '''this is the bitstring'''
        self._bits = str(bits)
        self._cnf = cnf
        
    
    @property
    def fitness(self, cnf):
        fitness = 0
        for clause in cnf.clauses:
            fitness += eval(clause)        
        return fitness

    def mutate(self, rate):
        return mutate(self._bits, rate)

    def crossover(self, other):
        return crossover(self._bits, other)
