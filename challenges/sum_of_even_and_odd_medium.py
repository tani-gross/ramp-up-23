def sum_odd_and_even(lst):
    even_sum = 0
    odd_sum = 0

    for num in lst:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    
    return [even_sum, odd_sum]

print(sum_odd_and_even([2,3,4,5,6,12,4,5]))