def pset_101():
    pass

def test_101():
    pass

def pset_102():
    pass

def test_102():
    pass

def pset_103():
    pass

def test_103():
    pass

def pset_104():
    pass

def test_104():
    pass

def pset_105():
    pass

def test_105():
    pass

pset_dict = {
    "101": pset_101,
    "102": pset_102,
    "103": pset_103,
    "104": pset_104,
    "105": pset_105,
}

test_dict = {
    "101": test_101,
    "102": test_102,
    "103": test_103,
    "104": test_104,
    "105": test_105,
}

#User can choose a specific function to run
def run_pset():
    num = input("Which example do you want to run?: ")
    if(num in pset_dict):
        print("Running example",num,"...\n...\n...")
        pset_dict[num]()
    else:
        print("Invalid pset number entered.")
        run_pset()

#User can choose a specific function to test
def test_pset():
    num = input("Which pset do you want to test?: ")
    if(num in test_dict):
        print("Testing pset",num,"...\n...\n...")
        print("Pset",num,"Test results:")
        test_dict[num]()
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