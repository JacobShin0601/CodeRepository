import os
with open('CodeRepository/Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

# 2 4 1 5 3 2 6
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5

grid = [list(map(int, line.split())) for line in lines]

def palindrome_check(lst):
    bool = True
    half_pnt = len(lst) // 2

    for i in range(half_pnt):
        if i != half_pnt:
            if lst[i] != lst[-i-1]:
                bool = False
    return bool


def palinedrome_row_cnt(grid):
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid) - 4):

            lst_check = []
            for n in range(j, j + 5):
                lst_check.append(grid[i][n])
            #print(lst_check)
            if palindrome_check(lst_check) == True:
                cnt += 1
    return cnt

def palinedrome_column_cnt(grid):
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid) - 4):

            lst_check = []
            for n in range(j, j + 5):
                lst_check.append(grid[n][i])

            if palindrome_check(lst_check) == True:
                cnt += 1
    return cnt

total_cnt = palinedrome_row_cnt(grid) + palinedrome_column_cnt(grid)
print(total_cnt)
