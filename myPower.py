def myPow(a,b):
    while b-1>0:
        a=a<<1
        b=b-1
    return a

print(myPow(2,8))