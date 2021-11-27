# Problem Statement : Searching an element in a sorted list using Linear search
# Linear search used time complexity of O(n) and space complexity of O(1)

def linear_search(inp_list, element):
    """Defining a function for linear search
	"""
    cur_pos = 0
    for i in inp_list:
        if i == element:
            return cur_pos
        else:
            cur_pos += 1


# test cases
test = [{"l": [1, 2, 4, 6, 8, 9, 11, 13, 15, 18, 20], "e": 18, "o": 9},
        {"l": [1, 2, 4, 6, 8, 9, 11, 13, 15, 18, 20], "e": 9, "o": 5},
        {"l": list(range(10000000, 0, -1)), "e": 2, "o": 9999998}
        ]

test_no = 1
for i in test:
    if linear_search(i['l'], i['e']) == i['o']:
        print('Test case ' + str(test_no) + ' passed !!!')
    else:
        print('Test case ' + str(test_no) + ' failed !!!')
    test_no += 1
