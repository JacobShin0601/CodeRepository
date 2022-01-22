import os
with open('CodeRepository/Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

# 1 4 3 6 2 8 5 7 9
# 5 7 2 1 3 9 4 6 8
# 9 8 6 7 5 4 2 3 1
# 3 9 1 5 4 2 7 8 6
# 4 6 8 9 1 7 3 5 2
# 7 2 5 8 6 3 9 1 4
# 2 3 7 4 8 1 6 9 5
# 6 1 9 2 7 5 8 4 3
# 8 5 4 3 9 6 1 2 7

sudoku = [list(map(int, line.split())) for line in lines]

def check_row(sudoku):
    bool = True
    for i in range(len(sudoku)):
        dict_check = {}
        for j in range(len(sudoku)):
            if sudoku[i][j] not in dict_check.keys():
                dict_check[sudoku[i][j]] = 1
            else:
                dict_check[sudoku[i][j]] += 1
        #print(dict_check)
        #print(dict_check.values())
       
        for value in dict_check.values():
            if value != 1:
                bool = False
                break
    return bool

def check_column(sudoku):
    bool = True
    for i in range(len(sudoku)):
        dict_check = {}
        for j in range(len(sudoku)):
            if sudoku[j][i] not in dict_check.keys():
                dict_check[sudoku[j][i]] = 1
            else:
                dict_check[sudoku[j][i]] += 1
        #print(dict_check)
        #print(dict_check.values())
       
        for value in dict_check.values():
            if value != 1:
                bool = False
                break
    return bool

def check_box(sudoku):
    bool = True
    for i in range(0, len(sudoku), 3):
        for j in range(0, len(sudoku), 3):
            dict_check = {}
            for m in range(3):
                for n in range(3):
                    if sudoku[i+m][j+n] not in dict_check.keys():
                        dict_check[sudoku[i+m][j+n]] = 1
                    else:
                        dict_check[sudoku[i+m][j+n]] += 1
        
            for value in dict_check.values():
                if value != 1:
                    bool = False
                    break
    return bool

if check_row(sudoku) & check_column(sudoku) & check_box(sudoku):
    print("Yes")
else:
    print("No")

        