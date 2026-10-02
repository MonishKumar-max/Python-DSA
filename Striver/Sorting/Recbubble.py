arr=[2,3,4,1,0,6,8,3]
n=len(arr)

def bubble(arr1,n):
    if n<=1:
        return arr1
    
    for i in range(n-1,0,-1):
        minno=i
        if arr1[minno-1]>arr1[minno]:
            newarr=arr1[minno-1]
            arr1[minno-1]=arr1[minno]
            arr1[minno]=newarr
    bubble(arr1,n-1)        
    return arr1    

output=bubble(arr,n)
print(output)    

def bubble2(arr,n):
    if n<=1:
        return arr
    for i in range(n-1,0,-1):
        j=i
        if arr[j-1]>arr[j]:
            new=arr[j-1]
            arr[j-1]=arr[j]
            arr[j]=new
        bubble2(arr,n-1)
        return arr    
output1=bubble2(arr,n)
print(output1)