def get_average_sublist(ls, n): 
    #Executes code if index exists. Otherwise, return None
    if(n < len(ls)):
        sum = 0

        for i in range(len(ls[n])):
            sum = sum + ls[n][i]

        average = round(sum / len(ls[n]), 1)
    
    else:
        return None

    return average

def has_list(ls):

    for x in ls:
        isList = isinstance(x, list)

        if(isList):
            return True
    
    return False

def max_list(inlist):
    out = []

    # If first element is not list, do not iterate
    isList = isinstance(inlist[0], list)
    
    if(not isList):
        out.append(max(inlist))
    else:
        for nested_list in inlist:
            out.append(max(nested_list))

    return out

def find_average_of_list(ls):
    return sum(ls) / len(ls)

def find_average_of_lists(ls):
    averages = []
    element_count = 0
    element_sum = 0

    # If first element is not list, do not iterate
    isList = isinstance(ls[0], list)

    if(not isList):
        rounded_average = round(find_average_of_list(ls), 2)
        averages.append(rounded_average)

        return averages, rounded_average
    
    for nested_list in ls:
        averages.append(round(find_average_of_list(nested_list), 2))
        element_sum = element_sum + sum(nested_list) 
        element_count = element_count + len(nested_list)

    average = round(element_sum / element_count, 2)

    return averages, average

    