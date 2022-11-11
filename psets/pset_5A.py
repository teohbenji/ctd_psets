import math

#Creates a dictionary with elements in fruits as keys
#and corresponding prices as values
def create_dictionary(fruits, prices):
    dict = {}

    # Returns none if lists are of diffrent length
    if (len(fruits) != len(prices)):
        return None
    else:
        #Creates a new dictionary object
        #Key: fruit, value:price
        for i in range(len(fruits)):
            dict[fruits[i]] = prices[i]
    
    return dict

def get_value(dd,key):
    return dd.get(key)

def extract_data(dd,key):
    if(key not in dd):    
        return None
    else:
        (x, y) = dd[key]

        distance = math.sqrt(x**2 + y**2)

        return round(distance, 2)

def get_base_counts(dna):
    dd = {"A": 0, "C": 0, "G": 0, "T": 0}

    for c in dna:
        if(c not in dd):
            return "The input DNA string is invalid"
        else:
            dd[c] = dd[c] + 1
    
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
    pass

