string="abcdcsahsdghhguhzk"
hash_list=[0]*26

for chr in string:
    asciino=ord(chr)-97
    hash_list[asciino]+=1
print(hash_list)        