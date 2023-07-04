print("Calculator")
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
try:
    print(f"Total is {float(num1)+ float(num2)}")
except ValueError:
    print("enter a decimals, integers only")
