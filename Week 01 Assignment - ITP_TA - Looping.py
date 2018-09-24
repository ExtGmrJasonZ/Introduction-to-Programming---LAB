def RightTriangle(num):                                     # Module for printing the right angle triangle shaped asterisks
    x = 0                                                   # x starts from 0
    while x <= num:                                         # this is the while loop in which the condition is x is less than or equal to the value of num
        print(" "*(num+x), "*"*(num - x))                   # print the spaces to increase down the line and print the asterisks also decrease down the line
        x += 1                                              # ready to continue to new line

RightTriangle(5)                                            # this means that I want to print 5 rows of the module

def Pyramid(num):                                           #Module for printing the pyramid shaped asterisks
    x = 0                                                   # x starts from 0
    while x <= num:                                         # this is the while loop in which the condition is x is less than or equal to the value of num
        print(" "*(num-x)+"*"*(x+(x-1)))                    # print the spaces to decrease down the line and print the asterisks multiply by the value of x + (x - 1)
        x += 1                                              # ready to continue to new line

Pyramid(5)                                                  # this means that I want to print 5 rows of the module


def Diamond(num):                                           # Moduule for printing the diamond shaped asterisks
    x = 0                                                   # x starts from 0
    while x <= num:                                         # this is the while loop in which the condition is x is less than or equal to the value of num
        print(" "*(num-x)+"*"*(x+(x-1)))                    # print the spaces to decrease down the line and print the asterisks multiply by the value of x + (x - 1)               #Upper Triangle
    x = 1                                                   # x starts from 1
    while x <= num:                                         # this is the while loop in which the condition is x is less than or equal to the value of num
        print(" "*x + "*"*((num - x)*2 - 1))                # print the spaces multiply by the value of x added by printing the asterisks multiply by the value of ((num - x)*2 -1) #Lower Triangle
        x +=1                                               # ready to continue to new line

Diamond(5)                                                  # this means that I want to print 5 rows of the module
