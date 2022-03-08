import os

from numpy import left_shift, sort
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

sorted_lst_tuples = sorted(lst_tuples, reverse=1, key=lambda x: x[0])  
print(sorted_lst_tuples)
lst_optimal = []
lst_optimal.append(sorted_lst_tuples[0])
#optimal_tuple = sorted_lst_tuples[0]

for i in range(1, len(sorted_lst_tuples)):
    optimal_tuple = sorted_lst_tuples[0]
    #flag_break = False
    # print(optimal_tuple)
    
        
    if (sorted_lst_tuples[i][1] > optimal_tuple[1]):
        optimal_tuple = sorted_lst_tuples[i]

        for j in range(1, len(sorted_lst_tuples)):
            if(sorted_lst_tuples[j][0] > optimal_tuple[0]) and (sorted_lst_tuples[j][1] > optimal_tuple[1]):
                optimal_tuple = sorted_lst_tuples[j]
        #num_optimal += 1
        #flag_break = True
        #optimal_tuple = sorted_lst_tuples[i]
        lst_optimal.append(optimal_tuple)
    
    # if(flag_break == True):
    #     #num_optimal += 1
    #     lst_optimal.append(optimal_tuple)
    
uni_lst_optimal = list(set(lst_optimal))
print(uni_lst_optimal)
    

