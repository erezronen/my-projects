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

def lesboprn(num,base1): #lossless encryption system based on psudo random number
    num=base(num,2,base1)
    r=randint(0,len(num)-1)
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
        r=randint(0,len(level)-1)
        out.append(level[r])
        key+=r*math.factorial(len(level))
        num1=level
    print(["".join(base(out,base1,10)),key])
    return ["".join(base(out,base1,2)),"".join(base(str(key),10,2))]
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
def activate_lesboprn(text,key_len):
    num = ''.join(format(ord(i), '08b') for i in text)
    num="".join(base(text,10,2))
    base1=round(2**(len(num)/key_len))
    out=lesboprn(num,base1)
    b="".join(base(str(base1),10,2))
    return [out[0],out[1]+"0"*(10-len(b))+b]
def binary_to_string(bits):
    return ''.join([chr(int(i, 2)) for i in bits])
def decrypt(num_key):
    num=str(num_key[0])
    key=str(num_key[1])
    base1=int("".join(base(key[-10:],2,10)))
    num=base(num,2,int(base1))
    key=int("".join(base(key[:-10],2,10)))
    key_list=[]
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
t=(activate_lesboprn(str(text),120))
print(int(decrypt(t))-int(text))
