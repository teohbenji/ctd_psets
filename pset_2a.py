import unittest

def calculate_bmi(weight, height):
    height = height / 100

    bmi = round(weight /(height * height), 1)
    
    return bmi

def test_201():
    print(calculate_bmi(2.5, 50))
    print(calculate_bmi(50, 150))
    print(calculate_bmi(43.5, 142.3))

def position_velocity(vo, t):
    pass

def test_202():
    pass

def decay(a, t):
    pass

def test_203():
    pass

def describe_bmi(bmi):
    pass

def test_204():
    pass

def is_positive_even(n):
    pass

def test_205():
    pass

def letter_grade(mark):
    pass

def test_206():
    pass

def largest_area(s, u, v):
    pass

def test_207():
    pass

test_dict = {
    "201": test_201,
    "202": test_202,
    "203": test_203,
    "204": test_204,
    "205": test_205,
    "206": test_206,
    "207": test_207
}

pset_dict = {
    "201": calculate_bmi,
    "202": position_velocity,
    "203": decay,
    "204": describe_bmi,
    "205": is_positive_even,
    "206": letter_grade,
    "207": largest_area
}

#User can choose a specific function to test
def run_program():
    #print out table showing pset numbers and the pset name
    print("Num:    Name:")
    for pset_num in pset_dict:
        print("{:8}{}".format(pset_num, pset_dict[pset_num].__name__))
        pass 
    
    num = input("\nWhich pset do you want to test?: ")
    
    if(num in test_dict):
        print("Running tests for pset {}\n...\n...".format(num))
        print("Pset num test results:".format(num))
        test_dict[num]()
    else:
        print("Invalid pset number entered.")
    
run_program()