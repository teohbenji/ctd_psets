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

def get_zero_matrix(m, n):
    zero_matrix = []
    for i in range(m):
        zero_matrix.append([0] * n)

    return zero_matrix
            
def transpose_matrix(ls):
    #Transposed rows = No. of columns, or no. of list elements
    #Transposed columns = No. of rows, or no. of elements in each list element
    
    transposed_rows = len(ls[0])
    transposed_columns = len(ls)
    
    transposed_matrix = get_zero_matrix(transposed_rows, transposed_columns)

    for i in range(transposed_rows):
        for j in range(transposed_columns):
            transposed_matrix[i][j] = ls[j][i]
    
    return transposed_matrix

def process_scores(f):
    pass