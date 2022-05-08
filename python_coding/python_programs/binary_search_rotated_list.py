# Binary search a rotated list

def find_rot(inp_list, lo, hi):
    print(inp_list[lo:hi+1],lo,hi)
    if (hi - lo) == 1 and (inp_list[hi] < inp_list[lo]):
        print('in')
        return hi
    elif inp_list[hi] > inp_list[lo]:
        return 'No'
    elif inp_list[hi] < inp_list[lo]:
        mid = lo + (hi - lo) // 2
        print(hi,lo,mid)
        lout , rout = find_rot(inp_list, lo, mid) , find_rot(inp_list, mid , hi)
        if lout != 'No':
            return lout
        elif rout != 'No':
            return rout
        else:
            return 'List is not rotated'


print(find_rot([6, 7, 8, 0, 1, 2, 3, 4, 5], 0,8))
#print(find_rot([1, 2, 3, 4, 5], 0,4))
#print(find_rot([6, 0, 1, 2, 3, 4, 5], 0,6))