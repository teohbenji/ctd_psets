#Calculates BMI given weight and height
def pset_101():
    weight = float(input('What is your weight in kg?'))
    height = float(input('What is your height in m?'))
   
    bmi = weight/(height*height)
    
    print('Your BMI is', round(bmi,2))
    
    if (bmi < 18 or bmi > 25):
        print("Good nutrition is important")
    else:
        print("Congratulations, Don't forget to exercise regularly")

def test_101():
    print("Demo of test cases:")
    print("Test case 1: Success")
    print("Test case 2: Failure")
    print("Test case 3: Success")

#Calculates value of f(x) = x^2 + 5x - 4
def pset_102():
    x = int(input("Enter the value of x: "))
    
    func_of_x = x ** 2 + 5 * x - 4
    
    print("The value of f(x) is",func_of_x)

#Calculates value of geometric series
def pset_103():
    a = 1.5
    r = 3
    n = 5
    
    numerator = a * (1 - r ** n)
    denominator = 1 - r
    
    result = numerator/denominator
    
    print("The sum is",result)

#Display an address in Singapore format
def pset_104():
    addressee = "Singapore Post Pte Ltd"
    house_number = "10"
    road_name = "Eunos Road 8"
    unit_number = "# 05-33"
    building_name = "Singapore Post Centre"
    postal_code = "408600"

    first_line = addressee
    second_line = house_number + " " + road_name
    third_line = unit_number + " " + building_name
    fourth_line = "Singapore " + postal_code
    
    print(first_line,second_line,third_line,fourth_line, sep='\n')

#Calculates interest tax, 5% payable on additional income above 20000
def pset_105():
    income = 19000
    
    if(income > 20000):
        tax = round(0.05 * (income - 20000),2)
        print("The tax payable on an income of",income,"is",tax,"dollars.")
    else:
        print("No tax payable.")

def pset_106():
    for i in range(5):
        x = 1 + 2 * i
        print("green bottle",x)

#Display every term of a sequence
def pset_107():
    number_of_terms = 10
    for n in range(number_of_terms):
        numerator = n ** 3 + 3 * n + 5
        denominator = n ** 2 + 1

        result = numerator / denominator
        
        print("n =",str(n) + ":",round(result,3))

#Calculate sum using for loop 
def pset_108():
    n = 10
    total = 0  # see note below
    for i in range(n):
        total += i + 1

    print("The sum is",total)

#Sum up terms of pset_107
def pset_109():
    number_of_terms = 10
    total = 0
    
    for n in range(number_of_terms):
        numerator = n ** 3 + 3 * n + 5
        denominator = n ** 2 + 1
        
        total += numerator / denominator

    print("The sum is",total)

#Swap variable values
def pset_110():
    a = 10
    b = "apple"

    new_a = b
    new_b = a
    a = new_a
    b = new_b

    print(a,b) 

#Outputs different strings based on bmi calculation.
def pset_111():
    height = 1.70
    weight = 69.0
   
    bmi = weight/(height*height)

    if(bmi >= 27.5):
        print("High Risk")
    elif(bmi >=23.0):
        print("Moderate Risk")
    else:
        print("Low Risk")       

#Draw polygon of n sides using turtle.
#Set line thickness and color
#Fills polygon with color 
def pset_112():
    import turtle  

    t = turtle.Turtle()
    # Inputs 
    n_sides = 5
    length = 72
    angle = 360 / n_sides

    # Process 
    width = 4
    color = "red"
    t.width(10)
    t.pencolor(color)
    for i in range(n_sides):
        t.forward(length)   
        t.right(angle)

    # Output
    turtle.done() 


# def pset_113():

#Save functions as dict values
#https://stackoverflow.com/questions/9205081/is-there-a-way-to-store-a-function-in-a-list-or-dictionary-so-that-when-the-inde
pset_dict = {
    "101": pset_101,
    "102": pset_102,
    "103": pset_103,
    "104": pset_104,
    "105": pset_105,
    "106": pset_106,
    "107": pset_107,
    "108": pset_108,
    "109": pset_109,
    "110": pset_110,
    "111": pset_111,
    "112": pset_112
}

test_dict = {
    "101": test_101
    # "102": test_102,
    # "103": test_103,
    # "104": test_104,
    # "105": test_105,
    # "106": test_106,
    # "107": test_107,
    # "108": test_108,
    # "109": test_109,
    # "110": test_110,
    # "111": test_111,
    # "112": test_112,
}

#User can choose the specific function to run
#https://stackoverflow.com/questions/9205081/is-there-a-way-to-store-a-function-in-a-list-or-dictionary-so-that-when-the-inde
def run_pset():
    num = input("Which pset do you want to run?: ")
    if(True):
        print("Running pset",num,"...\n...\n...")
        pset_dict[num]()
    else:
        print("Invalid pset number entered.")

#User can choose the specific function to test
def test_pset():
    num = input("Which pset do you want to test?: ")
    if(True):
        print("Testing pset",num,"...\n...\n...")
        print("Pset",num,"Test results:")
        test_101()
        #test_dict[num]()
    else:
        print("Invalid pset number entered.")

def run_program():
    choice = input("\nEnter run to manually test a pset.\nEnter test to automatically test a pset.\nSelection: ")
    if (choice == "run"):
        run_pset()
    elif (choice == "test"):
        test_pset()
    else: 
        print("Invalid input. Please try again.")
        run_program()    
    
run_program()