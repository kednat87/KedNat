# Problem Statement
# https://www.geeksforgeeks.org/reverse-words-in-a-given-string/

s = 'getting good at coding needs a lot of practice'


def reverse_words(s):
    l = s.split()
    new_list = []
    for i in range(len(l)-1,-1,-1):
        new_list.append(l[i])
    return ' '.join(new_list)


print(reverse_words(s))
