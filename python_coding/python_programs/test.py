# l = [8, 2, 5, 3]
# s = 7
#
#
# def solve(l, s, n):
#     if s == 0:
#         dp[n][s] = 1
#         return dp[n][s]
#     if n == 0:
#         dp[n][s] = 0
#         return dp[n][s]
#     if l[n - 1] > s:
#         return solve(l, s, n - 1)
#     else:
#         return solve(l, s, n - 1) or solve(l, s - l[n - 1], n - 1)
#
#
# dp = [[0 for j in range(s+1)] for i in range(len(l)+1)]
# print(solve(l,s,len(l)))
# print(dp)
#
#
# s1 = ['A', 'C', 'G', 'O', 'T']
# s2 = ['B', 'A', 'G', 'T', 'D']
#
# table = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
#
# for i in range(len(s1) ):
#     for j in range(len(s2) ):
#         if s1[i] == s2[j]:
#             table[i+1][j + 1] = 1 + table[(i-1)] [j]
#         else:
#             table[i+1][j+1] = table[(i)][j]
#
# print(table)
#

#
# def solve(n):
#     if n <= 2:
#         dp[n] = n
#         return n
#     else:
#         if dp[n-1] == 0 and dp[n-1] == 0:
#             sol = solve(n - 2) * (n - 1) + solve(n - 1)
#         else:
#             sol = dp[n-2] * (n - 1) + dp[n-1]
#         dp[n] = sol
#         return sol
#
#
# n = 100
# dp = [0 for i in range(n+1)]
# print(solve(n))
# print(dp)


# # Gold Mine Problem
# # https://www.geeksforgeeks.org/gold-mine-problem/
#
# def solve():
#     out = 0
#     for j in range(n-1, -1, -1):
#         for i in range(m):
#             if j == n-1:
#                 dp[i][j] = gold[i][j]
#             elif i == 0:
#                 dp[i][j] = max(dp[i][j+1],dp[i+1][j+1])+gold[i][j]
#             elif i == m-1:
#                 dp[i][j] = max(dp[i][j+1], dp[i-1][j+1])+gold[i][j]
#             else:
#                 dp[i][j] = max(dp[i][j+1], dp[i-1][j+1],dp[i][j+1])+gold[i][j]
#             if j==0:
#                 out = max(out,dp[i][j])
#     return out
#
# gold = [[1, 3, 1, 5],
#         [2, 2, 4, 1],
#         [5, 0, 2, 3],
#         [0, 6, 1, 2]]
#
# m, n = len(gold), len(gold[0])
# dp = [[0 for j in range(n)] for i in range(m)]
# print(solve())
# print(dp)


# def solve(arr,n):
#     for x in range(n):
#         print('------')
#         print(x)
#         for i in range(x-1,-1,-1):
#             print(i)
#             print('---')
#             print(x)
#             if i == 0:
#                 pass
#             elif arr[n] % arr[i] == 0:
#                 if dp[i] > 1:
#                     sol = dp[i] + 1
#                 else:
#                     sol = solve(arr,i)+1
#                 dp[n] = sol
#
#
# arr = [1, 3, 6, 13, 17, 18]
#
# dp = [1 for i in range(len(arr))]
# a = len(arr)-1
# print(a)
# solve(arr,a)
# print(dp)

# rod = [3, 5, 8, 9, 10, 17, 17, 20]
# rod.insert(0,0)
# print(rod)
# rod_den = []
# rod_den.insert(0,0)
# for i in range(1,len(rod)):
#     rod_den.insert(i,rod[i]/i)
# print(rod_den)
#
# l = []
#
# def solve(rod_den,n):
#     maxi = 0.0
#     max_i = 0
#     rem = 0
#     val = 0
#     for i in range(len(rod_den)):
#         if rod_den[i] > maxi:
#             maxi = rod_den[i]
#             max_i = i
#     if n/2 < max_i:
#         rem = n-max_i-1
#     elif n/2 >= max_i:
#         val = n//max_i
#         rem = n-(val*max_i)
#     return (max_i,rem,val)
#
#
# r = 8
# m = 0
# while r != 0:
#     m , r , v = solve(rod_den[:r+1],r+1)
#     print(m,v,r)
#     if v == 0:
#         l.append(m)
#     else:
#         for i in range(v):
#             l.append(m)
#     print(m,r)
#
# print(l)

from time import sleep


# def solve(w):
#     s = []
#     c = 0
#     for i in w:
#         if c == 0:
#             s.append(i)
#             s.append('')
#             c += 1
#         else:
#             k = [i for i in s]
#             for j in k:
#                 s.remove(j)
#                 new_st = j+i
#                 s.append(new_st)
#                 s.append(j)
#     print(s)
#
# word = 'kedharnatekar'
# solve(word)

#
# l = [-1 , 2, 3, -2, 4]
#
#
# def solve(l, n):
#     if n == 0:
#         return l[0], l[0]
#     else:
#         res = solve(l, n - 1)
#         a = res[0] * l[n]
#         b = res[1] * l[n]
#         if a >= b:
#             max = a
#             min = b
#         else:
#             max = b
#             min = b
#         return max, min
#
#
# print(solve(l, len(l) - 1))

l = [1,2,3,1,2]
s = set(l)
print(s)

t = (1,2,3)
print(t)

s.add(4)
s.add(3)
print(s)