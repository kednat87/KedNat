# Problem statement
# https://www.geeksforgeeks.org/python-program-to-find-smallest-number-in-a-list/

inp_list = [5,4,2,1,6,8,4,9]


def smallest(l):
	s = l[0]
	for i in l:
		if i < s:
			s = i
	print(s)


smallest(inp_list)


# With sorting the current list

def smallest2(l):
	l.sort()
	print(l[0])


smallest2(inp_list)

# creating a new sorted list

l1 = sorted(inp_list)
print(l1[0])