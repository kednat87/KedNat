# Problem statement : A list has elements in sorted ascending order. Find the first and last occurrence of the the given element
# eg : for list [1,1,2,3,3,3,4,5] and search element of 3 , then its first occurrence is 3 rd position and last occurrence is 5

def is_first_last(inp_list, mid):
    first = False
    last = False
    if inp_list[mid + 1] != inp_list[mid]:
        last = True
    if inp_list[mid - 1] != inp_list[mid]:
        first = True
    return first, last


def get_left(inp_list,low,mid):
    hi = mid
    while inp_list[mid-1] == inp_list[mid]:
        mid = low + (hi - low) // 2
        hi = mid
        low = mid +1
    return mid-1


def get_last(inp_list,hi,mid):
    lo = mid
    while inp_list[mid+1] == inp_list[mid]:
        mid = lo + (hi - lo) // 2
        lo = mid
        hi = mid - 1
    return mid


def search_occurrence(inp_list, element, hi, low):
    first = last = 0
    while low <= hi:
        mid = low + (hi - low) // 2
        if inp_list[mid] == element:
            first = get_left(inp_list,low,mid)
            print(first)
            last = get_last(inp_list,hi,mid)
            break
        elif inp_list[mid] < element:
            low = mid + 1
        else:
            hi = mid - 1
    print("First and last occurrence of the element is at :"+str(first)+" and "+str(last)+" positions")


l = [1, 1, 2, 3, 3, 3, 3, 3, 4, 5]
e = 3

search_occurrence(l, e, len(l) - 1, 0)
