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
    reversed_list = []
    #Access s from the right, using negative indexes
    for i in range(0, len(s)):
        reversed_list.append(s[-(i + 1)]) 

    return ''.join(reversed_list)

#Same function, but using list slicing instead
def reverse_other_method(s):
    return s[::-1]

def is_palindrome(s):
    reversed_string = s[::-1]
    if (s == reversed_string):
        return True
    else:
        return False