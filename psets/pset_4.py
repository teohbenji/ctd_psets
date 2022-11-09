def calculate_bmi(weight, height):
    height = height / 100

    bmi = round(weight /(height * height), 1)
    
    return bmi

def describe_bmi(bmi):
    if(bmi < 18.5):
        return "nutritional deficiency"
    elif(bmi >= 18.5 and bmi < 23):
        return "low risk"
    elif(bmi >= 23 and bmi < 27.5):
        return "moderate risk"
    else:
        return "high risk" 

def bmi_information(weight, height):
    bmi = calculate_bmi(weight, height)
    bmi_desc = describe_bmi(bmi)
    return "Your BMI is {} and your category is {}.".format(bmi, bmi_desc)

#Using loop, append reversed list with element from the end of s
def reverse(s):
    reversed_string = ""
    #Access s from the right, using negative indexes
    for i in range(0, len(s)):
        reversed_string = reversed_string + str(s[-(i + 1)]) 

    return reversed_string

#Same function, but using list slicing instead
def reverse_other_method(s):
    return s[::-1]

def is_palindrome(s):
    reversed_string = s[::-1]
    if(s == reversed_string):
        return True
    else:
        return False

#Compares ending with same length of characters from end of word
def match(ending, word):
    return ending == word[-len(ending):]

#Removes non-alphanumeric characters, keeps whitespaces
def clean_string(s):
    cleaned_string = ""

    for char in s:
        if(char == ' ' or char.isalnum()):
            cleaned_string = cleaned_string + str(char)

    return cleaned_string

def digits_in_string(s):
    digit_count = 0

    for char in s:
        if(char.isnumeric()):
            digit_count += 1

    return digit_count

#Check if password has at least 8 characters
#Only alphanumeric
#Need at least 2 numbers
def check_password(pwd):
    is_password_eight = len(pwd) < 8  
    is_password_2d = digits_in_string(pwd) < 2

    if(is_password_eight or is_password_2d):
        return False

    for char in pwd:
        is_password_alnum = char.isalnum()

        if not(is_password_alnum):
            return False
    
    return True

def longest_common_prefix(s1, s2):
    prefix_string = ""

    if(len(s1) < len(s2)):
        shorter_string = s1
    else:
        shorter_string = s2

    #Get indexes where both the characters in both strings have the same value
    for i in range(len(shorter_string)):
        if(s1[i] == s2[i]):
            prefix_string = shorter_string[:i+1]
        else: 
            break

    return prefix_string

def binary_to_decimal(s):
    sum = 0 

    for i in range(len(s)):
        sum += int(s[-(i + 1)]) * (2 ** i)

    return sum

def uncompressed(s):
    uncompressed_str = ""

    for char in s:
        is_numeric = char.isnumeric()
        is_alphabet = char.isalpha()

        if(is_numeric):
            digit = char

        if(is_alphabet):
            for i in range(int(digit)):
                uncompressed_str = uncompressed_str + char
            
    return uncompressed_str

def get_base_counts(dna):
    #A_count, C_count, G_count, T_count
    letter_counts = [0, 0, 0, 0]

    for char in dna:
        if(char == 'A'):
            letter_counts[0] = letter_counts[0] + 1
        elif(char == 'C'):
            letter_counts[1] = letter_counts[1] + 1
        elif(char == 'G'):
            letter_counts[2] = letter_counts[2] + 1
        elif(char == 'T'):
            letter_counts[3] = letter_counts[3] + 1
        else: 
            return []
    
    return letter_counts