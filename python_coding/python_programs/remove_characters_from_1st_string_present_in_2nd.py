# Problem Statement
# https://www.geeksforgeeks.org/remove-characters-from-the-first-string-which-are-present-in-the-second-string/

str1 = 'geeksforgeeks'
str2 = 'masks'

# Method 1 : using strings to replace
def remove_charaters(a,b):
    for i in b:
        if i in a:
            a = a.replace(i,'')
    return a

print(remove_charaters(str1,str2))


# Method 2 : Using List and sets

def remove_chars(a,b):
    # converted the string int set to remove duplicates
    bb = set(b)
    # converted string to list
    aa = list(a)
    i = 0
    while i < len(aa):
        # pops the char from the position i when found.
        # Increments i only when not found. Reason is after pop the characters in list is shifted
        # and hence no need t increment
        if aa[i] in bb:
            aa.pop(i)
        else:
            i +=1
    return ''.join(aa)


print(remove_chars(str1,str2))
