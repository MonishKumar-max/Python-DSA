arr=[7,2,9,0,1,4,6]
n=len(arr)

def insertion(arr1,n):
    if n<=1:
        return arr1

    for i in range(1,n):
       j=i
       while arr[j-1]>arr[j] and j>0:
           arr[j-1],arr[j]=arr[j],arr[j-1]
           j-=1
    insertion(arr1,n-1)
    return arr1       

output=insertion(arr,n)    
print(output)


