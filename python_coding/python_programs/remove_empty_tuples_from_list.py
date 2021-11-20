# Problem statement
# https://www.geeksforgeeks.org/python-remove-empty-tuples-list/
# this problem statement can also be said as remove a particular element from the list

tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]

# everytime there is a check if () is present in list. If exists first element is removed.
# loop exists when () is completely removed
while () in tuples:
    tuples.remove(())
print(tuples)

# Using filter method
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
tuples = filter(None,tuples)
print(tuples)
# above returned tuples object is filter object. Hence looping to create a new list
t = []
for i in tuples:
    print(i)
    t.append(i)
print(t)

# Using list comprehension
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),('krishna', 'akbar', '45'), ('',''),()]
tuples = [t for t in tuples if t]
print(tuples)