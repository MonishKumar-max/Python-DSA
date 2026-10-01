arr=[4,1,7,6,3,2,8]
high=len(arr)-1
low=0

def Partition(arr,high,low):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>=pivot and j>=low+1:
            j-=1
        if i<j:    
            arr[i],arr[j]=arr[j],arr[i] 
    arr[low],arr[j]=arr[j],arr[low] 
    return j

def quick_sort(arr,high,low):
    if low<high:
        p_index=Partition(arr,high,low)
        quick_sort(arr,p_index-1,low)
        quick_sort(arr,high,p_index+1)
quick_sort(arr,high,low)      
print(arr) 