# Problem Statement : Searching an element in a sorted list using Binary search
# Linear search used time complexity of O(log n) and space complexity of O(1)
import time


def binary_search(inp_list, element):
    low = 0
    hi = len(inp_list) - 1
    while low <= hi:
        mid = low + ((hi - low) // 2)
        if inp_list[mid] == element:
            return mid
        elif inp_list[mid] < element:
            low = mid + 1
        else:
            hi = mid - 1


# test cases
test = [{"l": [1, 2, 4, 6, 8, 9, 11, 13, 15, 18, 20], "e": 18, "o": 9},
        {"l": [1, 2, 4, 6, 8, 9, 11, 13, 15, 18, 20], "e": 9, "o": 5},
        {"l": list(range(1, 10000000, 1)), "e": 2, "o": 1}
        ]

tc = 0
for i in test:
    tc += 1
    if binary_search(i['l'], i['e']) == i['o']:
        print('Test case ' + str(tc) + ' Passed !!!')
    else:
        print('Test case ' + str(tc) + ' Failed !!!')
