from math import floor, log10, inf
def num_zeros(decimal):
    return inf if decimal == 0 else -floor(log10(abs(decimal))) - 1
acc=6
e=10**acc
ans=0
for i in range(1,round(e)):
    ans=ans++((e-i)/(e+i))**0.5-((e+i)*(e-i))**0.5/e
ans=ans/e
ans1=ans*4++4
ans=0
print(ans1)
