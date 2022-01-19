

def vowel_count(string) : 
    count_vowel = 0
    
    for char in string :
        if char in 'aeiou' :
            count_vowel += 1
    
    return count_vowel

def main() :
    while 1 == 1 :
        input_string = input("Input string is : ")

        if (input_string == '-1') : 
            break
        else :
            print(vowel_count(input_string), 'vowels in', input_string)


if __name__ == '__main__':
    main()
