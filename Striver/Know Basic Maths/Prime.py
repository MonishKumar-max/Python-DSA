#Check no is prime or not
n=13
divisors=[]
for n1 in range(1,n+1):
    if n%n1==0:
        divisors.append(n1)

if len(divisors)==2:
    print("It is a prime number")
else:
    print("It is not a prime number")    

# Mathematical optimal approach
import math

counter=0
for n1 in range(1,int(math.sqrt(n)+1)):
    if n%n1==0:
       counter+=1
       if (n/n1)!=n1:
            counter+=1
    
if counter==2:
    print("It is a prime number")
else:
    print("It is not a prime number")    