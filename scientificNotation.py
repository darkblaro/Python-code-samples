'''
Created on Oct 12, 2018
Scientific Notation
input: 9000
output: 9*10^3
@author: Roman Blagovestny
'''
def scinotdown(n):
    cz=0
    n=float(n)
    if n<1 and n>-1:
        while n<1 and n>-1:
            cz+=1
            n*=10
        return str(n)+"*10^-"+str(cz)
    if n>1 or n<-1:
        while n>=1 or n<-1:
            cz+=1
            n/=10
        return str(n*10)+"*10^"+str(cz-1)

if __name__ == '__main__':
    try:
        inp=float(input("Enter a number: "))
        print(scinotdown(inp))
    except ValueError:
        print("Wrong input.")