# Print N to 1 using Recursion

# Problem Description: Given an integer N, write a program to print numbers from N to 1.
import sys
n=7
m=n
sys.setrecursionlimit(n+1)

def name():
    global m
    print(m)
    m-=1
    name()
name()    