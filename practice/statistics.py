def calculate_statistics(lst):
    sum = 0
    min = 2147483647
    max = -2147483648
    
    for num in lst:
        sum += num
        if num < min:
            min = num
        
        if num > max:
            max = num
    
    print(f"Minimum: {min}, Maximum: {max}, Sum: {sum}, Average: {sum/len(lst)}")
