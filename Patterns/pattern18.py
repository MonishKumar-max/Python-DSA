count=65
for i in range(1,5):
    for j in range(4-i):
        print(' ',end='')
    for j in range(i):
        print(chr(count),end='')
        count+=1 
    for j in range(i-1, 0, -1):
        print(chr(64 + j), end='')
    for j in range(4-i):
        print(' ',end='')       
    count=65 
    print('')    