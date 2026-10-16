n = [3, 4, 6, 3, 5, 7, 8, 3, 8]
m = [2, 5, 7, 3, 6, 5, 8]

# Initialize an empty dictionary to store counts
hash_dict = {}

for i in n:
    if i in hash_dict:
        hash_dict[i]+=1
    else:
        hash_dict[i]=1    
print(hash_dict)
for i in m:
    print(i,":",hash_dict.get(i,0))
