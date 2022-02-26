# Problem statement
# https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/

inp_list = [0, -1, 2, -3, -1]
sum_elem = -2


def two_sum(l,s):
	r = len(l)
	for i in range(r):
		a = l[i]
		l1 = l[i+1:]
		for j in l1:
			if a+j == s:
				return a,j
	return 'No matching sum'


print(two_sum(inp_list,sum_elem))