# Problem statement
# https://www.geeksforgeeks.org/segregate-0s-and-1s-in-an-array-by-traversing-array-once/

inp_list = [1, 0, 0 , 1, 0, 1, 0, 0, 1, 1, 1, 0 , 1 , 1 , 0]


def segregate(l):
    a_p = 0
    b_p = len(l)-1
    while a_p < b_p:
        if l[a_p] == 1 and l[b_p] == 0:
            l[a_p] = 0
            l[b_p] = 1
        if l[a_p] == 0:
            a_p += 1
        if l[b_p] == 1:
            b_p -= 1
    print(l)


print(segregate(inp_list))