'''let's read from a file in python'''
'''1. read from the file 
   2.store what you read into a variable and print it
analyze the string and variablize all useful information'''



class Hero:
    def __init__(self):
        self.__dexterity = 0
        self.__strength = 0
        self.__name = "default"
    def info(self):
        print self.__dexterity
        print self.__strength
        print self.__name

def medoit():
    print 'donedidit'

medoit()
bob = Hero()
bob.info()
