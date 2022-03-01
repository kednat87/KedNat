# Problem Statement
# https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/

s1 = 'LISTEN'
s2 = 'SILENT'


def anagrams(a,b):
    for i in a:
        if a.count(i) == b.count(i):
            a.replace(i,'')
            b.replace(i,'')
        else:
            return 'Not Anagrams'
    return 'Anagrams'


print(anagrams(s1,s2))