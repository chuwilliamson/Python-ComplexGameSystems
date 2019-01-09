'''let's read from a file in python'''
'''1. read from the file 
   2.store what you read into a variable and print it
analyze the string and variablize all useful information'''

import os
class Expression(object):
    def __init__(self, expression):
        self._expression = expression
        self._clauses = expression.split('*')
        self._symbols = [' ', '\n', '*', '+', '(' , ')' , '!']
        self._variables = []
        self._values = []
        for char in self._expression:
            if char not in self._symbols and char not in self._variables:
                self._variables.append(char)
                self.variables.sort()
    
    def map_variables(self, values):        
        if len(values) != len(self.variables):
            print "Must match variable length of " + str(len(self.variables)) + "attempted to map with length " + str(len(values))
            return None
        self._values = zip(values, self.variables)
        

        
    @property
    def variables(self):
        return self._variables

    @property
    def values(self):
        return self._values

    @property
    def info(self):
        print expression.variables
        print expression.values

        
                
class Parser(object):
    def __init__(self, filename):
        self._filename = filename        
        self._file = file(filename, 'r')        
        self._lines = self._file.readlines()
    
    @property
    def lines(self):
        return self._lines

p = Parser("info.txt")
expressions = []
for line in p.lines:    
    expressions.append(Expression(line))

for expression in expressions:
    expression.map_variables("101011")
    expression.info
    






