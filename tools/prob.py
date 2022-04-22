from collections import Counter

import random

# ite = 10000
# result = []

# for i in range(ite):
#     place = 0
#     t = 0
#     while True:
#         r = random.random()
#         t += 1
#         if r > 0.5:
#             place += 1
#             place = place%7
#         elif r < 0.5:
#             place -= 1
#             place = place%7
#         if place == 0:
#             result.append(t)
#             break

# print(Counter(result))


# Python3 implementation of the above approach
import numpy as np
 
# Function to return the probability when
# number of heads is greater than
# the number of tails
def Probability(p, n) :
 
    # Declaring the DP table
    dp = np.zeros((n + 1, n + 1));
    for i in range(n + 1) :
        for j in range(n + 1) :
            dp[i][j] = 0.0
 
    # Base case
    dp[0][0] = 1.0;
 
    # Iterating for every coin
    for i in range(1, n + 1) :
 
        # j represents the numbers of heads
        for j in range(i + 1) :
 
            # If number of heads is equal to zero
            # there there is only one possibility
            if (j == 0) :
                dp[i][j] = dp[i - 1][j] * (1.0 - p[i]);
            else :
                dp[i][j] = (dp[i - 1][j] * (1.0 - p[i]) +
                            dp[i - 1][j - 1] * p[i]);
     
    ans = 0.0;
 
    # When the number of heads is greater than (n+1)/2
    # it means that heads are greater than tails as
    # no of tails + no of heads is equal to n for
    # any permutation of heads and tails
    for i in range((n + 1)// 2, n + 1) :
        ans += dp[n][i];
 
    return ans;
 
# Driver Code
if __name__ == "__main__" :
     
    # 1 based indexing
    p = [ 0.0, 0.3, 0.4, 0.7 ];
 
    # Number of coins
    n = len(p) - 1;
 
    # Function call
    print(Probability(p, n));
 
# This code is contributed by AnkitRai01