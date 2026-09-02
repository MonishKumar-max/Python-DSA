n=5
count=65
for i in range(n,0,-1):
    for j in range(i):
        print(chr(count),end='')
        count+=1
    count=65    
    print('')    

