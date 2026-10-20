n=[2,3,3,1,4,3,2]
hashlist=[0]*(max(n)+1)

for i in n:
   hashlist[i]+=1  


max_freq=hashlist[0]
min_freq= float('inf')

for i in range(len(hashlist)):
   if hashlist[i]>max_freq:
      max_freq=hashlist[i]

for i in range(len(hashlist)):
    if hashlist[i] == 0:
      continue       
    if hashlist[i] < min_freq:
      min_freq = hashlist[i]

print(max_freq+min_freq)
