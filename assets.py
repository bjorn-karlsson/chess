def invertList(l):
    for index, value in enumerate(l):
        l[index] = value * -1
    return l

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