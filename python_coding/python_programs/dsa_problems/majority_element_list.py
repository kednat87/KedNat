# Problem statement
# https://www.geeksforgeeks.org/majority-element/

inp_list = [3, 3, 4, 2, 4, 4, 4, 4]


def majority_elem(l):
    d = {}
    a = len(l)
    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1

    for k,v in d.items():
        if v >= a/2:
            statement = str(k) + ' is repeating ' + str(v) + ' times'
            return statement

    statement = 'No Majority Element'
    return statement


print(majority_elem(inp_list))