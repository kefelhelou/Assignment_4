from math import *

x = int(input("Enter the first number:  "))
print("The app perform the following: \n")
process = input("1: +\n2: -\n3: *\n4: /\n5: ^\n6: %\n enter the operation:")
y = int(input(" Enter the second number: "))
if process == "1" or process == "+":
    result = x + y
    print("The process was addition and the result is: ", result)
if process == "2" or process == "-":
    result = x - y
    print("The process was subtraction and the result is: ", result)
if process == "3" or process == "*":
    result = x * y
    print("The process was multiplication and the result is: ", result)
if process == "4" or process == "/":
    result = x / y
    print("The process was division and the result is: ", result)
if process == "5" or process == "^":
    result = x ** y
    print("The process was power to and the result is: ", result)
if process == "6" or process == "%":
    result = x % y
    print("The process was the mode and the result is: ", result)
process_1 = input("The application can perform:\n 1: Round to least integer\n 2: Round to upper integer\n 3: Remove decimal point\n 4: Exit \n Enter your choice:  ")
if process_1 == "1":
    result_1 = ceil(result)
    print("The process was rounding to upper integer and the result is: ", result_1)
elif process_1 == "2":
    result_1 = floor(result)
    print("The process was rounding to least integer and the result is: ", result_1)
elif process_1 == "3":
    result_1 = int(result)
    print("The process was remove decimal points and the result is: ", result_1)
elif process_1 == "4":
    print("Bye ...")
    exit()





