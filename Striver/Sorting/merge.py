arr=[1,5,2,7,0,9]

def merge_sort(arr1):
    if len(arr1)<=1:
        return arr1
    
    mid=len(arr1)//2
    firsthalf=arr1[:mid]
    secondhalf=arr1[mid:]
    left=merge_sort(firsthalf)
    right=merge_sort(secondhalf)
    return merge_array(left,right)

def merge_array(left1,right1):
    i,j=0,0
    result=[]
    while i<len(left1) and j<len(right1):
        if left1[i]<=right1[j]:
            result.append(left1[i])
            i+=1
        elif left1[i]>=right1[j]:
            result.append(right1[j])
            j+=1

    if i<len(left1):
        while i<len(left1):
           result.append(left1[i])
           i+=1

    if j<len(right1):
         while j<len(right1):
           result.append(right1[j])
           j+=1
    return result
output=merge_sort(arr)
print(output)                    