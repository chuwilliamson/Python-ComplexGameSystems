#File: CNF.py
class CNF:
    def __init__(self, exp):
        #Name: expression
        #Description: The literal expression this CNF is associated with. Ex: "(a * b) + (c * d)"
        self.expression = exp
        #Name: clauses
        #Description: list of the clauses Ex: [(a*b), (c*d)]
        self.clauses = []
        #Name: valid
        #Description: valid variables this CNF can use
        self.valid = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        #Name: varcount
        #Description: the number of total unique variables
        self.varcount = 0
        #Name: variables
        #Description: unique variables for this specific CNF
        self.variables = ""
        self.numClauses = len(self.clauses)
        self.setClauses()        
        #set the variables and number of variables in the cnf
        self.setVariables()
    #Function: setClauses
    #Parameters: self
    #Description: checks for valid cnf clause by incrementing  the current charactesr until it finds a "+". Once #it matches to a "+" matches the next char for ")" . After passing this check it appends the disjunct to the #clause list. It does not care to append the "+" b/c these are irrelevant due to the nature of cnf.  Updates #the number of clauses. Then converts them to the bitwise string
    #set the clauses for this gene
    #the clauses will come from the cnf and then
    #converted into a format that is compatible with bit operations
    #ex: chromosome.clause = a & b
    #Clauses: ['~a&b', 'c&d', 'e&~f', 'g&h']
    #Return: n/a    
    
    def setClauses(self):        
        tmp = ""        
        clauses = []
        for c in self.expression:   
            if(c != '+'):
                tmp += c
                if(c == ')'):                    
                    clauses.append(tmp)            
                    tmp = "" 
                
        
        self.clauses = self.convert(clauses)
        self.numClauses = len(self.clauses)
    #Function: convert
    #Parameters: c
    #Description: c is a clause of the form (a*b). Strips spaces and the "(" ")".It replaces the following: ! to ~ #+ to & and * to |.
    #Return: the string with the values replaced 
    #convert a cnf string to it's literal form
    #ex: "(!a + b) * (c + d) = (~a & b) | (c & d)
    def convert(self, c):        
        for i in range(len(c)):        
            c[i] = c[i].replace(" ", "")
            c[i] = c[i].replace("(", "")
            c[i] = c[i].replace(")", "")
            c[i] = c[i].replace("!", "~")
            c[i] = c[i].replace("+", "&")
            c[i] = c[i].replace("*", "|")        
        
        return c
        
    #Function: setVariables
    #Parameters: self
    #Description: set the variables and number of variables in the cnf
    #Return: n/a 
    def setVariables(self):     
        for i in self.expression:
            if(i in self.valid and i not in self.variables):
                self.variables += i
                
        self.varcount = len(self.variables)
     
    #Function: display
    #Parameters: n/a
    #Description: prints relevant information for this cnf
    #Return: n/a
    def display(self):
        print("===== CNF =====")        
        print("CNF:", self.expression)
        print("Clauses:", self.clauses)
        print("Variables:", self.variables)
        print("=========================\n")