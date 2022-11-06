import math

def sequence(n):
    if (n < -0.5 and n >= -3):
        return None
    else:
        sequence = round(math.sqrt((2 * n + 1) / (n + 3)), 4)
        return sequence

#Returns True if x > n1 and n2, and x < n3
#Else False
def check_value (n1, n2, n3, x):
    return x > n1 and x > n2 and x < n3
        
