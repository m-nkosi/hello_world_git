print("Calculator")

def add(num1: float, num2: float) -> float:
    """adds to numbers"""
    return num1 + num2

def substract(num1: float, num2: float) -> float:
    """substract num2 from num1"""
    return num1 - num2

type_of_calculation = input("what type  of  calculations do you want to do: ")
calculations = {
    "add": add,
    "substract": substract
}

if type_of_calculation in calculations.keys():
    num1 = input("Enter num1: ")
    num2 = input("Enter num2: ")
    try:
        print(calculations[type_of_calculation](float(num1), float(num2)))
    except ValueError:
        print("enter a decimals, integers only")
else:
    print("we dont currently offer that type of calculation")