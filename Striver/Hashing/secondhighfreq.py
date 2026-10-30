m=[3,5,6,7,8,4,6,4,3,3]
hash_list=[0]*(max(m)+1)

for i in m:
   hash_list[i]+=1
print(hash_list)   

max_freq=0
second_max_freq=0

for i in range(len(hash_list)):
   if hash_list[i]>max_freq:
      second_max_freq=max_freq
      max_freq=hash_list[i]
   elif hash_list[i]>second_max_freq:
      second_max_freq=hash_list[i]
  

print(" Second Max frequency:%s"%second_max_freq)