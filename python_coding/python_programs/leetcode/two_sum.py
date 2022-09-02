# Problem Statement
# https://leetcode.com/problems/two-sum/

def two_sum(arr,tsum):
    position_dict = {}
    length = len(arr)
    for i in range(length):
        if (tsum-arr[i]) in position_dict.keys():
            return arr[i] , tsum-arr[i]
        else:
            position_dict[arr[i]] = i


list_inp= [4,2,1,8,7]
tsum = 5

print(two_sum(list_inp,tsum))