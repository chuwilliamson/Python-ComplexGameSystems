'''main.py'''
from random import randrange


class Chromosome(object):
    '''Chromosome'''

    def __init__(self, expression):
        '''init'''
        self.expression = expression
        self.grammar = ['+', '*', '(', ')', '!']
        self.variables = self.get_variables()
        self.clauses = self._get_clauses()
        self.num_clauses = len(self.clauses)
        self.num_variables = len(self.variables)
        self.pairs = self._get_pairs()

    def _get_clauses(self):
        '''get clauses'''
        return self.expression.split('*')

    def get_variables(self):
        '''get variables'''
        variables = []
        expression = self.expression
        for item in self.grammar:
            expression = expression.replace(item, '')
        expression = expression.split()
        expression.sort()
        for i in expression:
            if i not in variables:
                variables.append(i)
        return variables

    def _get_pairs(self):
        '''get pairs'''
        pairs = []
        for i in self.variables:
            if i not in pairs:
                pairs.append((i, ''))
        return pairs

    def set_variable_pairs(self, args):
        '''set pair values'''
        for i in range(0, len(args)):
            pair = (self.pairs[i][0], args[i])
            self.pairs[i] = pair


def readfilewritefile():
    '''read write from file'''
    outfile = open('test.txt', 'w')
    for i in range(0, 9000):
        if i % 32 == 0:
            outfile.write('\n')
        outfile.write(str(randrange(0, 2)))
    outfile.close()

    infile = open('main.py', 'r')
    print infile.readline()


def makegene(num):
    '''make a gene'''
    gene = []
    for _ in range(0, num):
        gene.append(randrange(0, 2))
    return gene


def insertgene(chromosome):
    '''insert a gene into a chromosome'''
    gene = makegene(chromosome.num_variables)
    print 'insert: ', gene
    chromosome.set_variable_pairs(gene)
    print 'pairs:', chromosome.pairs


def main():
    '''main function to do work'''
    chromosome = Chromosome("(a + b) * (d + c) * (d + c + e + !d)")
    print 'expression:', chromosome.expression
    print 'variables:', chromosome.variables
    print 'clauses:', chromosome.clauses
    print 'num clauses:', chromosome.num_clauses
    print 'pairs:', chromosome.pairs

    for _ in range(0, 5):
        insertgene(chromosome)


main()
