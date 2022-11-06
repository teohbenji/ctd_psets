import math

def calculate_sum_odd(n):
    sum = 0 
    
    for i in range(1, n, 2):
        sum += i

    return sum

def alternating(n):
    sum = 0

    for k in range(1, n + 1):
        sum += pow(-1, k + 1) / k

    return sum

def compound_interest(principal, rate, months):
    monthly_rate = rate / 12

    for i in range(0, months):
        principal *= (1 + monthly_rate)

    return round(principal, 2)

def regular_savings(deposit, rate, months):
    monthly_rate = rate / 12
    sum = 0

    for i in range(0, months):
        sum = (sum + deposit) * (1 + monthly_rate)

    return round(sum, 2)

def sum_of_series(n):
    sum = 0

    for i in range(1, n + 1):
        sum += 1 / pow(i, 2)

    return sum

def fraction_of_pisq(s):
    pisq = pow(math.pi, 2)
    result = s / (pisq / 6)
    
    return result
    
def terms_required(p):
    n = 0
    frac = 0

    while (frac < p):
        n += 1
        sum = sum_of_series(n)
        frac = fraction_of_pisq(sum)

    return n

def is_prime(n):
    for i in range (2, n-1):
        if(n % i == 0):
            return False

    return True

#Same logic as calculate_sum_odd, but using a while loop instead of a for loop
def calculate_sum_even(n):
    total = 0
    i = 0

    while (i < n):
        if (i % 2 == 0):
            total += i

        i += 1

    return total

def alternating_while(stop):
    total = 0
    n = 1
    term = 1

    while abs(term) > stop:
        total += term
        n += 1
        term = pow(-1, n + 1) / n
    
    return total
