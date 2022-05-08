# Binary search where elements are repeated more than once. Such cases the position of first occurrence should be returned

def check_repetition(inp_list):
    leng = len(inp_list)
    elem = inp_list[leng-1]
    for i in range(leng-1,-1,-1):
        if elem == inp_list[i]:
            pass
        else:
            return i+1


def binary_search(inp_list,elem):
    lo = 0
    hi = len(inp_list)
    while lo <= hi:
        mid = lo + (hi-lo)//2
        if elem == inp_list[mid]:
            return check_repetition(inp_list[:mid + 1])
        elif elem < inp_list[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return 'Element not found !!!'


testcase1 = {"input":[1,2,2,2,2,3,3,3,3,4,4,4,4,5,6] , "elem" : 2 , "output" : 1 }

print(binary_search(testcase1["input"],testcase1["elem"]))







