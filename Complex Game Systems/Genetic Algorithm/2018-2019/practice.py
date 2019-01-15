

def max_of_three(var1, var2, var3):
    '''Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!'''
    items = [var1, var2, var3]
    items.sort()
    return items[2]

print max_of_three(1,2,3)
print max_of_three(1,2,30)
print max_of_three(1,20,3)


'''Take two lists, say for example these two:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
'''

def add_to_list(item, list1):
    if item not in list1:
        list1.append(item)

def list_overlap_2(list1, list2):
    list3 = []
    for item1,item2 in zip(list1,list2):        
        add_to_list(item1, list3)
        add_to_list(item2, list3)
    return list3

def list_overlap_1(list1, list2):
    list3 = []
    for item in list1:
        if item in list3:
            continue
        list3.append(item)
    
    for item in list2:
        if item in list2:
            continue
        list3.append(item)    
    return list3

print list_overlap_2([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])