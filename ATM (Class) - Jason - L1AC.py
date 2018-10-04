

class Account:                                                                                                          # Class named Account
    def __init__(self,name,balance):                                                                                    # begin with the function to initialize the name and balance
        self.name = name                                                                                                # declare "name" to be part of the Account class
        self.balance = float(balance)                                                                                   # declare "balance" to be part of the account class with the input later being a float

    def getName(self):                                                                                                  # Make another fucntion for getting the name of the customer
        return self.name                                                                                                # press enter to get the name of the customer

    def getCash(self):                                                                                                  # make another fucntion for inputing the cash that you will own
        return self.cash                                                                                                # press enter to get your amount of cash

    def Balance(self):                                                                                                  # make another function to get the balance in the card
        return self.balance                                                                                             # press enter to get your balance

    def deposit(self,amount,cash):                                                                                      # make a new function for deposit
        self.amount = float(amount)                                                                                     # for inputing the cash you want to deposit into your account
        self.cash = float(cash)                                                                                         # declare cash as part of this function too
        if self.amount > 0:                                                                                             # if the amount of cash you want to deposit is greater than 0 (Duh, of course)

            if self.cash >= self.amount:                                                                                # if conditional for the condition your cash is greater or equal to the amount
                self.balance += self.amount                                                                             # This will add amount for your balance
                self.cash -= self.amount                                                                                # for deposit, our cash will be decreased by the amount
                return print("balance = {} cash = {}".format(self.balance, self.cash))                                  # press enter to print result for the balance and cash after depositing


            else:                                                                                                       # else conditional for the condition the cash is less than amount
                return print("Insufficient funds")

    def withdraw(self,amount):                                                                                          # make a function for withdraw
        self.amount = float(amount)                                                                                     # make amount that will be used for how much money that is in your account
        if self.balance >= self.amount:                                                                                 # if conditional for the condition the balance of your account is greater or equal to the amount in the account
            self.balance -= self.amount                                                                                 # for withdraw, balance is decreased by amount
            self.cash += self.amount                                                                                    # for withdraw, our cash is increased by amount
            return print("balance = {} cash = {}".format(self.balance, self.cash))                                      # print the result of balance and cash after withdrawing


        else:
            return print("Insuffiecient funds")                                                                         #else conditional, print this sentence



Name = input("enter your name: ")                                                                                       # Variable name for inputing your name
A_ccount = Account(Name,0)                                                                                              # variable A_ccount is an object to call class Account
Cash = input("cash = ")                                                                                                 # enter how much money you want for your cash
print(Cash)                                                                                                             # print the amount of cash that you inputed

while True:                                                                                                             # while looping for the condition to make this program endless until you choose to quit
    print("Option: \n 1.Deposit \n 2.Withdraw \n 3.Check Balance \n 4.Quit")                                            # print out the available option
    choice = input("Enter your choice: ")                                                                               # enter your choice from the option

    if choice == "1":                                                                                                   # if your choice is option 1
        Amount = float(input("enter the amount: "))                                                                     # enter the amount that you want to deposit
        print(A_ccount.deposit(Amount,Cash))                                                                            # print the resul of deposit (will show you balance and cash)

    elif choice == "2":                                                                                                 # if your choice is option 2
        Amount = float(input("enter the amount: "))                                                                     # enter the amount that you want to withdraw
        print(A_ccount.withdraw(Amount))                                                                                # print the result of withdraw(will show you balance and cash)

    elif choice == "3":                                                                                                 # if your choice is option 3
        print(A_ccount.Balance())                                                                                       # print the balance

    elif choice == "4":                                                                                                 # if your choice is option 4
        print("Thank you for using this service")                                                                       # print this sentence
        break                                                                                                           # to break the loop and stop the program



