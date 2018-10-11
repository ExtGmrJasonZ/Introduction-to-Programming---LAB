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


def toll_operator():                                    # function for toll operator
    listofCars = 0                                      # list for number of cars
    listofBus = 0                                       # list for number of bus
    listofTrucks = 0                                    # list for number of trucks

    while restart != ("N"):                             # While looping for the condition the input is not "N"
        print("="*25)                                   # print caption
        print(" "*2, "Toll Payment systems")            # print caption
        print(" "*2, "Pt Jasa Marga, Tbk")              # print caption
        print("="*25)                                   # print caption

        print("Category of vehicle: ")                  # print caption
        print("1. Car (Rp 6000)\n2. Bus (Rp 8000)\n3. Truck (Rp 10000)")# print caption
        Userinput = input("Category of vehicle: ").lower()              # Userinput variable for inputing your choices
        TG = Tollgate(Userinput)                                        # TG Object from Tollgate
        if Userinput == "car":                                          # if condition for your choice for car
            listofCars += 1                                             # List for number of cars is added by 1 for the value
            print("Fee: Rp.{}".format(TG.car_fee()))                    # print caption and the fee of the car
            print(listofCars, "Cars")                                   # print the number of cars
            Again = input("Is there any other vehicle (Y/N)? ").upper() # Again variable for inputing Y or N
            if Again == "N":                                            # If condition the coice is N
                print("Car  Bus  Truck")                                # print caption
                print("{}   {}   {}.".format(listofCars, listofBus, listofTrucks))      # print the number of all vehicles
                revenue = (TG.car_fee() * listofCars + TG.bus_fee() * listofBus + TG.truck_fee() * listofTrucks)    # variable for calculating the revenue
                print("The revenue is {}".format(revenue))              # print the revenue
                print("<Exit Program>")                                 # print the caption
                break                                                   # break the loop
        if Userinput == "bus":                                          # if input is the bus
            listofBus += 1                                              # the value of number of buses is added by 1
            print("Fee: Rp.{}".format(TG.bus_fee()))                    # print the caption and the fee of the bus
            print(listofBus, "Buses")                                   # print the list of the buses
            Again = input("Is there any other vehicle (Y/N)? ").upper() # Variable for inputing the Y or N
            if Again == "N":                                            # if the input is N
                print("Car  Bus  Truck")                                # print the caption
                print("{}   {}   {}.".format(listofCars, listofBus, listofTrucks))      # print the list of all the vehicles
                revenue = (TG.car_fee() * listofCars + TG.bus_fee() * listofBus + TG.truck_fee() * listofTrucks)    # variable for calculating the revenue
                print("The revenue is {}".format(revenue))              # print the revenue
                print("<Exit Program>")                                 # print caption
                break                                                   # break the loop
        if Userinput == "truck":                                        # If the input is truck
            listofTrucks += 1                                           # the number of the buses is added by 1
            print("Fee: Rp. {}".format(TG.truck_fee()))                 # print the caption and the fee of the bus
            print(listofTrucks, "Trucks")                               # print the list of trucks
            Again = input("Is there any other vehicle (Y/N)? ").upper() # Variable for inputing Y or N
            if Again == "N":                                            # if input is N
                print("Car  Bus  Truck")                                # print the caption
                print("{}   {}   {}.".format(listofCars, listofBus, listofTrucks))      # print the list of all the vehicles
                revenue = (TG.car_fee() * listofCars + TG.bus_fee() * listofBus + TG.truck_fee() * listofTrucks)    # variable for calculating the revenue
                print("The revenue is {}".format(revenue))              # print the revenue
                print("<Exit Program>")                                 # print the caption
                break                                                   # break the loop

toll_operator()                                                         # Run the function









