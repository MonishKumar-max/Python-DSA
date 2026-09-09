for i in range(10):
    for j in range(1):
        if i%3==0:
           print("*",end='')
        else:
            print(" ",end='')
    for j in range(2):
        if i==0 or i==9:
            print("*",end='')
        else:
            print(" ",end='')
    for j in range(1):
        if i%3==0:
           print("*",end='')
        else:
            print(" ",end='')                       
    print('')     
