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