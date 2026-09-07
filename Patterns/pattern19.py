count=69
for i in range(0,6):
    for j in range(i):
        print(chr(count),end='')
        count=count+1
    count=69    
    count=count-i
    print('')    