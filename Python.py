def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def get_list_item(lst, index):
    if index < 0 or index >= len(lst):
        return "Index out of range"
    return lst[index]

def calculate_total(price, tax):
    price = float(price)
    tax = float(tax)
    total = price + tax
    return total

# Test cases
print(divide_numbers(10, 2))          # Output: 5.0
print(get_list_item([1, 2, 3], 1))    # Output: 2
print(calculate_total(100, 10))       # Output: 110.0
