from random import randint
from math import log2
import binascii
def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
digits=3840
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)
def generate(length_of_orgin_number):
    number="1"
    for interval in range(round(length_of_orgin_number)-1):
        digit=randint(0,1)
        number+=str(digit)
    return number
txt=open("to_condense.txt","w")
txt1=open("to_condense - copy.txt","w")
g=generate(digits)
txt.write(g)
txt1.write(g)