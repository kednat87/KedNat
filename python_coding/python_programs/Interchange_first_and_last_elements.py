# Problem statement
# https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/

# By using variables

def interchange(inp_list):
    out_list = inp_list[:]
    a = inp_list[0]
    b = inp_list[-1]
    out_list[0] = b
    out_list[-1] = a
    print(out_list)


input = [1, 2, 3, 4, 5]
interchange(input)


# By not using any variables

def interchange_1(inp_list1):
    out_list1 = inp_list1[-1] + inp_list1[1:len(inp_list1)] + inp_list1[0]
    print(out_list1)


input1 = [1, 2, 3, 4, 5]
interchange(input1)


# swapping the elements in the same list

def interchange_2(inp_list2):
    inp_list2 = inp_list2[-1] + inp_list2[1:len(inp_list2)] + inp_list2[0]
    print(inp_list2)


input2 = [1, 2, 3, 4, 5]
interchange(input2)
