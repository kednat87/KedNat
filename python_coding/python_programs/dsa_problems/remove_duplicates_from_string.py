# Problem Statement
# https://www.geeksforgeeks.org/remove-duplicates-from-a-given-string/

str = 'geeksforgeeks'


def remove_dups(s):
    new_string = []
    ns = ''
    for i in s:
        if i in new_string:
            pass
        else:
            # using list
            new_string.append(i)
            # using string
            ns += i
    print(ns)
    return ''.join(new_string)


print(remove_dups(str))