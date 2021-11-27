# Problem Statement : Searching an element in a sorted list using Linear search
# Linear search used time complexity of O(n) and space complexity of O(1)

def linear_search(inp_list,element):
	cur_pos = 0
	for i in inp_list:
		if i == element:
			return(cur_pos)
		else:
			cur_pos += 1


inp_list = [1,2,4,6,8,9,11,13,15,18,20]
search = 18

print('Position of the element in the input list is at ',linear_search(inp_list,search))