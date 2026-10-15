n=13
count=0
divisors=[]

for i in range(1,n+1):
    for n1 in range(1,i+1):
        if i%n1==0:
            divisors.append(n1)
    if len(divisors)==2:
        count+=1
    divisors=[]            
print(count)
