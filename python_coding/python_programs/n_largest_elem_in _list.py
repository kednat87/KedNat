# Problem Statement
# https://www.geeksforgeeks.org/python-program-to-find-n-largest-elements-from-a-list/

l = [10,9,4,5,7,2]
n = 3

# Bubble Sort the list first

# first loop range is length-1 as it would take maximum n-1 iterations for smallest element to arrive at starting of list and vice versa
# second loop range is length-1 as there would be only n-1 swaps in a given iteration

for i in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i],l[i+1] = l[i+1], l[i]

print(l[-2:])

# Using sort method
l = [4,2,5,9,10,7]
l.sort(reverse=True)
print(l[:2])