'''
x = lambda  a : a + 10
print(x(5))

arr = [1, 2, 3, 4, 5]
x = lambda b : b [-1]
print(x(arr))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)

print(mydoubler(120))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print("Lambda Calculator")
'''
add = lambda a, b : a + b                                                                                               # this is the variable add for the lambda of addition

subtract = lambda a, b : a - b                                                                                          # this is the variable subtract for the lambda of subtraction

multiply = lambda a, b : a * b                                                                                          # this is the variable multiply for the lambda of multiply

divide = lambda a, b : a / b                                                                                            # this is the variable divide for the lambda of divide

userinput = input("Enter any numbers: ")                                                                                # variable user input for inputing the numbers
us = userinput.split()                                                                                                  # the variable us for splitting the user input to strings
list = list(us)                                                                                                         # variable of list for listing the us so we can use indexing

if list[1] == "+":                                                                                                      # if conditional if index 1 in the list is +
    print(add(int(list[0]), int(list[2])))                                                                              # print function add for the integers in index 0 and 2 (int is to make sure it is integer)
elif list[1] == "-":                                                                                                    # else if conditional if index 1 in the list is -
    print(subtract(int(list[0]), int(list[2])))                                                                         # print function subtract for the integers in index 0 and 2
elif list[1] == "*":                                                                                                    # else if conditional if index 1 in the list is *
    print(multiply(int(list[0]), int(list[2])))                                                                         # print function multiply for the integers in index 0 and 2
elif list[1] == "/":                                                                                                    # else if conditional if index 1 in the list is /
    print(divide(int(list[0]), int(list[2])))                                                                           # print fucntion divide for the integers in index 0 and 2
