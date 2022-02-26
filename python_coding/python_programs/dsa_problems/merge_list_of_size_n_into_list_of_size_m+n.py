# Problem statement
# https://www.geeksforgeeks.org/merge-one-array-of-size-n-into-another-one-of-size-mn/

mn = [2, 8, None, None, None, 13, None, 15, 20]
n = [5, 7, 9, 25]


def merge(a,b):
    pos_mn = 0
    pos_n = 0
    for i in mn:
        if i is None:
            mn[pos_mn] = n[pos_n]
            pos_n += 1
        pos_mn += 1
    return mn


print(merge(mn,n))