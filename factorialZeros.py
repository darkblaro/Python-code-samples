'''
Created on Sep 21, 2018

@author: Roman Blagovestny

The factorial of a non-negative integer n, denoted by n! is the product of all positive integers
less than or equal to n.

Example:
input: 5
output: 1 (5!-120 has one trailing zero)

input: 10
output: 2 (10!=3628800 has two trailing zeros)
'''
import math as m
def countZeros(n):
    count=0
    fact=str(m.factorial(n))
    for i in reversed(fact):
        if i=="0":
            count+=1
        else:
            break
    return count
if __name__ == '__main__':
    a=int(input("Enter a number"))
    print(f'The number {m.factorial(a)} has {countZeros(a)} trailing zeros.')