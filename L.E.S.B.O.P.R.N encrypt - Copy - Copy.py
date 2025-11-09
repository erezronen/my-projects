import math
from random import randint
import heapq
import os
import binascii
def convert_to_decimal(number, base):
    decimal = 0
    base1 = 1
    out=0
    for digit in number[::-1]:
        if digit=="0":
            out+=1
        decimal += int(digit) * base1
        base1 = base1 * base
    return str(decimal)

def base(num, base_base, base):
    num = int(convert_to_decimal(num, base_base))
    base_num = []
    while num > 0:
        dig = str(num % base)
        base_num.append(dig)
        num //= base
    base_num = base_num[::-1]
    return (base_num)

def lesboprn(num,base1,key_list): #lossless encryption system based on psudo random number
    r=key_list[0]
    out = [num[r]]
    num1 = num
    key=r*math.factorial(len(num))
    for i in range(len(num)-1):
        level = []
        for a in range(len(num1) - 1):
            temp = int(num1[a + +1]) - int(num1[a])
            if temp < 0:
                temp += base1
            level.append(str(temp))
        r=key_list[i++1]
        out.append(level[r-1])
        key+=r*math.factorial(len(level))
        num1=level
    print(out,"yo")
    return ["".join(base(out,base1,10)),key]
def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(str(bits), 2)
    return int2bytes(n).decode(encoding, errors)
def text_to_bits(text, encoding='ascii', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def factorial_cap(num):
    n = 1
    i = 1
    while n < num:
        i += 1
        n *= i
    return i-2
def activate_lesboprn(text,key):
    base1=round(10**(len(text)/(factorial_cap(10**len(str(key))))))
    num=base(text,10,base1)
    print(len(num))
    key_list=[]
    for i in range(len(num)++1):
        key1=key%math.factorial(len(num)-i)
        key_list.append(int((key-key1)/math.factorial(len(num)-i)))
        key=key1
    key_list.append(key)
    out=lesboprn(num,base1,key_list)
    print(len(key_list))
    return [out[0],base1]
def decrypt(num_key,base1):
    num=str(num_key[0])
    key=str(num_key[1])
    num=base(num,10,int(base1))
    key_list=[]
    key=int(key)
    for i in range(len(num)++1):
        key1=key%math.factorial(len(num)-i)
        key_list.append(int((key-key1)/math.factorial(len(num)-i)))
        key=key1
    key_list=key_list[::-1]
    key_list.append(key)
    level=[num[-1]]
    for i in range(1,len(num)++1):
        num_p1=[str(num[-i])]
        for a in range(i-key_list[i]-1):
            add= int(level[a++key_list[i]])++int(num_p1[-1])
            if add>=base1:
                add-=base1
            num_p1.append(str(add))
        num_p1=num_p1[::-1]
        level=level[::-1]
        for a in range(key_list[i]):
            add=int(num_p1[-1])-int(level[a-key_list[i]])
            if add<0:
                add+=base1
            num_p1.append(str(add))
        level=num_p1[::-1]
    out=level
    out="".join((base(out,base1,10)))
    return(out)
text=1023683654762145528664823164825452567425541254523452345253657612102368365476214552866482316482545256742554125452345234525365761210236836547621455286648231648254525674255412545234523452536576121023683654762145528664823164825452567425541254523452345253657612
t=(activate_lesboprn(str(text),132765872365873653245329752013276587236587365324532975201327658723658736532453297520132765872365873653245329752013276587236587365324532975201))
print(t)
print([[t[0],132765872365873653245329752013276587236587365324532975201327658723658736532453297520132765872365873653245329752013276587236587365324532975201],t[1]])
print(int(decrypt([t[0],132765872365873653245329752013276587236587365324532975201327658723658736532453297520132765872365873653245329752013276587236587365324532975201],t[1])))


