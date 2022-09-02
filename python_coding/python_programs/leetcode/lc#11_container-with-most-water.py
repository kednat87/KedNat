# Problem statement
# https://leetcode.com/problems/container-with-most-water/

def get_vars(arr,lo,hi,width):
    '''Function returns low , high pointers and decreases the width'''
    if arr[lo] < arr[hi]:
        lo += 1
    else:
        hi -= 1
    width -= 1
    return lo,hi,width


def max_container(arr):
    ''' gets the maximum volume that can be stored in a container '''
    lo , hi = 0 , len(arr)-1
    width = len(arr)-1
    max_volume = 0
    mi = 0
    while lo < hi:
        if min(arr[lo],arr[hi]) < mi:
            lo , hi , width = get_vars(arr,lo,hi,width)
        else:
            mi = min(arr[lo],arr[hi])
            volume = width*mi
            if volume > max_volume:
                max_volume = volume
            lo , hi , width = get_vars(arr,lo,hi,width)

    return max_volume


container_lengths1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
container_lengths2 = [7, 8, 6, 2, 5, 4, 8, 3, 1]

print(max_container(container_lengths2))
