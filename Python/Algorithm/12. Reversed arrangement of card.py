import os

with open('CodeRepository/Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()
    lst_input = []
    for line in lines:
        start, end = map(int, line.split())
        lst_input.append((start, end))

###

def num_reverser(lst, start, end):
    lst_duplicate = lst[start-1:end]
    num_sublst = len(lst_duplicate)
    
    for i in range(num_sublst):
        lst[start-1+i] =  lst_duplicate[-1-i]
    
    return lst

###
def main():
    lst_original = [i for i in range(1, 21)]
    lst_reversed = lst_original

    for start, end in lst_input:
        lst_reversed = num_reverser(lst_reversed, start, end)
        print(lst_reversed)

if __name__ == '__main__':
    main()

    




    

