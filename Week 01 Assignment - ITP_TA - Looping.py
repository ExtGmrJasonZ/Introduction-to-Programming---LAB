def RightTriangle(num):                                     #print the right angle triangle shaped asterisks
    x = 0
    while x <= num:
        print(" "*(num+x), "*"*(num - x))
        x += 1

RightTriangle(5)

def Pyramid(num):                                           #print the pyramid shaped asterisks
    x = 0
    while x <= num:
        print(" "*(num-x)+"*"*(x+(x-1)))
        x += 1

Pyramid(5)


def Diamond(num):                                           #print the diamond shaped asterisks
    x = 0
    while x <= num:
        print(" "*(num-x)+"*"*(x+(x-1)))                    #code to make the upper triangle
        x += 1
    x = 1
    while x <= num:
        print(" "*x + "*"*((num - x)*2 - 1))
        x +=1

Diamond(5)
