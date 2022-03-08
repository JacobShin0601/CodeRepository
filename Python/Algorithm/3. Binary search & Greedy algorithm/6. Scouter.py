import os

from numpy import left_shift
with open('Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()
    
# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60

num_athle = int(lines[0])
lines.pop(0)

lst_tuples = []

for item in lines: 
    key, value = map(int, item.split())
    lst_tuples.append((key, value))
    
print(lst_tuples)
num_optimal = 0

for i in range(len(lst_tuples)):
    optimal_tuple = lst_tuples[i]
    flag_break = False
   # print(optimal_tuple)
    
    for j in range(i+1, len(lst_tuples)):
        #print(lst_tuples[j])
        #print(lst_tuples[j][0], lst_tuples[j][1])
        
        if (lst_tuples[j][0]>optimal_tuple[0]) & (lst_tuples[j][1]>optimal_tuple[1]):
            flag_break = True
    
    if(flag_break == False):
        num_optimal += 1
    
print(num_optimal)
    

