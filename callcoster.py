
day_input = str(input("Enter the day the call started at: "))
time_input = str(input("Enter the time the call started at (hhmm): "))
duration_input = int(input("Enter the duration of the call (in minutes): "))

day_input = day_input.lower()
total_cost = 0.00
time_input_hour = time_input[0:2]
time_input_hour = int (time_input_hour)

if (day_input == "sat" or day_input == "sun"):
    total_cost = duration_input * 0.15
elif (8 <= time_input_hour <= 17):
    total_cost = duration_input * 0.40
else :
    total_cost = duration_input * 0.25

print("This call will cost $%2.2f" %total_cost)


# Enter the day the call started at: Fri
# Enter the time the call started at (hhmm): 2350
# Enter the duration of the call (in minutes): 22
# This call will cost $5.50