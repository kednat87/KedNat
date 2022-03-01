# Problem statement
# if input string is 'aabbbaaaaccc' it should return the output as (5,4) as longest repetitive string is aaaa starting at position 5 and of length 4

def longest_value(d):
    long_k = 'zzz'
    long_v = -1
    for k, v in d.items():
        if int(v[1]) > long_v:
            long_k = k
            long_v = int(v[1])
    return d[long_k]


def longest_string(inp):
    l = list(inp)
    d = {}
    start = 0
    end = 0
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            end += 1
        else:
            if l[i] in d.keys():
                if d[l[i]][1] < end - start + 1:
                    d[l[i]] = (start, end - start + 1)
                    start = i + 1
                    end = i + 1
                else:
                    start = i+1
                    end = i+1
            else:
                d[l[i]] = (start, end - start + 1)
                start = i + 1
                end = i + 1
    d[l[end]] = (start, end - start + 1)
    return longest_value(d)


inp_string = 'aaaaabbbbaaaaccc'

print(longest_string(inp_string))