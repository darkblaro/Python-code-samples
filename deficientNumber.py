def FindFactors(n):
    factors=[]
    for i in range(1, int(n/2+1)):
        if n%i==0:
            factors.append(i)
    print("Factors of the number: ", factors)
    return factors

def SumOfFactors(f):
    fact=FindFactors(f)
    sum=0
    for i in fact:
        sum+=i
    print("Sum of factors: ", sum)
    return sum

def isDeficient(n):
    if SumOfFactors(n)<n:
        return True
    return False

#Prints "True" if number is deficient and prints "False" if not
print(isDeficient(10))