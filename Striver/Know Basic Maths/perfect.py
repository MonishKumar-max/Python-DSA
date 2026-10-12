n=6
divisors=[]
def Perfect():
    for n1 in range(1,n):
        if n%n1==0:
            divisors.append(n1)
    current_sum=0
    for i in range(len(divisors)):
        current_sum+=divisors[i]
    if current_sum == n:
        return True
    else:
        return False        
print(Perfect())   
    