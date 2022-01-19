import random

def list_of_dice_rolls(n) :
    result_list = []
    for i in range(n) :
        result_list.append(random.randint(1, 6))
    return result_list

def main():
    input_num = int(input("Please input the integer for dice rolling: "))
    result = list_of_dice_rolls(input_num)
    print(result)

main()