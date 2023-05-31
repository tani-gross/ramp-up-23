def find_highest(lst):
    if len(lst) == 1:
        return lst[0]
    
    max_of_rest = find_highest(lst[1:])

    if lst[0] > max_of_rest:
        return lst[0]
    else:
        return max_of_rest
    
print(find_highest([1,2,4,5,67,4,32,100]))
