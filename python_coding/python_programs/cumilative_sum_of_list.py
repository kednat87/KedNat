# Problem statement
# https://www.geeksforgeeks.org/python-program-to-find-cumulative-sum-of-a-list/

list = [10, 20, 30, 40, 50]

cum = []
sum = 0
for i in range(len(list)):
    sum+= list[i]
    cum.append(sum)

print(cum)
