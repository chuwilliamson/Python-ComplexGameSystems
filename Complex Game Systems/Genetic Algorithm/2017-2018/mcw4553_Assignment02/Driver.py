import os
import Chromosome
import Genetic
import CNF
from Genetic import *
from Chromosome import *
from CNF import *

#Function: main
#Parameters: n/a
#Description: takes in from file expressions in cnf. strips white space and newline characters. It then performs the genetic algorithm on all expressions.
#Return: n/a
def main():
    tmp = []
    file = 'Expressions.txt'
    presets = LoadPresets(file)
    for p in presets:
        p = p.replace(" ", "")
        p = p.replace("\n", "")
        tmp.append(p)
    presets = tmp
    all = True
    
    #testCnf = CNF(presets[4])
    #gens = Genetic.run(testCnf)
    if(all):
        for i in presets:
            #print(i)
            cnf = CNF(i)
            gens = Genetic.run(cnf, False)
    else:
        #print("testing bit operaations 1 & 0 =", 1 & 0)
        #print("testing bit operations 1 | 1 = ", 1 | 0)
        gens = Genetic.run(testCnf)
        while True:
            if(gens > 1):
                return
            
            
            else:
                gens = Genetic.run(testCnf)
   
#Function: LoadPresets
#Parameters: file
#Description: file is the name of the file to be loaded. If no file is found it will load the default cnf "(a * b) +  (c * d)
#Return: the string representation of the cnf
def LoadPresets(file):   
    inFile = open(file, 'r')
    conjunct = []
    if(inFile):
        for i in inFile:
            conjunct.append(i)
    else:
        preset = "(a * b) + (c * d)"
        v = ""
        print("Loading presets")
        for p in preset:       
            disjunct += p
            v += p
            if(p == ')' or p == '*'):
                conjunct.append(disjunct)
                disjunct = ''
    
    return conjunct

'''====================================='''
main()
#main(input("1 for preset, 2 for user specified: "))