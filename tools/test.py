import math

def rec(depth):
    if depth==1 or depth==0:
        return 1
    else:
        return rec(depth-2) + depth

def closed(n):
    return 1 + n*n/2 - (n+2)*n/4


for i in range(2,10):
    k = i
    print(k,":",rec(k),",",closed(k))
