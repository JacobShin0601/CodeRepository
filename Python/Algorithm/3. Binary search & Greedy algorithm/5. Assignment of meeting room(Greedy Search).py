import os

from numpy import left_shift
with open('Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

# 5
# 1 4
# 3 5
# 5 7
# 2 3
# 4 6

num_meeting = int(lines[0])
lines.pop(0)

lst_tuples = []

for item in lines: 
    key, value = map(int, item.split())
    lst_tuples.append((key, value))

# The earlier the meeting finished, the better for arranging meeting 
sorted_lst_tuples = sorted(lst_tuples, key=lambda x: x[1]) 
print(sorted_lst_tuples)

# Applying Greedy Algorithm in terms of 'ending time of meeting'
lst_result_greedy = []
lst_result_greedy.append(sorted_lst_tuples[0]) 
pnt = 0

for i in range(1, len(sorted_lst_tuples)):
    if sorted_lst_tuples[pnt][1] <= sorted_lst_tuples[i][0]:
        lst_result_greedy.append(sorted_lst_tuples[i])
        pnt = i

print(lst_result_greedy)
