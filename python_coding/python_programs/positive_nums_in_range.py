# Problem statement
# https://www.geeksforgeeks.org/python-program-to-print-all-positive-numbers-in-a-range/

start = -200
end = 12

# looping just selecting from 0

if start < 0:
    if end > 0:
        start = 0
    if end < 0:
        print('No positive elements')
    if end == 0:
        print(0)

l = []

# normal loop using range of start and end
for i in range(start,end+1):
    if i>0:
        l.append(i)

print(l)