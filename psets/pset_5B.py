def increase_value(sample_dict, key):
    if (key in sample_dict):
        sample_dict[key] += 1
    
    return sample_dict

def translate_point(dd,key,vector):
    if(key in dd):
        (old_x, old_y) = dd[key]
        (translate_x, translate_y) = vector
        dd[key] = (old_x + translate_x, old_y + translate_y)

    return dd

#Same as translate_point, but returns a modified copy of dd
def translate_point_new(dd,key,vector):
    dd_out = dd.copy()

    if(key in dd_out):
        (old_x, old_y) = dd_out[key]
        (translate_x, translate_y) = vector
        dd_out[key] = (old_x + translate_x, old_y + translate_y)

    return dd_out

def replace_values(ls, value1, value2):
    for i in range(len(ls)):
        if(ls[i] == value1):
            ls[i] = value2

    return ls 

#Same as replace_values, but returns a modified copy of ls
def replace_values_new(ls, value1, value2):
    ls_out = ls.copy()

    for i in range(len(ls_out)):
        if(ls_out[i] == value1):
            ls_out[i] = value2

    return ls_out 

#Returns a: change in x, b: change in y
#c: point 1 x * change in y - point 1 y * change in x 
def equation_of_line(point1, point2):
    (p1_x, p1_y) = (point1) 
    (p2_x, p2_y) = (point2) 
    
    a = p2_x - p1_x
    b = -(p2_y - p1_y)
    c = p1_x *(-b) - p1_y * a

    return a, b, c

def reflect(point, eqn):
    (a, b, c) = eqn
    (p, q) = point

    common_denominator = a ** 2 + b ** 2
    reflected_p = (p * (a ** 2 - b ** 2) - 2 * b * (a * q + c) ) / common_denominator
    reflected_q = (q * (b ** 2 - a ** 2) - 2 * a * (b * p + c) ) / common_denominator

    return reflected_p, reflected_q 

def reflect_triangle(dd, point):
    dd_out = dd.copy()

    #Assign coordinates of point
    (pt_x, pt_y) = dd[point]
    del dd[point]

    #Get eqn of line from remaining two points
    eqn_of_line = equation_of_line(list(dd.values())[0], list(dd.values())[1])
    
    #Update value of point with reflected coordinates
    dd_out[point] = reflect((pt_x, pt_y), eqn_of_line)

    return dd_out

