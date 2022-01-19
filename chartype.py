

input_string = str(input("Enter a character: "))

if(input_string.isalnum() == False) :
    print(input_string, "is a non-alphanumeric character.")
elif(input_string.isdigit() == True) :
    print(input_string, "is a digit.")
elif(input_string.islower() == True) :
    print(input_string, "is a lower case letter.")  
elif(input_string.isupper() == True) :
    print(input_string, "is an upper case letter.")      


# Write a program that  reads a character (string of  length  1)  from  the 
# user, and classifies it to  one of the following: lower case letter, upper case letter, 
# digit,  or non-alphanumeric character 

# Sample  output (4 different executions):  
# Enter a character: j
# j is  a lower case  letter.
# Enter a character: 7
# 7 is  a digit.
# Enter a character: ^
# ^ is  a non-alphanumeric  character.
# Enter a character: C
# C is  an  upper case  letter.