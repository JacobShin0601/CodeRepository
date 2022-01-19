

input_string = str(input("Enter an odd length string: "))

len_of_string = len(input_string)
half_index = int(len_of_string/2)


print("Middle character:", input_string[half_index])
print("First half:", input_string[:half_index])
print("Second half:", input_string[half_index+1:])



# Sample output: 
# Enter an odd length string: Fortune favors the bold
# Middle character: o
# First half: Fortune fav
# Second half: rs the bold