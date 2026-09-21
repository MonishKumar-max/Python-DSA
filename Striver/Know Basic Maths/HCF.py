# Brute force approach
n1=36
n2=18
factors=[]

for n in range(1, min(n1, n2)+1):
    if n1%n==0 and n2%n==0:
        factors.append(n)
length=len(factors)
maxno=factors[length-1]
print(maxno)
             
#Euclidean Algorithm  

while n1>0 and n2>0:
    if n1>n2:
        n1=n1%n2
    elif n2>n1:
        n2=n2%n1
    if n1==0:
        print(n2) 
    else:
        print(n1)           