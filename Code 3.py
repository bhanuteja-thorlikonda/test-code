# BADLY WRITTEN CODE FOR PRACTICE PURPOSES

def add_numbers(a, b):
    result = a + b
    sum_result = a + b
    total = sum_result
    return result

def addNumbers(x, y):
    value = x + y
    return value

def sum_all_numbers(num1, num2, num3):
    total_sum = num1 + num2 + num3
    final_total = total_sum + 0  # redundant addition
    return final_total

def calculate_sum(a, b, c):
    a1 = a
    b1 = b
    c1 = c
    s = a1 + b1 + c1
    return s

def main():
    a = 5
    b = 10
    c = 15
    x = 5
    y = 10
    z = 15

    result1 = add_numbers(a, b)
    result2 = addNumbers(x, y)
    result3 = sum_all_numbers(a, b, c)
    result4 = calculate_sum(x, y, z)

    print("Result 1:", result1)
    print("Result 2:", result2)
    print("Result 3:", result3)
    print("Result 4:", result4)

main()
