
from random import randint

def crossover(genes, pivot):
    value1 = str(genes[0])
    value2 = str(genes[1])
    
    head1,tail1 = value1[:pivot], value1[pivot:]        
    head2,tail2 = value2[:pivot], value2[pivot:]         
    str1 = "{}{}".format(head1, tail2)
    str2 = "{}{}".format(head2, tail1)
    return (str1, str2)

def mutate(gene, rate):
    value = str(gene)
    newvalue = ""
    for v in value:          
        actualvalue = v      
        if random() <= rate:
            actualvalue = '1' if v is '0' else '0'
        newvalue += str(actualvalue)
    return newvalue

def random_gene(strlen):
    value = ""
    for _ in range(strlen):
        value += str(randint(0, 1))
    return value
    
def roulette_wheel(items):
    '''fitness selection'''
    result = None
    partial_sum = 0    
    random_choice = randint(0, sum(items))

    for item in items:
        partial_sum += item
        if partial_sum <= random_choice:
            result = item
            break
    
    return result
