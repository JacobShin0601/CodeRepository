import os
from tempfile import tempdir
with open('CodeRepository/Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

# 8 32
# 23 87 65 12 57 32 99 81

num_input, target_input = map(int, lines[0].split())
lst_nums = [int(item) for item in list(lines[1].split())]

#print(num_input, target_input)
#print(lst_nums)
#print('\n')

def bubble_sort(lst):
    num_input = len(lst)

    for i in range(num_input-1):
        for j in range(i+1, num_input):
            if lst[i] > lst[j]:
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
            #print(lst)
    return lst

def binary_search(lst, target_input):
    num_input = len(lst)
    left_pnt = 0
    right_pnt = num_input
    
    while(True):
        mid_pnt = (left_pnt + right_pnt) // 2

        if lst[mid_pnt] == target_input:
            print(mid_pnt+1)
            break
        elif lst[mid_pnt] > target_input:
            right_pnt = mid_pnt - 1
        else:
            left_pnt = mid_pnt + 1



sorted_lst_nums = bubble_sort(lst_nums)
binary_search(lst_nums, target_input)



