# Optimal approach (rewritten)
n=[2,3,3,1,4,3,2]
hashlist=[0]*(max(n)+1)

for i in n:
   hashlist[i]+=1  
print(hashlist)

max_freq=hashlist[0]
min_freq, min_elem = float('inf'), n[0]
max_no=0
for i in range(len(hashlist)):
   if hashlist[i]>max_freq:
      max_freq=hashlist[i]
      max_no=i

for i in range(len(hashlist)):
    if hashlist[i] == 0:
      continue       
    if hashlist[i] < min_freq:
      min_freq = hashlist[i]
      min_elem=i
   
print("Minimum occuring element: %s"%min_elem)   
print("Maximum occuring element: %s"%max_no)

#  ...............................................................................................
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

m=[3,5,6,7,8,4,6,4,3,3]
hash_list=[0]*(max(m)+1)

for i in m:
   hash_list[i]+=1
print(hash_list)   

max_el,max_fre=hash_list[0],0

for i in range(len(hash_list)):
   if hash_list[i]>max_fre:
      max_fre=hash_list[i]
      max_el=i

print("Max element:%s"%max_el)
print("Max frequency:%s"%max_fre)

min_el,min_freq=float('inf'),m[0]

for i in range(len(hash_list)):
   if hash_list[i]==0:
      continue
   elif hash_list[i]<min_freq:
      min_freq=hash_list[i]
      min_el=i

print("min element:%s"%min_el)
print("min frequency:%s"%min_freq)
