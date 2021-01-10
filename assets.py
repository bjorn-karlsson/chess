def invertList(l):
    for index, value in enumerate(l):
        l[index] = value * -1
    return l

def Listdifference (list1, list2):
   list_dif = [i for i in list1 + list2 if i not in list1 or i not in list2]
   return list_dif



def isOdd(value):
    if(value % 2 == 0):
        return False
    else: 
        return True

def isEven(value):
    if(value % 2 == 0):
        return True
    else: 
        return False
