# Problem statement
# https://www.geeksforgeeks.org/python-cloning-copying-list/

l1 = [1,3,5,4,2]

# copying methods

# Slicing
l2 = l1[:]
# copy command
l3 = l1.copy()
# = operator. If we use = operator then any modifications in original list will modify the assigned list
l4 = l1


print('Original list l1 :',l1)
print('l2 list : ',l2)
print('l3 list : ',l3)
print('l4 list : ',l4)

# Testing by appending one extra element to the original list
l1.append(7)

print('\nOriginal list l1 :',l1)
print('l2 list : ',l2)
print('l3 list : ',l3)
print('l4 list : ',l4)