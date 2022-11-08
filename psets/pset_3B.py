def median(ls):
    ls.sort()
    length_of_list = len(ls)
    
    #Different method of finding median depending on list length
    if (length_of_list % 2 == 1):
        index_of_median = int((length_of_list - 1) / 2)
        return ls[index_of_median]
    else:
        index_right_of_median = int(length_of_list / 2)
        index_left_of_median = int((length_of_list / 2) - 1)
        return (ls[index_left_of_median] + ls[index_right_of_median]) / 2
    
def middle_list(ls):
    ls.pop(0)
    ls.pop(-1)
    return ls

def swap_elements(ls, index1, index2):
    length_of_list = len(ls)
    
    #Invalid if index 1 and 2 > max_index, or index 1 and 2 < 0
    if (index1 >= length_of_list or index2 >= length_of_list or index1 < -length_of_list or index2 < -length_of_list):
        return None
    else:
        new_ls = ls.copy()
        new_ls[index1] = ls[index2]
        new_ls[index2] = ls[index1]
        return new_ls

#Returns sum of positive odd nubmers in the list
def sum_odd_numbers(ls):
    sum = 0

    for num in ls:
        if (num > 0 and num % 2 == 1):
            sum += num
    
    return sum

#Returns Collatz conjecture
def hailstone(n):
    list = [n]

    while(n > 1):
        if (n % 2 == 0):
            n = int(n / 2)
        else:
            n = int(3 * n + 1)

        list.append(n)
    return list

def get_odd_numbers(ls):
    list = []
    
    for num in ls:
        if (num % 2 == 1):
            list.append(num)
    
    return sorted(list)

def moving_average(ls):
    moving_averages = []
    
    for i in range(0, len(ls) - 2):
        moving_average = round(sum(ls[i: i + 3]) / 3, 1) 
        moving_averages.append(moving_average)

    return moving_averages

def trapezoidal_rule(f, dx):
    if (len(f) <= 1):
        return 0
    else: 
        sum = f[0] + f[-1]  
        f.pop(0)
        f.pop(-1)

        for y in f:
            sum += 2 * y

        area = 0.5 * dx * sum
    
        return area

def left_riemann_sum(x, y):
    #Invalid input: x or y has 1 element or less
    if (len(x) <= 1 or len(y) <= 1):
        return 0
    else:
        sum = 0
        #Formula is y * change in x
        for i in range(0, len(x) - 1):
            sum += y[i] * (x[i + 1] - x[i])
        return sum
