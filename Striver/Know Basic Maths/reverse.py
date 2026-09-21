#  Time = O((log n)²)
#  Space = O(log n)

n=1345
revdigit=0
while n>0:
    digit=n%10
    revdigit=revdigit*10+digit
    n=n//10
print(revdigit)    