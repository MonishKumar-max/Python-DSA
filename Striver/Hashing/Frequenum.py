n=[3,4,6,3,5,7,8,3,8]
m=[2,5,7,3,6,5,8]
hashlist=[0]*(max(n)+1)
for i in n:
   hashlist[i]+=1  

for i in m:
  print(i,":",hashlist[i])