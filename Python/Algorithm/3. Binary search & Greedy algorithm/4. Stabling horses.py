import os

from numpy import left_shift 
with open('Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

# 5 3
# 1
# 2
# 8
# 4
# 9

num_stabling, num_horses = map(int, lines[0].split())
lines.pop(0)

lst_location = [int(item) for item in lines]
lst_location.sort()
print(lst_location)

left_pnt = 0
right_pnt = len(lst_location)
cnt = 3

while(left_pnt < right_pnt):
    mid_pnt = (left_pnt + right_pnt) // 2

    left_gap = mid_pnt - left_pnt
    right_gap = right_pnt - mid_pnt

    if cnt == num_horses:
        nearest_gap = max(left_gap, right_gap)
        print(nearest_gap)
        break

    if left_gap < right_gap:
        left_pnt = mid_pnt
        cnt += 1
    elif left_gap > right_gap:
        right_pnt = mid_pnt
        cnt += 1
