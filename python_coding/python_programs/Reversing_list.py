# Problem Statement
# https://www.geeksforgeeks.org/python-reversing-list/

def reverse_list(l):
    new_l = []
    for i in range(len(l),0,-1):
        new_l.append(l[i-1])
    print(new_l)


reverse_list([4,5,6,7,8])

# Other ways
l = [4,5,6,7,8]
print(l[::-1])

# Reverse the list itself
l.reverse()
print(l)

l = [4,5,6,7,8]
for i in reversed(l):
    print(i)