import os
with open('CodeRepository/Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

num_grid = int(lines[0])
lines.pop(0)

# lst_grid = []
# for i in range(num_grid):
#     lst_temp = list(lines[0].split())
#     lst_temp = [int(item) for item in lst_temp]
#     lst_grid.append(lst_temp)
#     lines.pop(0)
#print(lst_grid)
lst_grid = [list(map(int, line.split())) for line in lines]
for _ in range(num_grid):
    lines.pop(0)
print(lines)

num_rotation = int(lines[0])
lines.pop(0)

lst_rotation = []
for i in range(num_rotation):
    lst_temp = list(lines[0].split())
    lst_temp = [int(item) for item in lst_temp]
    lst_rotation.append(lst_temp)
    lines.pop(0)
#print(lst_rotation)

# 5
# 10 13 10 12 15 
# 12 39 30 23 11 
# 11 25 50 53 15 
# 19 27 29 37 27 
# 19 13 30 13 19

# 3
# 2 0 3
# 5 1 2
# 3 1 4

def grid_rotation(lst_grid, lst_rotation):
    for item_rotation in lst_rotation:
        row_num_of_rotation = item_rotation[0] - 1
        num_rotation = item_rotation[2]

        if item_rotation[1] == 0:
            target_row = lst_grid[row_num_of_rotation]
            lst_rotated = lst_grid[row_num_of_rotation]
            
            for i in range(num_rotation):
                lst_rotated.append(lst_rotated[0])
                lst_rotated.pop(0)
                # lst_rotated[i] = lst_grid[row_num_of_rotation][i-num_rotation]
            #print(lst_rotated)
        elif item_rotation[1] == 1:
            target_row = lst_grid[row_num_of_rotation]
            lst_rotated = lst_grid[row_num_of_rotation]
            
            for i in range(num_rotation):
                lst_rotated.insert(0, lst_rotated[-1])
                lst_rotated.pop()
                #print(lst_rotated)
            #print(lst_rotated)
            #print("\n")
        lst_grid[row_num_of_rotation] = lst_rotated
        #print(lst_grid)
    return lst_grid

def sum_of_grid(lst_grid):
    num_grid = len(lst_grid)
    #print(num_grid)
    hori_pnt = 0
    vert_pnt = num_grid
    half_pnt = num_grid // 2
    sum = 0

    for i in range(num_grid): ### connected with hori
        for j in range(hori_pnt, vert_pnt):
            sum += lst_grid[i][j]
        
        #print(sum)
        if i < half_pnt:
            hori_pnt += 1
            vert_pnt -= 1
        else:
            hori_pnt -= 1
            vert_pnt += 1

    return sum



grid_rotated = grid_rotation(lst_grid, lst_rotation)
print(grid_rotated)
print(sum_of_grid(grid_rotated))




