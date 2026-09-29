arr=[2,6,2,1,0,9,5]
n=len(arr)

for i in range(1,n):
    j=i
    while arr[j-1]>arr[j] and j>0:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
print(arr)        

# revision 
for i in range(1,n):
    j=i
    while arr[j-1]>arr[j] and j>0:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
print(arr)        