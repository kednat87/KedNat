# Problem Statement
# https://www.geeksforgeeks.org/find-the-smallest-window-in-a-string-containing-all-characters-of-another-string/
# Not Solved !!!!

str = 'this is a test string'
pat = 'tist'


def get_pos(s):
    d = {}
    s = list(s)
    for i in range(len(s)):
        if s[i] in d.keys():
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]
    return d

def get_pat_pos()

d = get_pos(str)
temp_d = d.copy()

for i in d.keys():
    if i not in pat:
        temp_d.pop(i)

d = temp_d.copy()

print(d)
