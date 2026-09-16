import math
n=153
original_n=n
length=len(str(n))
amstrngno=0
while n>0:
    digit=n%10
    amstrngno+=math.pow(digit ,length)
    n=n//10
if amstrngno==original_n:
    print("The no is Amstrong number")
else:
    print("The no is not an amstrong number")    

