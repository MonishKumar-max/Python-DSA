# SUBSCRIPTIONS:

# A new TV streaming service was recently started in Chefland called the Chef-TV.

# A group of N friends in Chefland want to buy Chef-TV subscriptions. We know that 6 people can share one Chef-TV subscription. 
# Also, the cost of one Chef-TV subscription is  X rupees. 

# Determine the minimum total cost that the group of  N friends 
# will incur so that everyone in the group is able to use Chef-TV.

# INPUT FORMAT:

# The first line contains a single integer T — the number of test cases.
#  Then the test cases follow.
# The first and only line of each test case contains two integers N and  X — 
# the size of the group of friends and the cost of one subscription.

# OUTPUT FORMAT:
# For each test case, 
# output the minimum total cost that the group will incur 
# so that everyone in the group is able to use Chef-TV.

# INPUT:   OUTPUT:
# 3        100
# 1 100    500
# 12 250   405
# 16 135

T=int(input())

for _ in range(T):
    N,X=map(int,input().split())
    
    count=-(N//-6)
    cost=count*X
    print(cost)