n=5
m=1
multiply=1
def name():
    global m
    global multiply
    if n>=m:
       multiply=multiply*m
       m+=1
       name()
    else:
        return multiply   
name()    
print(multiply)    