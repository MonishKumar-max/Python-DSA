n=6
count=65
for i in range(1,n):
    for j in range(i):
        print(chr(count),end='')
    count+=1    
    print('')    