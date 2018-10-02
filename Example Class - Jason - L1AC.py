'''
class Test:
    def fun(self):
        print("Hello")
obj = Test()
obj.fun()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hi(self):
        print('Hello, my name is', self.name , 'and I am', self.age)
p = Person ('Shwetanshu',"18")
p.say_hi()
me = Person ('Jason Sianandar',"17")
me.say_hi()
'''

class Calculator:                                                                                                       #Class calculator
    def __init__(self, num1, num2):                                                                                     #Initiate (self, num1, num2)
        self.n1 = num1                                                                                                  #num 1 is self.n1
        self.n2 = num2                                                                                                  #num 2 is self.n2

    def add(self):                                                                                                      #Function for addition
        return self.n1 + self.n2                                                                                        #Press enter for first number to be added with the second number
    def subtract(self):                                                                                                 #Function for subtraction
        return self.n1 - self.n2                                                                                        #Press enter for first number to be subtracted with the second number
    def multiply(self):                                                                                                 #Function for multiply
        return self.n1 * self.n2                                                                                        #Press enter for first number to be multiplied with the second number
    def divide(self):                                                                                                   #Function for division
        return self.n1 / self.n2                                                                                        #Press enter for first number to be divided with the second number


one = int(input("Enter any numbers: "))                                                                                 #variable one, we input the first number
op = input("Enter an operator: ")                                                                                       #variable op, we input the operator
two = int(input("Enter the second number: "))                                                                           #variable two, we input the second number

op_list = ["+", "-", "*", "/"]                                                                                          #variable op_list contains the lists of operators that we can enter

if op == op_list[0]:                                                                                                    #if conditional the operator is equal to + from index 0 from op_list
    cal = Calculator(one, two)                                                                                          #variable cal, we take from the class Calculator
    print(cal.add())                                                                                                    #print the result
elif op == op_list[1]:                                                                                                  #else if conditional the operator is equal to - from index 1 from op_list
    cal = Calculator(one, two)                                                                                          #variable cal, we take from the class calculator
    print(cal.subtract())                                                                                               #print the result
elif op == op_list[2]:                                                                                                  #else if conditional the operator is equal to * from index 2 from op_list
    cal = Calculator(one, two)                                                                                          #variable cal, we take from the class calculator
    print(cal.multiply())                                                                                               #print the result
elif op == op_list[3]:                                                                                                  #else if conditional the operator is equal to / from index 3 from op_list
    cal = Calculator(one, two)                                                                                          #variable cal, we take from the class calculator
    print(cal.divide())                                                                                                 #print the result
