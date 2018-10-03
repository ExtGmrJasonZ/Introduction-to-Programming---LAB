print("Lambda Calculator")

add = lambda a, b : a + b                                                                                               # this is the variable add for the lambda of addition

subtract = lambda a, b : a - b                                                                                          # this is the variable subtract for the lambda of subtraction

multiply = lambda a, b : a * b                                                                                          # this is the variable multiply for the lambda of multiply

divide = lambda a, b : a / b                                                                                            # this is the variable divide for the lambda of divide
                                                               
def maincalculator():                                                                                                   # Main function for the calculator
    calc = True                                                                                                         # calc = True
    num1 = int(input("Enter number 1: "))                                                                               # variable num 1 for inputing number 1
    while calc == True:                                                                                                 # while looping for the condition calc = True

        num2 = int(input("Enter number 2: "))                                                                           # input number 2
        op = input("Input the operator, or 'e' if you want to quit: ")                                                  # input the operator

        if op == "+":                                                                                                   # if condition the operator is + then result will be num 1 + num 2
            result = add(num1, num2)
            print(result)
        elif op == "-":                                                                                                 # if condition the operator is - then result will be num 1 - num 2
            result = subtract(num1, num2)
            print(result)
        elif op == "*":                                                                                                 # if condition the operator is * then result will be num 1 * num 2
            result = multiply(num1, num2)
            print(result)
        elif op == "/":                                                                                                 # if condition the operator is * then result will be num 1 / num 2
            result = divide(num1, num2)
            print(result)
        elif op == "e":                                                                                                 # if condition the operator is e then the program will quit
            run = False
            print("You have quit this program", result)
            break                                                                                                       # it will break the whole loop

    r = result

maincalculator()

# Reference from Ryan Rusli
