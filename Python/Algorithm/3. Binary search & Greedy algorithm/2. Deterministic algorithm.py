import os 
with open('Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

# 4 11
# 802
# 743
# 457 
# 539

num_ethernet_cable, required_num_cable = map(int, lines[0].split())
lines.pop(0)

length_ether = []
for i in range(num_ethernet_cable):
    length_ether.append(int(lines[i]))

left_pnt = 0
right_pnt = 1000

while(left_pnt <= right_pnt):
    mid_pnt = (left_pnt + right_pnt) // 2
    #print(mid_pnt)
    sum_cable_num = 0

    for cable in length_ether:
        sum_cable_num += cable // mid_pnt
    #print(sum_cable_num)

    if sum_cable_num >= required_num_cable:
        left_pnt = mid_pnt + 1
    else:
        right_pnt = mid_pnt - 1
print(mid_pnt)
### Solution, but not deterministic algorithm
# optimal_length = sum(length_ether)//required_num_cable

# sum_of_cable_num = 0
# for _ in range(optimal_length):
    
#     for cable in length_ether:
#         sum_of_cable_num += cable//optimal_length

#     if sum_of_cable_num >= required_num_cable:
#         print(optimal_length)
#         break 
#     else:
#         optimal_length -= 1
#         sum_of_cable_num = 0
