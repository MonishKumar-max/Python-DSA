# Brute : Printing until the recursion stack overflows.
def greet():
    print("hi")
    greet()
greet()    

# Optimized approach : Printing something by restricting to a certain number.
n=4
m=0
def greet(m):
    if m<n:
        print("hi")
        greet(m+1)
greet(m)   

# Using sys module to set recursion limit.
import sys
n=5
sys.setrecursionlimit(n+1)

def name():
    print("Asish")
    name()
name()    