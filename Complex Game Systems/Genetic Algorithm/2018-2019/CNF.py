
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
        self._fitness = 0

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
        result = self._expression      
        self._values = zip(self._variables, values)        
        for item in self._values:
            result = result.replace(item[0], item[1])        
        for item in self._symbolmap:
            result = result.replace(item[0], item[1])       

        return result.split('and')
        

    @property
    def variables(self):
        return self._variables

    @property
    def clauses(self):
        return self._clauses

    @property
    def info(self):
        return "variables:: {}\nexpression:: {}\nresult:: {}".format(self._variables, self._expression, self._result)
                
