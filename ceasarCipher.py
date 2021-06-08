'''
Created on Oct 14, 2018

@author: Roman Blagovestny
'''
#CeasarCipher - encrypts the string
def CeasarCipher(word):
    output=[]
    for i in word:
        if (ord(i)<65 or ord(i)>90) and (ord(i)<97 or ord(i)>122):
            output+=i
            continue
        if (ord(i)+1)>=97 and (ord(i)+1)<=122 or (ord(i)+1>=65 and ord(i)+1<=90):
            output+=chr(ord(i)+1)
        if (ord(i)+1)>122:
            output+=chr(ord(i)-122+97)
        if (ord(i)+1)>90 and ord(i)<97:
            output+=chr(ord(i)-90+65)
    return "".join(output)
    
#CeasarCipherDec - decrypts the string
def CeasarCipherDec(word):
    output=[]
    for i in word:
        n=ord(i)
        if (ord(i)<65 or ord(i)>90) and (ord(i)<97 or ord(i)>122):
            output+=i
            continue
        if (ord(i)-1)>=65 and (ord(i)-1)<=90 or (ord(i)-1>=97 and ord(i)-1<=122):
            output+=chr(ord(i)-1)
        if (ord(i)-1)<97 and (ord(i)-1)>90:
            output+=chr(ord(i)+90-65)
        if (ord(i)-1)<65:
            output+=chr(ord(i)+122-97)
    return "".join(output)

if __name__ == '__main__':
    txt=input("Enter your text: ")
    a=CeasarCipher(txt)
    print(a)
    print(CeasarCipherDec(a))