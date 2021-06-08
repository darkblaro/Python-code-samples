import math
def isPrime(n):
    flag=0
    for i in range(2,int(n/2+1)):
        if n%i==0:
            flag=1
    if flag==1:
        return False
    else:
        return True

def mersennePrime(n):
    e=int(math.log(n,2)+1)
    if isPrime(n) and 2**e-1==n:
        return True
    else:
        return False

if __name__ == '__main__':
    start=int(input("Enter start of a range"))
    end=int(input("Enter end of a range"))
    for i in range(start,end):
        if mersennePrime(i):
            print(f'{i} is Mersenne Prime')