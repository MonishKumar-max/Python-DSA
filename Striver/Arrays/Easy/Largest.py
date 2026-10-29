arr=[2,6,1,8,2,9]
n=len(arr)

# Brute-force approach
for i in range(0,n-1):
    minno=i
    for j in range(i+1,n-1):
        if arr[j]<arr[minno]:
            newarr=arr[j]
            arr[j]=arr[minno]
            arr[minno]=newarr
Largelement=arr[n-1]
print(Largelement)

# Optimal approach
max_no=arr[0]
for i in range(n):
    if arr[i]>max_no:
        max_no=arr[i]
print(max_no)        