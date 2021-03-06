import os 
with open('Python/Algorithm/input.txt') as obj_file:
    lines = obj_file.readlines()

# 9 3
# 1 2 3 4 5 6 7 8 9

num_songs, num_dvd = map(int, lines[0].split())
lines.pop(0)

lst_min_songs = [int(item) for item in list(lines[0].split())]

left_pnt = 0
right_pnt = sum(lst_min_songs) - 1

while(left_pnt < right_pnt):
    mid_pnt = (left_pnt + right_pnt) // 2

    min_available = mid_pnt

    cnt_dvd = 1
    temp_sum = 0
    for min_song in lst_min_songs:
        if temp_sum + min_song > min_available:
            cnt_dvd += 1
            temp_sum = min_song
        elif temp_sum + min_song < min_available:
            temp_sum += min_song
    
    if cnt_dvd <= num_dvd:
        right_pnt = mid_pnt - 1
        #print("Right:")
        #print(right_pnt)
    elif cnt_dvd > num_dvd:
        left_pnt = mid_pnt + 1
        #print("Left:")
        #print(left_pnt)
        

print(mid_pnt)
