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

class Tollgate2(Car, Bus, Truck):                       # Class for tollgate 2
    def __init__(self, type):
        super().__init__(type)
    def car_fee(self):
        Car.getCar = 18000
        return Car.getCar
    def bus_fee(self):
        Bus.getBus = 20000
        return Bus.getBus
    def truck_fee(self):
        Truck.getTruck = 25000
        return Truck.getTruck

restart = "Y"                                           # restart variable is "Y"


def toll_operator():                                    # function for toll operator
    listofCars = 0                                      # list for number of cars
    listofBus = 0                                       # list for number of bus
    listofTrucks = 0                                    # list for number of trucks

    NumofCars = 0                                       # List for the other tollgate
    NumofBus = 0
    NumofTruck = 0

    while restart != ("N"):                             # While looping for the condition the input is not "N"
        print("="*25)                                   # print caption
        print(" "*2, "Toll Payment systems")            # print caption
        print(" "*2, "Pt Jasa Marga, Tbk")              # print caption
        print("="*25)                                   # print caption

        print("1. Meruya Toll Gate \n2. Pondok Aren Toll Gate")     # print caption
        usrinput = input("Location:")                               # variable for inputing location
        if usrinput == "1":
            print("Category of vehicle: ")                  # print caption
            print("1. Car (Rp 6000)\n2. Bus (Rp 8000)\n3. Truck (Rp 10000)")# print caption
            Userinput = input("Category of vehicle - (Input car/bus/truck): ").lower()              # Userinput variable for inputing your choices
            TG = Tollgate(Userinput)                                        # TG Object from Tollgate
            TG2 = Tollgate2(Userinput)
            if Userinput == "car":                                          # if condition for your choice for car
                listofCars += 1                                             # List for number of cars is added by 1 for the value
                print("Fee: Rp.{}".format(TG.car_fee()))                    # print caption and the fee of the car
                print(listofCars, "Cars")                                   # print the number of cars
                Again = input("Is there any other vehicle (Y/N)? ").upper() # Again variable for inputing Y or N
                if Again == "N":                                            # If condition the coice is N
                    print("Location: Meruya")
                    print("="*25)
                    print("Car  Bus  Truck")                                # print caption
                    print("="*25)
                    print("{}   {}   {}.".format(listofCars, listofBus, listofTrucks))      # print the number of all vehicles
                    print("Location: Pondok Aren")
                    print("="*25)
                    print("Car  Bus  Truck")
                    print("="*25)
                    print("{}   {}   {}.".format(NumofCars, NumofBus, NumofTruck))
                    revenue = (TG.car_fee() * listofCars + TG.bus_fee() * listofBus + TG.truck_fee() * listofTrucks)    # variable for calculating the revenue for the meruya tollgate
                    revenue2 = (TG2.car_fee() * NumofCars + TG2.bus_fee() * NumofBus + TG2.truck_fee() * NumofTruck)    # variable for calculating the revenue for the pondok aren tollgate
                    gtotalrevenue = revenue + revenue2                                                                  # for counting the grand total revenue
                    print("The revenue of Meruya Tollgate is {}".format(revenue))              # print the revenue
                    print("The revenue of Pondok Aren Tollgate is {}".format(revenue2))        # print the revenue
                    print("The grand total revenue is {}".format(gtotalrevenue))               # print the grand total revenue
                    print("<Exit Program>")                                 # print the caption
                    break                                                   # break the loop

            if Userinput == "bus":                                          # if input is the bus
                listofBus += 1                                              # the value of number of buses is added by 1
                print("Fee: Rp.{}".format(TG.bus_fee()))                    # print the caption and the fee of the bus
                print(listofBus, "Buses")                                   # print the list of the buses
                Again = input("Is there any other vehicle (Y/N)? ").upper() # Variable for inputing the Y or N
                if Again == "N":                                            # if the input is N
                    print("Location: Meruya")
                    print("="*25)
                    print("Car  Bus  Truck")                                # print caption
                    print("="*25)
                    print("{}   {}   {}.".format(listofCars, listofBus, listofTrucks))      # print the number of all vehicles
                    print("Location: Pondok Aren")
                    print("="*25)
                    print("Car  Bus  Truck")
                    print("="*25)
                    print("{}   {}   {}.".format(NumofCars, NumofBus, NumofTruck))
                    revenue = (TG.car_fee() * listofCars + TG.bus_fee() * listofBus + TG.truck_fee() * listofTrucks)    # variable for calculating the revenue
                    revenue2 = (TG2.car_fee() * NumofCars + TG2.bus_fee() * NumofBus + TG2.truck_fee() * NumofTruck)
                    gtotalrevenue = revenue + revenue2
                    print("The revenue of Meruya Tollgate is {}".format(revenue))              # print the revenue
                    print("The revenue of Pondok Aren Tollgate is {}".format(revenue2))
                    print("The grand total revenue is {}".format(gtotalrevenue))
                    print("<Exit Program>")                                 # print the caption
                    break                                                   # break the loop

            if Userinput == "truck":                                        # If the input is truck
                listofTrucks += 1                                           # the number of the buses is added by 1
                print("Fee: Rp. {}".format(TG.truck_fee()))                 # print the caption and the fee of the bus
                print(listofTrucks, "Trucks")                               # print the list of trucks
                Again = input("Is there any other vehicle (Y/N)? ").upper() # Variable for inputing Y or N
                if Again == "N":                                            # if input is N
                    print("Location: Meruya")
                    print("="*25)
                    print("Car  Bus  Truck")                                # print caption
                    print("="*25)
                    print("{}   {}   {}.".format(listofCars, listofBus, listofTrucks))      # print the number of all vehicles
                    print("Location: Pondok Aren")
                    print("="*25)
                    print("Car  Bus  Truck")
                    print("="*25)
                    print("{}   {}   {}.".format(NumofCars, NumofBus, NumofTruck))
                    revenue = (TG.car_fee() * listofCars + TG.bus_fee() * listofBus + TG.truck_fee() * listofTrucks)    # variable for calculating the revenue
                    revenue2 = (TG2.car_fee() * NumofCars + TG2.bus_fee() * NumofBus + TG2.truck_fee() * NumofTruck)
                    gtotalrevenue = revenue + revenue2
                    print("The revenue of Meruya Tollgate is {}".format(revenue))              # print the revenue
                    print("The revenue of Pondok Aren Tollgate is {}".format(revenue2))
                    print("The grand total revenue is {}".format(gtotalrevenue))
                    print("<Exit Program>")                                 # print the caption
                    break                                                   # break the loop
        if usrinput == "2":
            print("Category of vehicle: ")                  # print caption
            print("1. Car (Rp 18000)\n2. Bus (Rp 20000)\n3. Truck (Rp 25000)")
            Userinput = input("Category of vehicle - (Input car/bus/truck): ").lower()              # Userinput variable for inputing your choices


            if Userinput == "car":                                          # if condition for your choice for car
                NumofCars += 1                                             # List for number of cars is added by 1 for the value
                print("Fee: Rp.{}".format(TG2.car_fee()))                    # print caption and the fee of the car
                print(NumofCars, "Cars")                                   # print the number of cars
                Again = input("Is there any other vehicle (Y/N)? ").upper() # Again variable for inputing Y or N
                if Again == "N":                                            # If condition the coice is N
                    print("Location: Meruya")
                    print("Location: Meruya")
                    print("="*25)
                    print("Car  Bus  Truck")                                # print caption
                    print("="*25)
                    print("{}   {}   {}.".format(listofCars, listofBus, listofTrucks))      # print the number of all vehicles
                    print("Location: Pondok Aren")
                    print("="*25)
                    print("Car  Bus  Truck")
                    print("="*25)
                    print("{}   {}   {}.".format(NumofCars, NumofBus, NumofTruck))
                    revenue = (TG.car_fee() * listofCars + TG.bus_fee() * listofBus + TG.truck_fee() * listofTrucks)    # variable for calculating the revenue
                    revenue2 = (TG2.car_fee() * NumofCars + TG2.bus_fee() * NumofBus + TG2.truck_fee() * NumofTruck)
                    gtotalrevenue = revenue + revenue2
                    print("The revenue of Meruya Tollgate is {}".format(revenue))              # print the revenue
                    print("The revenue of Pondok Aren Tollgate is {}".format(revenue2))
                    print("The grand total revenue is {}".format(gtotalrevenue))
                    print("<Exit Program>")                                 # print the caption
                    break                                                   # break the loop

            if Userinput == "bus":                                          # if input is the bus
                NumofBus += 1                                              # the value of number of buses is added by 1
                print("Fee: Rp.{}".format(TG2.bus_fee()))                    # print the caption and the fee of the bus
                print(NumofBus, "Buses")                                   # print the list of the buses
                Again = input("Is there any other vehicle (Y/N)? ").upper() # Variable for inputing the Y or N
                if Again == "N":                                            # if the input is N
                    print("Location: Meruya")
                    print("="*25)
                    print("Car  Bus  Truck")                                # print caption
                    print("="*25)
                    print("{}   {}   {}.".format(listofCars, listofBus, listofTrucks))      # print the number of all vehicles
                    print("Location: Pondok Aren")
                    print("="*25)
                    print("Car  Bus  Truck")
                    print("="*25)
                    print("{}   {}   {}.".format(NumofCars, NumofBus, NumofTruck))
                    revenue = (TG.car_fee() * listofCars + TG.bus_fee() * listofBus + TG.truck_fee() * listofTrucks)    # variable for calculating the revenue
                    revenue2 = (TG2.car_fee() * NumofCars + TG2.bus_fee() * NumofBus + TG2.truck_fee() * NumofTruck)
                    gtotalrevenue = revenue + revenue2
                    print("The revenue of Meruya Tollgate is {}".format(revenue))              # print the revenue
                    print("The revenue of Pondok Aren Tollgate is {}".format(revenue2))
                    print("The grand total revenue is {}".format(gtotalrevenue))
                    print("<Exit Program>")                                 # print the caption
                    break                                                   # break the loop

            if Userinput == "truck":                                        # If the input is truck
                NumofTruck += 1                                           # the number of the buses is added by 1
                print("Fee: Rp. {}".format(TG2.truck_fee()))                 # print the caption and the fee of the bus
                print(NumofTruck, "Trucks")                               # print the list of trucks
                Again = input("Is there any other vehicle (Y/N)? ").upper() # Variable for inputing Y or N
                if Again == "N":                                            # if input is N
                    print("Location: Meruya")
                    print("="*25)
                    print("Car  Bus  Truck")                                # print caption
                    print("="*25)
                    print("{}   {}   {}.".format(listofCars, listofBus, listofTrucks))      # print the number of all vehicles
                    print("Location: Pondok Aren")
                    print("="*25)
                    print("Car  Bus  Truck")
                    print("="*25)
                    print("{}   {}   {}.".format(NumofCars, NumofBus, NumofTruck))
                    revenue = (TG.car_fee() * listofCars + TG.bus_fee() * listofBus + TG.truck_fee() * listofTrucks)    # variable for calculating the revenue
                    revenue2 = (TG2.car_fee() * NumofCars + TG2.bus_fee() * NumofBus + TG2.truck_fee() * NumofTruck)
                    gtotalrevenue = revenue + revenue2
                    print("The revenue of Meruya Tollgate is {}".format(revenue))              # print the revenue
                    print("The revenue of Pondok Aren Tollgate is {}".format(revenue2))
                    print("The grand total revenue is {}".format(gtotalrevenue))
                    print("<Exit Program>")                                 # print the caption
                    break                                                   # break the loop

toll_operator()                                                         # Run the function
