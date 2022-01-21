import os
with open('CodeRepository/Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

# 5
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2

num_grid = int(lines[0])
lines.pop(0)

grid = []
for line in lines:
    lst_temp = list(line.split())
    lst_temp = [int(item) for item in lst_temp]
    lst_temp.append(0)
    lst_temp.insert(0, 0)
    grid.append(lst_temp)
grid.append([0] * (num_grid + 2))
grid.insert(0, [0] * (num_grid + 2))
print(grid)

num_grid += 2
cnt_local_minima = 0
for i in range(1, num_grid-1):
    for j in range(1, num_grid-1):
        condition1 = grid[i][j] > grid[i][j-1]
        condition2 = grid[i][j] > grid[i-1][j]
        condition3 = grid[i][j] > grid[i][j+1]
        condition4 = grid[i][j] > grid[i+1][j]

        if condition1 & condition2 & condition3 & condition4 == True:
            cnt_local_minima += 1

print(cnt_local_minima)