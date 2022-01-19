
def max_abs_val(lst):
    max_value = -1
    temp_value = -1

    for item in lst:
        temp_value = abs(item)
        if(temp_value > max_value):
            max_value = temp_value
    
    return max_value