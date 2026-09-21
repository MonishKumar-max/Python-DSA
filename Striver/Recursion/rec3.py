# Print 1 to N using Recursion

# Problem Description: Given an integer N, write a program to print numbers from 1 to N.

import sys
n=7
m=1
sys.setrecursionlimit(n+1)

def name():
    global m
    print(m,end=',')
    m+=1   
    name()
name()    