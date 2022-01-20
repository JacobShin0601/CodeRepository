import os

# 3
# 1 3 5
# 5
# 2 3 6 7 9

with open('CodeRepository/Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

num_lst1 = lines[0]
lst1 = list(lines[1].split())
num_lst2 = lines[2]
lst2 = list(lines[3].split())

lst_merged = lst1 + lst2
lst_merged_sorted = sorted(lst_merged)
print(lst_merged_sorted)


