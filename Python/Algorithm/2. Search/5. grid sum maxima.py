import os
with open('CodeRepository/Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

num_grid = int(lines[0])
lines.pop(0)

lst_grid = []
for line in lines:
    lst_grid.append(list(map(int, line.split())))

#print(lst_grid)
# print(num_grid)
# print(type(num_grid))

maxima = float('-inf')

for i in range(num_grid):
    vert_sum = 0
    hori_sum = 0
    
    for j in range(num_grid):
        vert_sum += lst_grid[i][j]
        hori_sum += lst_grid[j][i]
    
    if vert_sum > maxima:
        maxima = vert_sum
    elif hori_sum > maxima:
        maxima = hori_sum


for i in range(num_grid):
    left_diagonal = 0
    right_diagonal = 0

    for j in range(num_grid):
        if i == j:
            left_diagonal += lst_grid[i][j]
        elif i+j-1 == num_grid:
            right_diagonal += lst_grid[i][j]

    if left_diagonal > maxima:
        maxima = left_diagonal
    elif right_diagonal > maxima:
        maxima = right_diagonal

print(maxima)    
