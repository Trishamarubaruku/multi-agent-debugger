Buggy Python Code

def divide_numbers(a, b):
    return a / b

def get_list_item(lst, index):
    return lst[index]

def calculate_total(price, tax):
    total = price + tax
    return total

 Test cases
print(divide_numbers(10, 0))          # Bug 1: Division by zero
print(get_list_item([1, 2, 3], 5))    # Bug 2: Index out of range
print(calculate_total("100", 10))     # Bug 3: Type error
