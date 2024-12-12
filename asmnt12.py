
def find_greatest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        greatest = num1
    elif num2 >= num1 and num2 >= num3:
        greatest = num2
    else:
        greatest = num3
    return greatest

# Input numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Finding and displaying the greatest number
greatest = find_greatest(num1, num2, num3)
print(f"The greatest number among {num1}, {num2}, and {num3} is: {greatest}")
