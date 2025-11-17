import heapq
import os
import binascii
import math
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

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
def text_from_bits(bits):
    n=base(bits,2,128)
    out=""
    for i in n:
        out+=chr(int(i))
    return out
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def rtir_complex(num,n):
    out = [num[-1]]
    num1 = num
    for i in range(len(num) - 1):
        level = []
        for a in range(len(num1) - 1):
            temp = int(num1[a++1]) ++ int(num1[a])
            if temp > 256:
                temp -= 256
            level.append(str(temp))
        out.append(level[n])
        num1=level
    return ((out))
def rtir(num,n):
    out = [num[0]]
    num1 = num
    for i in range(len(num) - 1):
        level = []
        for a in range(len(num1) - 1):
            temp = int(num1[a + +1]) - int(num1[a])
            if temp < 0:
                temp += 256
            level.append(str(temp))
        out.append(level[0])
        num1=level
    return ((out))
def rtir_efficient(num,division,n):
    out=[]
    while len(num)>=division:
        for i in rtir(num[:division],n):
            out.append(i)
        num=num[division:]
    return out
def rtir_efficient_complex1(num, division,n):
    out = []
    while len(num) >= division:
        for i in rtir_complex(num[:division],n):
            out.append(i)
        num = num[division:]
    return out
def rtir_efficient_complex(num,division,times):
    max=0
    iii=0
    iiii=0
    for i in range(times):
        num = rtir_efficient(num[::-1], division,-1)
        num = rtir_efficient_complex1(num, division,0)
        t=[round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4),round(-len(num)/4)]
        for ii in range(len(num)):
            t[int(num[ii])-1]+=1
        t=abs(t[0])+abs(t[1])+abs(t[2])+abs(t[3])
        if t>max:
            max=t
            iii=num
            iiii=i
    return [iii,iiii]
def un_rtir_efficient_complex(num,division,times):
    for i in range(times):
        num = rtir_efficient(num[::-1], division,0)
        num = rtir_efficient_complex1(num, division,-1)
    return num
def lesboprn(num,base1): #lossless encryption system based on psudo random number
    num=base(num,2,base1)
    r=round(len(num)/2)
    out = [num[r]]
    num1 = num
    for i in range(len(num)-1):
        level = []
        for a in range(len(num1) - 1):
            temp = int(num1[a + +1]) - int(num1[a])
            if temp < 0:
                temp += base1
            level.append(str(temp))
        r=round(len(level)/2)
        out.append(level[r])
        num1=level
    return "".join(base(out,base1,2))
def decrypt(num,base1):
    num=base(num,2,int(base1))
    key_list=[]
    for i in range(len(num)++1):
        key_list.append(round(i/2))
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
    out="".join((base(out,base1,2)))
    return(out)
def test_tree_branch(tree, path):
    a=len(path)
    try:
        for i in path:
            tree=tree[int(i)]
            a-=1
        return([tree,0])
    except:
        return([tree,a])
def test_tree(tree):
    i=0
    out=[]
    for i in range(256):
        out.append("0")
    while True:
        i+=1
        j=base(str(i),10,2)[1:]
        t=test_tree_branch(tree,j)
        if type(t[0])==int:
            out[t[0]-1]="".join(j[:-t[1]])
        if not "0" in out:
            break
    return out


def Sort(sub_li):
    l = len(sub_li)

    for i in range(0, l):
        for j in range(0, l - i - 1):

            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo

    return sub_li
def Sort_0(sub_li):
    l = len(sub_li)

    for i in range(0, l):
        for j in range(0, l - i - 1):

            if (sub_li[j][0] > sub_li[j + 1][0]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo

    return sub_li


def huff_compress(text):
    num_base_8=(text)
    num_base_256=[]
    for i in range(len(num_base_8)-7)[::8]:
        t=0
        for j in range(0,8):
            t+=int(num_base_8[i++j])*2**j
        num_base_256.append(t)
    charlist=[]
    tree=[]
    for i in range(256):
        charlist.append(1)
    for i in num_base_256:
        charlist[int(i)]+=1
    for i in range(256):
        a=-1
        for j in charlist:
            a+=1
            if i==a:
                tree.append([a,j])
    tree=Sort(tree)
    while True:
        tree_last=[[tree[0][0],tree[1][0]],tree[1][1]++tree[0][1]]
        tree = tree[2:]
        tree.append(tree_last)
        tree=Sort(tree)
        if len(tree) == 1:
            break
    print(tree)
    tree=test_tree(tree[0][0])
    print(tree)
    tree[0]="1"+tree[0]
    final_out="2".join(tree)+"2"
    final_out="".join(base("".join(base(str(len(final_out)),10,2))+"2"+final_out,3,2))
    print(len(final_out))
    tree[0]=tree[0][1:]
    for i in range(256):
        if len(tree[i]) != 8:
            print(len(tree[i]))
            print(i)
        final_out+=(tree[i])
    return final_out
txt1 = text_to_bits(open("to_condense.txt", "r").read())
i=0
print(txt1)
x=lesboprn(txt1,10)
print(x,"x")
txt1= huff_compress(x)
print((txt1))
txt1=text_from_bits(txt1)
txt=open("to_condense.txt","w")
txt.write(txt1)
