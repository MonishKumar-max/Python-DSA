import sys
n=7
m=0
current_sum=0
prev_sum=0
sys.setrecursionlimit(100)
def name():
    global current_sum
    global prev_sum
    global m
    if n>=m:
        m+=1
        old_sum=current_sum
        current_sum=prev_sum+current_sum
        prev_sum=old_sum
        print(old_sum)
        if current_sum==0:
            current_sum=1
    name()
name()        