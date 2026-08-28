n=11
for i in range(0,n-3):
    for j in range(i):
        print("*",end='')
    print('')    

for i in range(n-3,0,-1):
    for j in range(i):
        print("*",end='')
    print('')    