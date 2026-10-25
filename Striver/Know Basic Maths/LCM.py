n1=36
n2=18
HCF=0
a=n1
b=n2

while n1>0 and n2>0:
   
    if n1>n2:
        n1=n1%n2
    elif n2>n1:
        n2=n2%n1
    if n1==0:
        HCF=n2
    else:
        HCF=n1

LCM=(a*b)//HCF
print(LCM)