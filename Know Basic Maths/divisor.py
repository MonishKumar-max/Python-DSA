# Print all the divisors
#brute force
n=36
divisors=[]
for n1 in range(1,n+1):
    if n%n1==0:
        divisors.append(n1)
print(divisors)        

# Mathematical optimal approach
import math
divisors1=[]
for i in range(1,int(math.sqrt(n)+1)):
    if n%i==0:
        divisors1.append(int(i))
        if (n/i)!=i:
            divisors1.append(int(n/i))
divisors1.sort()            
print(divisors1)