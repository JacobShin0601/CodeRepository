

integer_input = int(input("Please enter a positive integer greater than 1: "))

first_item = 0
second_item = 1
count = 1

print("1")

while(integer_input != count):
    print(first_item+second_item)

    tmp = first_item
    first_item = second_item
    second_item = tmp + second_item

    count = count + 1



# Please enter a positive integer greater than 1: 4
# 1
# 1
# 2
# 3