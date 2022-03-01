# Problem Statement
# https://www.geeksforgeeks.org/program-for-array-rotation-continued-reversal-algorithm/

input_list = [1, 2, 3, 4, 5, 6, 7]
r = 2


# def rotate_list(l):
#     new_list = []
#     for i in range(len(l)-1,-1,-1):
#         new_list.append(l[i])
#     return new_list


def rotate(l,r):
    right_list = l[:len(l)-r]
    left_list = l[len(l)-r:]
    rotated_list = left_list + right_list
    return rotated_list


print(rotate(input_list,r))