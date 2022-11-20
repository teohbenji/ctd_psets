import copy

def get_average_sublist(ls, n): 
    #Executes code if index exists. Otherwise, return None
    is_index_in_list = n < len(ls)

    if(is_index_in_list):
        sum = 0

        for i in range(len(ls[n])):
            sum += ls[n][i]
    
    else:
        return None

    average = round(sum / len(ls[n]), 1)

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

#Process scores from scores.txt document
def process_scores(f):
    #Returns list of scores only, without whitespaces
    scores_list = f.read().split()
    sum = 0

    for score in scores_list:
        sum += int(score)
    
    rounded_average = round(sum / len(scores_list), 1)
    
    return sum, rounded_average

def read_fdi(f):
    row_list = f.readlines()
    row_dict = {}

    # Ignore first row which doesn't contain value
    for i in range(1, len(row_list)):
        row = row_list[i].split(",")
        year = row[0]
        value = row[2].replace("\n", "") #Remove newline character from string
        
        row_dict[year] = float(value)

    return row_dict

def gc_content(f):
    bases_to_check = 'CG'
    dna_string = f.read().replace("\n", "")
    gc_occurences = 0

    for char in dna_string:
        #Checks if character is g or c base
        isGCbase = char in bases_to_check
        
        if isGCbase:
            gc_occurences += 1

    gc_percentage = gc_occurences / len(dna_string) * 100

    return round(gc_percentage, 1)
    
def scalar_multiply(ls, scalar):
    """
    Returns the result of matrix multiplication

    Parameters:
        ls (list): A list containing matrix values
        scalar (int): An integer to multiply ls
    
    Returns:
        ls (list): A list containing matrix values that has been multiplied
    """
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            ls[i][j] = ls[i][j] * scalar
    
    return ls

def scalar_multiply_new(ls, scalar):
    """
    Returns a deepcopy of a list that has been multiplied

    Parameters:
        ls (list): A list containing matrix values
        scalar (int): An integer to multiply ls
    
    Returns:
        ls_new (list): A list containing matrix values that has been multiplied
    """
    ls_new = copy.deepcopy(ls)
    
    for i in range(len(ls_new)):
        for j in range(len(ls_new[i])):
            ls_new[i][j] = ls_new[i][j] * scalar
    
    return ls_new

