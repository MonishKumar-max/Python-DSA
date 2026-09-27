arr=[2,6,1,0,4,8,3,5]
n=len(arr)

# True re-written selection sort
for i in range(n):
    minno=i
    for j in range(i+1,n):
        if arr[j]<arr[minno]:
            minno=j
    arr[i],arr[minno]=arr[minno],arr[i]        
print(arr)    