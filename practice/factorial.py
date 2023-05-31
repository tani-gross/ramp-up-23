def factorial_iterative(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    
    return total

def factorial_recursive(num):
    if num == 0:
        return 1
    
    return num * factorial_recursive(num - 1)

def factorial(num):
    first = factorial_iterative(num)
    second = factorial_recursive(num)

    if (first == second):
        print(f"Factorial: {first}")
    else:
        print("Something went wrong, oops")\
    
factorial(2)