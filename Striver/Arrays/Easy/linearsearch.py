arr=[1,0,4,8,22,3,5,9]
n=len(arr)
num=22

for i in range(n-1,0,-1):
    for j in range(0,i):
        if arr[j]==num:
            index=j
print("The number %d is at index %d"%(num,index))
    