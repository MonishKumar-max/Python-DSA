# Problem-1
N=7

for i in range(N):
  for j in range(N):
    print("*",end='')
  print()  

print(" ")

# Problem-2

for i in range(N):
  for j in range(i+1):
    print("*",end='')
  print()  

print(" ")

# Problem-3

for i in range(5,0,-1):
  for j in range(i):
    print("*",end='')
  print()    

print(" ")

# Problem-3

for i in range(1,N):
  for j in range(N,0,-1):
    if j>i:
      print(" ",end='')
    else:
      print("*",end='')  
  print()    

print(" ")
# problem-4

k=1
for i in range(1,N+1):
  for _ in range(k):
    print("*",end='')
  k+=2  
  print()

print(' ')

# problem-5

K=1
for i in range(N,0,-1):
  for j in range(i):
    if i==N:
      print("*",end='')
    elif j==0 or j==N-K:
      print("*",end='')
    else:
      print(" ",end='')  
  K+=1
  print()    
