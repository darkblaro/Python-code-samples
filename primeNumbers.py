def isPrime(pn):
    flag=0
    for i in range(2, int(pn/2+1)):
        if pn%i==0:
            flag=1
            break
    if flag==0:
        return True
    else:
        return False

if __name__=='__main__':
    if isPrime(6):
        print("Prime")
    else:
        print("Not prime")