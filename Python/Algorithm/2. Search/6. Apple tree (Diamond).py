import os
with open('CodeRepository/Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

# 5
# 10 13 10 12 15 
# 12 39 30 23 11 
# 11 25 50 53 15 
# 19 27 29 37 27 
# 19 13 30 13 19

num_grid = int(lines[0])
lines.pop(0)

lst_grid = []
for line in lines:
    lst_temp = list(line.split())
    lst_temp = [int(item) for item in lst_temp]
    lst_grid.append(list(lst_temp))

print(lst_grid)
'''
(0,2)
(1,1), (1,2), (1,3)
(2,0), (2,1), (2,2), (2,3), (2,4)
(3,1), (3,2), (3,3)
(4,2)
'''

hori_pnt = num_grid//2
vert_pnt = num_grid//2 


apple_sum = 0
for i in range(num_grid):
    for j in range(hori_pnt, vert_pnt+1):
        apple_sum += lst_grid[i][j]

    if i < num_grid//2:
        hori_pnt -= 1
        vert_pnt += 1
    else:
        hori_pnt += 1
        vert_pnt -= 1

print(apple_sum)
