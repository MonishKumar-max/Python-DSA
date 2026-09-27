arr=[1,5,9,10,4,23,5]
n=len(arr)

for i in range(n-1,0,-1):
    for j in range(0,i):
        if arr[j]>arr[j+1]:
            t=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=t
print(arr)            