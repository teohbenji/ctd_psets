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
    funcOfx = x ** 2 + 5 * x - 4
    print("The value of f(x) is",funcOfx)

#Calculates value of geometric series
def pset_103():
    a = int(input("Enter the value of a: "))
    r = 1
    n = 1 
    sum = a + r + n
    print("The sum is",sum)


# def pset_104():


# def pset_105():


# def pset_106():


# def pset_107():


# def pset_108():


# def pset_109():


# def pset_110():


# def pset_111():


# def pset_112():


# def pset_113():

#Save functions as dict values
#https://stackoverflow.com/questions/9205081/is-there-a-way-to-store-a-function-in-a-list-or-dictionary-so-that-when-the-inde
pset_dict = {
    "101": pset_101,
    "102": pset_102,
    "103": pset_103
    # "104": pset_104,
    # "105": pset_105,
    # "106": pset_106,
    # "107": pset_107,
    # "108": pset_108,
    # "109": pset_109,
    # "110": pset_110,
    # "111": pset_111,
    # "112": pset_112,
    # "113": pset_113,
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
    # "113": test_113,
}

#User can choose the specific function to run
#https://stackoverflow.com/questions/9205081/is-there-a-way-to-store-a-function-in-a-list-or-dictionary-so-that-when-the-inde
def run_pset():
    num = input("Which pset do you want to run?: ")
    if (True):
        print("Running pset",num,"...\n...\n...")
        pset_dict[num]()
    else:
        print("Invalid pset number entered.")

#User can choose the specific function to test
def test_pset():
    num = input("Which pset do you want to test?: ")
    if (True):
        print("Testing pset",num,"...\n...\n...")
        print("Pset",num,"Test results:")
        test_101()
        #test_dict[num]()
    else:
        print("Invalid pset number entered.")

def run_program():
    choice = input("Enter run to manually test a pset.\nEnter test to automatically test a pset.\nSelection: ")
    if (choice == "run"):
        run_pset()
    elif (choice =="test"):
        test_pset()
    else: 
        print("Invalid input. Please try again.")
        run_program()    

run_program()