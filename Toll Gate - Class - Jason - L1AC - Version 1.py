# Tollgate by Jason
class Car:                                              #Class for Car
    def __init__(self, car):                            #Initiator for car
        self.w_4 = car                                  #Declare car as part of the class
    def getCar(self):                                   #Function to return car
        return self.w_4                                 #Return car
class Bus:                                              #Class for Bus
    def __init__(self, bus):                            #Iniator for bus
        self.w_6 = bus                                  #Declare bus as part of the class
    def getBus(self):                                   #Function to return bus
        return self.w_6                                 #Return bus
class Truck:                                            #Class for Truck
    def __init__(self, truck):                          #Iniator for truck
        self.w_8 = truck                                #Iniator for truck
    def getTruck(self):                                 #Function to return truck
        return self.w_8                                 #return truck

class Tollgate(Car, Bus, Truck):                        #Class Tollgate inheriting the subclasses of Car, Bus, Truck
    def __init__(self, type):                           #Iniator for types
        super().__init__(type)                          #Make a super class
    def car_fee(self):                                  # Fucntion for car fee
        Car.getCar = 6000                               # car fee is 6000
        return Car.getCar                               # return the car fee
    def bus_fee(self):                                  # Function for bus fee
        Bus.getBus = 8000                               # bus fee is 8000
        return Bus.getBus                               # return the bus fee
    def truck_fee(self):                                # Function for the truck fee
        Truck.getTruck = 10000                          # truck fee is 10000
        return Truck.getTruck                           # return truck fee


restart = "Y"                                           # restart variable is "Y"


def toll_operator():                                    # Function for toll operator
    while restart != ("N"):                             # While looping for the condition the input is not "N"
        print("="*25)                                   # print caption
        print(" "*2, "Toll Payment systems")            # print caption
        print(" "*2, "Pt Jasa Marga, Tbk")              # print caption
        print("="*25)                                   # print caption

        print("Category of vehicle: ")                  # print caption
        print("1. Car (Rp 6000)\n2. Bus (Rp 8000)\n3. Truck (Rp 10000)")# print caption

        Userinput = input("Category of vehicle: ").lower() # Variable userinput for inputing in the category of vehicle caption and lowercase all the letters
        TG = Tollgate(Userinput)                        # TG Object from class Tollgate
        if Userinput == "car":                          # if choice is "car"
            print("Fee: Rp.{}".format(TG.car_fee()))    # print the caption and the fee from class
            Again = input("Is there any other vehicle (Y/N)? ").upper() # Again is the variable for inputing Y or N
            if Again == "N":                            # if condition for the input is N
                print("<Exit Program>")                 # print exit program
                break                                   # break the loop
        if Userinput == "bus":                          # if choice is "bus"
            print("Fee: Rp.{}".format(TG.bus_fee()))    # print the caption and the fee from class
            Again = input("Is there any other vehicle (Y/N)? ").upper() # Again is the variable for inputing Y or N
            if Again == "N":                            # if condition for the input is N
                print("<Exit Program>")                 # print exit program
                break                                   # break the loop
        if Userinput == "truck":                        # if choice is truck
            print("Fee: Rp. {}".format(TG.truck_fee())) # print the caption and the fee from class
            Again = input("Is there any other vehicle (Y/N)? ").upper() # Again is the variable for inputing Y or N
            if Again == "N":                            # if condition for the input is N
                print("<Exit Program>")                 # print caption
                break                                   # break the loop

toll_operator()                                         # call the function toll operator









