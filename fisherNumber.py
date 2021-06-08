from functools import reduce

def FindFactors(n):
    factors=[]
    for i in range(1, int(n+1)):
        if n%i==0:
            factors.append(i)
    return factors

def isFisher(n):
    div=FindFactors(n)
    f=reduce(lambda x,y:x*y,div)
    if n**3==f:
        print(f'Number {n} is Fisher number')
    else:
        print(f'Number {n} is not Fisher number')

if __name__=='__main__':
    num=input("Enter a number: ")
    isFisher(int(num))