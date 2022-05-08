# Binary search a list of non repetetive element
import time


def binary_search(inp_list,elem):
    lo = 0
    hi = len(inp_list) -1
    while lo <= hi:
        mid = lo+(hi - lo) // 2
        if elem == inp_list[mid]:
            return mid
        elif elem > inp_list[mid]:
            lo = mid+1
        else:
            hi = mid-1
    return 'Element not found !!!'


testcase1 = {"inp_list":[2,5,6,7,10,11,13,17,19,24] , "elem" : 19 , "output" : 8 }
testcase2 = {"inp_list":[2,5,6,7,10,11,13,17,19,24] , "elem" : 100 , "output" : 'Element not found !!!' }
testcase3 = {"inp_list":[i for i in range(10000)], "elem" : 9999 , "output": 9999}

testcases = [testcase1,testcase2,testcase3]

for i in testcases:
    out = binary_search(i["inp_list"], i["elem"])
    if out==i["output"]:
        print('Test case '+str(i)+' Passed')
    else:
        print('Test case '+str(i)+' Failed')
        print('Expected :'+str(i["output"]))
        print('Actual :'+str(out))

