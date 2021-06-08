'''A number is called a Disarium number if the sum of the powers of its digits equals the number itself. The digits are powered to their positions in the number.

For example:
Input: 135
Output: true
135 is a Disarium number because it equals to 1^1 + 3^2 + 5^3 (each digit powered to the position in the number).'''

def disarium(num):
    st=str(num)
    i=0
    n2=0
    while i<len(st):
        n2+=(int(st[i]))**(i+1)
        i+=1
    if n2==num:
        return True
    else:
        return False

b=int(input("Enter start number of the range"))
e=int(input("Enter end number of the range"))
for i in range(b,e):
    if disarium(i):
        print(f'The number {i} is disarium number')
    else:
       print(f'The number {i} is not disarium number')