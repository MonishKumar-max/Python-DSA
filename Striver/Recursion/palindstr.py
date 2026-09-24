# Brute force approach
string="ABA"
revstring=''
strarr=list(string)
revarr=strarr[::-1]

for l in revarr:
    revstring+=l

if revstring==string:
    print("It is a palindrome string")
else:
    print("It is not a palindrome string")    

# Recursive approach
start =0
end=len(string)-1

def Palindrome(string,start,end):
    if start>=end:
        return True
    
    if string[start]!=string[end]:
        return False
    
    return Palindrome(string,start+1,end-1)

output=Palindrome(string,start,end)
print(output)