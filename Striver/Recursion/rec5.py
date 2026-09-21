n=4
m=1
sum=0
def name():
    global m
    global sum
    if n>=m:
       sum+=m
       m+=1
       name()
    else:
        return sum   
name()    
print(name())    