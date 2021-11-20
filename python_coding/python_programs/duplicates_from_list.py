# Problem Statement
# https://www.geeksforgeeks.org/python-program-print-duplicates-list-integers/

list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

d = {}
for i in list:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1

for k,v in d.items():
    if v > 1 :
        print('Integer '+str(k)+' is repeating '+str(v)+' times')