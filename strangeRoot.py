import math
'''
getRoot gets a number; calculate a square root of the number;
separates 3 digits after
decimal point and converts them to list of numbers
'''
def getRoot(nb):
    lsr=[]
    nb=math.floor(((math.sqrt(nb))%1)*1000) #To get 3 digits after decimal point
    ar=str(nb)
    for i in ar:
        lsr.append(int(i))
    return lsr

'''
getPower gets a number; calculate a power of the number;
and converts the result to list of numbers
'''
def getPower(num):
    lsp=[]
    num=int(math.pow(num,2))
    ar=str(num)
    for i in ar:
        lsp.append(int(i))
    return lsp

'''
isStrange gets a number; calls to two functions above and gets from them two lists
of numbers; after that compares two lists
'''
def isStrange(nb):
    ls1=getRoot(nb)
    ls2=getPower(nb)
    for i1 in ls1:
        for i2 in ls2:
            if i1==i2:
                return True
    return False

if __name__ == '__main__':
    number=int(input("Enter a number"))
    if isStrange(number):
        print(f'{number} has strange root')
    else:
        print(f'{number} doesn\'t have strange root')