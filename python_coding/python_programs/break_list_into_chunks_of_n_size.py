# Problem Statement
# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/

my_list = ['geeks', 'for', 'geeks', 'like','geeky','nerdy', 'geek', 'love','questions','words', 'life']
n = 5

start = 0
end = n

result = []

while end <= len(my_list):
    result.append(my_list[start:end])
    start += n
    end += n
    if end > len(my_list):
        result.append(my_list[start:])
print(result)

# just by using Range function to increment
result1 = []
for i in range(0,len(my_list),n):
    result1.append(my_list[i:i+n])

print(result1)
