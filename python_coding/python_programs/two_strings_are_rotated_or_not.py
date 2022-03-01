# Problem Statement
# https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/

s1 = 'ABCD'
s2 = 'CDAB'


def rotated_or_not(a,b):
    l1 = len(a)
    i = 0
    while i <= l1:
        if a == b :
            return 'Rotated String'
        else :
            i += 1
            a = list(a)
            a = a[i+1:]+a[:i+1]
            a = ''.join(a)
    return 'Not a Rotated String'


print(rotated_or_not(s1,s2))
