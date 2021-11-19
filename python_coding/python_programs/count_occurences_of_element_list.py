# Problem statement
# https://www.geeksforgeeks.org/python-count-occurrences-element-list/

# Example 1 when search element is only 1

# List given
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]

# search element
x = 10

d = {}

for i in lst:
    if i in d.keys():
        d[i] = d[i] + 1
    else :
        d[i] = 1

# printing counts for given element
print('Element '+str(x)+' occurs '+ str(d[x])+' times')

# using count function
print(lst.count(x))


print('====================================================')
# Example 1 when search element are multiple

# List given
lst = [15, 6, 7, 10, 12, 20, 10, 28, 10, 6, 15]

# search element
search_x = [10,0,6]

for i in search_x:
    d = {}
    for j in lst:
        if j in d.keys():
            d[j] = d[j] + 1
        else :
            d[j] = 1

    # printing counts for given element . Here dictionary element is defaulted to 0 if it doesnt exst
    print('Element ' + str(i) + ' occurs ' + str(d.get(i,0)) + ' times')






