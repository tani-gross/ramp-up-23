def uncensor(str, left_out):
    return_str = ""
    count_used = 0
    for char in str:
        if(char == "*"):
            return_str += left_out[count_used]
            count_used += 1
        else:
            return_str += char
    
    return return_str