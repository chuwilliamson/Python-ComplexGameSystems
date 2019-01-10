'''let's read from a file in python'''
'''1. read from the file 
   2.store what you read into a variable and print it
analyze the string and variablize all useful information'''

import os
class Expression(object):
    def __init__(self, expression):         
        self._expression = expression.replace('\n', '')
        self._clauses = expression.split('*')        
        self._symbols = ['*', '+', '(' , ')' , '!']      
        self._symbolmap = [('!', 'not '), ('+', 'or'),('*', 'and')]  
        self._literals = []
        self._variables = []
        self._values = []
        self._result = False
        self._evaluation = self._expression

        #get the literals
        for char in self._expression:
            if char not in self._symbols and char != ' ':
                self._literals.append(char)
        #get the variables aka: the unique literals
        for char in self._literals:
            if char not in self._variables:
                self._variables.append(char)
                self.variables.sort()
                        
    def map_variables(self, values):        
        if len(values) != len(self.variables):
            self._result = None            
            return None
        self._values = zip(self.variables, values)       
        for kvp in self._values:            
            self._evaluation = self._evaluation.replace(kvp[0], kvp[1])

        for kvp in self._symbolmap:
            self._evaluation = self._evaluation.replace(kvp[0], kvp[1])          
        
        self._result = eval(self._evaluation)

    @property
    def evaluation(self):
        return self._evaluation
    @property
    def expression(self):
        return self._expression
    @property
    def result(self):
        return self._result
    @property
    def variables(self):
        return self._variables
    @property
    def values(self):
        return self._values

    @property
    def info(self):
        print "variables:: " , expression.variables
        print "expression:: " , expression.expression
        print "evaluation:: " , expression.evaluation
        print "result:: " , expression.result

        
                
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
    






