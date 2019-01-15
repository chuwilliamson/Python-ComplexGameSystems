
class CNF(object):
    def __init__(self, expression):         
        self._expression = expression.replace('\n', '')
        self._clauses = self._expression.split('*')
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
                self._variables.sort()
 

    def map_variables(self, values):        
        if len(values) != len(self._variables):
            self._result = None            
            return None
        self._values = zip(self._variables, values)
        
        for item in self._values:
            self._evaluation = self._evaluation.replace(item[0], item[1])
        for item in self._symbolmap:
            self._evaluation = self._evaluation.replace(item[0], item[1])
        self._result = eval(self._evaluation)

    @property
    def variables(self):
        return self._variables
    def clauses(self):
        return self._clauses

    @property
    def info(self):
        return "variables:: {}\nexpression:: {}\nevaluation:: {}\nresult:: {}".format(self._variables, self._expression,self._evaluation, self._result)
                
