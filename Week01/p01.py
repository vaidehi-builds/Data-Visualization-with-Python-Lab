"""1. Write a Python function to input two numbers and perform the Calculator operations of (+, -, *, /). """
def calculator():
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    print("Addition: ",num1+num2)
    print("Subtraction: ",num1-num2)
    print("Multiplication: ",num1*num2)
    if num2!=0:
        print("Divison: ",num1/num2)
    else:
        print("Division not possible as denominator is zero!")

calculator()