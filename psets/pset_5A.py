import math

#Creates a dictionary with elements in fruits as keys
#and corresponding prices as values
def create_dictionary(fruits, prices):
    dict = {}

    # Returns none if lists are of diffrent length
    if (len(fruits) == len(prices)):
        #Creates a new dictionary object
        #Key: fruit, value:price
        for i in range(len(fruits)):
            dict[fruits[i]] = prices[i]
    else:
        return None
    return dict

def get_value(dd,key):
    return dd.get(key)

def extract_data(dd,key):
    if(key in dd):    
        (x, y) = dd[key]

        distance = math.sqrt(x**2 + y**2)

        return round(distance, 2)
    else:
        return None

def get_base_counts(dna):
    dd = {"A": 0, "C": 0, "G": 0, "T": 0}

    for c in dna:
        if(c in dd):
            dd[c] = dd[c] + 1
        else:
            return "The input DNA string is invalid"
    
    return dd

def evaluate_polynomial(dd, x):
    y = 0

    for exponent, value in dd.items(): 
        y = y + value * x ** exponent
    
    return round(y, 2)

def diff(pp):
    dp = {}
    
    for key in pp:
        #Derivative of constant is 0, no x value
        if(key != 0):
            dp[key - 1] = key * pp[key]

    return dp

def read_list(ls, reg_no, key):
    for dict in ls:
        #Checks which dict has the reg_no, and whether it has the key
        if(dict['reg'] == reg_no and key in dict):
            return dict[key]
        
    return None

def get_highest_value(dd):
    max_value = max(dd.values())

    for key in dd:
        if(dd[key] == max_value):
            return key, max_value