# Hotel Simulation by Jason
class CheckIn:                          #class check in
    def __init__(self, check_in):
        self.check1n = check_in
    def getInSr(self):
        return self.check1n
    def getInDr(self):
        return self.check1n

class CheckOut:                         #class check out
    def __init__(self, checkout):
        self.checkOut = checkout
    def getOutSr(self):
        return self.checkOut
    def getOutDr(self):
        return self.checkOut

class Operator(CheckIn, CheckOut):      #class operator
    def __init__(self, category):       #superclass
        super().__init__(category)
    def singleroom_fee(self):           #method for single room fee
        CheckOut.getOutSr = 1000000
        return CheckOut.getOutSr
    def doubleroom_fee(self):           #method for double room fee
        CheckOut.getOutDr = 2000000
        return CheckOut.getOutDr

def Hotel_operator():                   #function for hotel operator
    listofSingleRooms = 5               #list of single rooms
    listofDoubleRooms = 5               #list of double rooms

    listofdays1a = 0                    #days spent in room 1a
    listofdays2a = 0                    #days spent in room 2a
    listofdays3a = 0                    #days spent in room 3a
    listofdays4a = 0                    #days spent in room 4a
    listofdays5a = 0                    #days spent in room 5a

    listofdays1b = 0                    #days spent in room 1b
    listofdays2b = 0                    #days spent in room 2b
    listofdays3b = 0                    #days spent in room 3b
    listofdays4b = 0                    #days spent in room 4b
    listofdays5b = 0                    #days spent in room 5b

    while True:                         # while true
        print("="*75)
        print("Hi there, welcome to Hotel Simulation b*****")
        print("="*75)

        print("Check In")
        print("1.Single Rooms\n2.Double Rooms")
        usrinput = input("Which type of room you would like? ") # selecting type of rooms
        if usrinput == "1":             # if I input 1
            print(listofSingleRooms, "rooms left")
            print("1a, 2a, 3a, 4a, 5a")
            Userinput = input("Which room would you like to stay in: ").lower() # selecting the desired room
            Op = Operator(Userinput)    # creating an object Op

            if Userinput == "1a":
                listofSingleRooms -= 1          # the list will be subtracted by 1
                print("Fee: Rp.{}".format(Op.singleroom_fee()), "per night")
                print("Maximum 3 Nights Stay")
                print(listofSingleRooms, "rooms left")
                days = input("How many days would you be staying? ")        # selecting the days spent
                if days == "1":
                    listofdays1a += 1       # list of days spent added by 1
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays1a))  #fee * days spent
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")  #selecting other options


                    if Again == "1":       # if I want to check in again
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":       # if I want to check out for good
                        print("Thank you for using our services.")
                        break
                    if Again == "3":       # if I want to check my revenue
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "2":
                    listofdays1a += 2
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays1a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))

                if days == "3":
                    listofdays1a += 3
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays1a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))

            elif Userinput == "2a":             # room 2a
                listofSingleRooms -= 1
                print("Fee: Rp.{}".format(Op.singleroom_fee()), "per night" )
                print("Maximum 3 Nights Stay")
                print(listofSingleRooms, "rooms left")
                days = input("How many days would you be staying? ")
                if days == "1":
                    listofdays2a += 1
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays2a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "2":
                    listofdays2a += 2
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays2a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "3":
                    listofdays2a += 3
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays2a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
            elif Userinput == "3a":            # room 3a
                listofSingleRooms -= 1
                print("Fee: Rp.{}".format(Op.singleroom_fee()), "per night" )
                print("Maximum 3 Nights Stay")
                print(listofSingleRooms, "rooms left")
                days = input("How many days would you be staying? ")
                if days == "1":
                    listofdays3a += 1
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays3a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "2":
                    listofdays3a += 2
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays3a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "3":
                    listofdays3a += 3
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays3a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))

            elif Userinput == "4a":            # room 4a
                listofSingleRooms -= 1
                print("Fee: Rp.{}".format(Op.singleroom_fee()), "per night" )
                print("Maximum 3 Nights Stay")
                print(listofSingleRooms, "rooms left")
                days = input("How many days would you be staying? ")
                if days == "1":
                    listofdays4a += 1
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays4a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "2":
                    listofdays4a += 2
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays4a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "3":
                    listofdays4a += 3
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays4a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))

            elif Userinput == "5a":             # room 5a
                listofSingleRooms -= 1
                print("Fee: Rp.{}".format(Op.singleroom_fee()), "per night" )
                print("Maximum 3 Nights Stay")
                print(listofSingleRooms, "rooms left")
                days = input("How many days would you be staying? ")
                if days == "1":
                    listofdays5a += 1
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays5a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "2":
                    listofdays5a += 2
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays5a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "3":
                    listofdays5a += 3
                    print("The price would be Rp.{}".format(Op.singleroom_fee()*listofdays5a))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
        if usrinput == "2":         # if I input 2
            print(listofDoubleRooms)
            print("1b, 2b, 3b, 4b, 5b")
            Userinput = input("Which room would you like to stay in: ").lower()    # selecting the desired rooms
            Op = Operator(Userinput)    # creating an object Op

            if Userinput == "1b":       # room 1b
                listofDoubleRooms -= 1
                print("Fee: Rp.{}".format(Op.doubleroom_fee()), "per night" )
                print("Maximum 3 Nights Stay")
                print(listofDoubleRooms, "rooms left")
                days = input("How many days would you be staying? ")
                if days == "1":
                    listofdays1b += 1
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays1b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "2":
                    listofdays1b += 2
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays1b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "3":
                    listofdays1b += 3
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays1b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
            elif Userinput == "2b":         # room 2b
                listofDoubleRooms -= 1
                print("Fee: Rp.{}".format(Op.doubleroom_fee()), "per night" )
                print("Maximum 3 Nights Stay")
                print(listofDoubleRooms, "rooms left")
                days = input("How many days would you be staying? ")
                if days == "1":
                    listofdays2b += 1
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays2b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "2":
                    listofdays2b += 2
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays2b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "3":
                    listofdays2b += 3
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays2b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))


            elif Userinput == "3b":         # room 3b
                listofDoubleRooms -= 1
                print("Fee: Rp.{}".format(Op.doubleroom_fee()), "per night" )
                print("Maximum 3 Nights Stay")
                print(listofDoubleRooms, "rooms left")
                days = input("How many days would you be staying? ")
                if days == "1":
                    listofdays3b += 1
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays3b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "2":
                    listofdays3b += 2
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays3b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "3":
                    listofdays3b += 3
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays3b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))

            elif Userinput == "4b":         # room 4b
                listofDoubleRooms -= 1
                print("Fee: Rp.{}".format(Op.doubleroom_fee()), "per night" )
                print("Maximum 3 Nights Stay")
                print(listofDoubleRooms, "rooms left")
                days = input("How many days would you be staying? ")
                if days == "1":
                    listofdays4b += 1
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays4b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "2":
                    listofdays4b += 2
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays4b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "3":
                    listofdays4b += 3
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays4b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))

            elif Userinput == "5b":         # room 5b
                listofDoubleRooms -= 1
                print("Fee: Rp.{}".format(Op.doubleroom_fee()), "per night" )
                print("Maximum 3 Nights Stay")
                print(listofDoubleRooms, "rooms left")
                days = input("How many days would you be staying? ")
                if days == "1":
                    listofdays5b += 1
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays5b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "2":
                    listofdays5b += 2
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays5b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))
                if days == "3":
                    listofdays5b += 3
                    print("The price would be Rp.{}".format(Op.doubleroom_fee()*listofdays5b))
                    print("1.Check In with Rooms Available\n2. Check Out\n3. Check Revenue")
                    Again = input("Is there anything else that we can help you? ")

                    if Again == "1":
                        print("Single rooms available: ", listofSingleRooms)
                        print("Double rooms available: ", listofDoubleRooms)
                    if Again == "2":
                        print("Thank you for using our services.")
                        break
                    if Again == "3":
                        revenue1 = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a)
                        revenue2 = (Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b)
                        revenuetotal = (Op.singleroom_fee() * listofdays1a + Op.singleroom_fee() * listofdays2a + Op.singleroom_fee() * listofdays3a + Op.singleroom_fee() * listofdays4a + Op.singleroom_fee() * listofdays5a + Op.doubleroom_fee() * listofdays1b + Op.doubleroom_fee() * listofdays2b + Op.doubleroom_fee() * listofdays3b + Op.doubleroom_fee() * listofdays4b + Op.doubleroom_fee() * listofdays5b )
                        print("The revenue of single room is {}".format(revenue1))
                        print("The revenue of double room is {}".format(revenue2))
                        print("The grand total revenue is {}".format(revenuetotal))


Hotel_operator()            # run the function
