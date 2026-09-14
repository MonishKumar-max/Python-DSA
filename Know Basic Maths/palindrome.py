# Time: O(d)
# Space: O(d)
# (d = number of digits)

n=121
revdigit=0
original_n=n
while n>0:
    digit=n%10
    revdigit=revdigit*10+digit
    n=n//10
revnumber=revdigit
if revnumber==original_n:
    print("Palindrome number")
else:
    print("It is not a palindrome number")    