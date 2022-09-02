# Gold Mine Problem
# https://www.geeksforgeeks.org/gold-mine-problem/

def solve():
    out = 0
    for j in range(n-1, -1, -1):
        for i in range(m):
            if j == n-1:
                dp[i][j] = gold[i][j]
            elif i == 0:
                dp[i][j] = max(dp[i][j+1],dp[i+1][j+1])+gold[i][j]
            elif i == m-1:
                dp[i][j] = max(dp[i][j+1], dp[i-1][j+1])+gold[i][j]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i-1][j+1],dp[i][j+1])+gold[i][j]
            if j==0:
                out = max(out,dp[i][j])
    return out

gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]

m, n = len(gold), len(gold[0])
dp = [[0 for j in range(n)] for i in range(m)]
print(solve())
print(dp)
