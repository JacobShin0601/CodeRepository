import os
with open('CodeRepository/Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

# 8 3
# 1 2 1 3 1 1 1 2

num_items, sum_target = map(int, lines[0].split())
items = list(lines[1].split())
cnt_match = 0

for i in range(num_items):
    cum_sum = int(items[i])
    if cum_sum == sum_target:
        cnt_match += 1

    for j in range(i+1, num_items):

        cum_sum += int(items[j])

        if cum_sum > sum_target:
            break
        elif cum_sum == sum_target:
            cnt_match += 1
            break
            

print(cnt_match)
