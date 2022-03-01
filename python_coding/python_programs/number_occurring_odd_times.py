# Problem statement
# https://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/

inp_list = [1, 2, 3, 2, 3, 1, 3]


def odd_times(l):
    d = {}
    for i in l:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1

    for k,v in d.items():
        if v%2 == 1:
            return k

    return 'No odd number of times occurences'

print(odd_times(inp_list))
