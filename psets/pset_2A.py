import math

#Calculates bmi given a weight(kg) and height (cm)
def calculate_bmi(weight, height):
    height = height / 100

    bmi = round(weight /(height * height), 1)
    
    return bmi

#Calculates position and velocity using the SUVAT formulas    
def position_velocity(vo, t):
    g = 9.81

    position = round(vo * t - 0.5 * g * pow(t, 2), 3)
    velocity = round(vo - g * t, 3)

    return position, velocity

#Calculates displacement using decay formula
def decay(a, t):
    displacement = math.exp(-a * t) * math.cos(a * t)

    return displacement

#Returns description of bmi based on bmi value
def describe_bmi(bmi):
    if(bmi < 18.5):
        return "nutritional deficiency"
    elif(bmi >= 18.5 and bmi < 23):
        return "low risk"
    elif(bmi >= 23 and bmi < 27.5):
        return "moderate risk"
    else:
        return "high risk" 

#Returns true if a number is positive and even
def is_positive_even(n):
    return n % 2 == 0 and n > 0

#Returns a letter grade based on mark received 
def letter_grade(mark):
    if (mark >= 90 and mark <= 100):
        return "A"
    elif (mark >= 80 and mark <= 89):
        return "B"
    elif (mark >= 70 and mark <= 79):
        return "C"
    elif (mark >= 60 and mark <= 69):
        return "D"
    elif (mark >= 0 and mark <= 59):
        return "E"        
    else:
        return None

#Returns None if any negative value is input, or if u and v are larger than s
#Else calculates and returns largest area
def largest_area(s, u, v):
    if (s < 0 or u < 0 or v < 0):
        return None
    elif (s < u or s < v):
        return None
    
    #Length is the greater between v, and the other length s - v 
    if (v >= s - v):
        length = v
    else:
        length = s - v
    
    #Breadth is the greater between u, and the other breadth s - u
    if (u >= s - u):
        breadth = u
    else: 
        breadth = s - u
    
    return length * breadth
        