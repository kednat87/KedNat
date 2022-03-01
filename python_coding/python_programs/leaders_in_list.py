# Problem statement
# https://www.geeksforgeeks.org/leaders-in-an-array/

input_list = [16, 17, 4, 3, 6, 5, 2]


def leaders(l):
    output= []
    output.append(l[-1])
    for i in range(len(l)-1,-1,-1):
        if l[i-1] > max(l[i:]):
            output.append(l[i-1])

    output.reverse()
    return output


print(leaders(input_list))