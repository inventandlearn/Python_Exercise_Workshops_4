class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self):
        self.name = None
        namechange_request = input("Do you wish to change your name? Enter Y or N: ")
        if namechange_request == "Y" or namechange_request == "y":
            name = input("Enter your newly desired name: ")
            self.name = name
        elif namechange_request == "N" or namechange_request == "n":
            print("You have canceled this request to change your name.")
            
    def change_pin(self):
        self.pin = None
        pinchange_request = input("Do you wish to change your pin? Enter Y or N: ")
        if pinchange_request == "Y" or pinchange_request == "y":
            pin = input("Enter your newly desired pin: ")
            self.pin = pin
        elif pinchange_request == "N" or pinchange_request == "n":
            print("You have canceled this request to change your pin.")
            
    def change_password(self):
        self.password = None
        passwordchange_request = input("Do you wish to change your password? Enter Y or N: ")
        if passwordchange_request == "Y" or passwordchange_request == "y":
            password = input("Enter your newly desired password: ")
            self.password = password
        elif passwordchange_request == "N" or passwordchange_request == "n":
            print("You have canceled this request to change your password.")
            

# ----Driver Code For Task 1----

# bank_user = User("Daniel", 1550, "Engineering90")
# print(bank_user.name, bank_user.pin, bank_user.password)


#----Driver Code For Task 2----

# updatedbank_user = User("Alteon", 5050, "Optical50")
# print(updatedbank_user.name, updatedbank_user.pin, updatedbank_user.password)
# updatedbank_user.change_name()
# updatedbank_user.change_pin()
# updatedbank_user.change_password()
# print(updatedbank_user.name, updatedbank_user.pin, updatedbank_user.password)


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        money_symbol = "{:.2f}".format(self.balance)
        print(f"{self.name} has an account balance of: ${money_symbol}")
    
    def withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount
        
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount

    def transfer_money(self, user, xfer_amount):
        print(f"You are transferring ${xfer_amount} to {user.name}")
        print("Your authentication is required to complete this transaction.")
        pin = int(input("Enter your PIN: "))

        if pin != self.pin:
            print("You have entered an invalid PIN number! This transaction is terminated!")
            return False
        elif pin == self.pin:
            print("Transfer Authorized!")
            print(f"Transferring ${xfer_amount} to {user.name}!")
            self.balance = self.balance - xfer_amount
            user.balance = user.balance + xfer_amount
            return True
    
    def request_money(self, user, xfer_amount):
            print(f"You are requesting ${xfer_amount} from {user.name}")
            print("User auhtentication is required......")
            pin = int(input(f"Enter {user.name} PIN: "))
            password = input(f"Enter {user.name} password: ")

            if pin != user.pin and password == user.password:
                    print("You have entered an invalid PIN! This transaction is terminated!")
                    return False
            elif pin == user.pin and password != user.password:
                    print("You have entered an invalid password! This transaction is terminated!")
                    return False
            elif pin == user.pin and password == user.password:
                    print("Request Authorized!")
                    print(f"{user.name} sent ${xfer_amount}!")
                    self.balance = self.balance + xfer_amount
                    user.balance = user.balance - xfer_amount
                    return True


#----Driver Code For Task 3----

# bank_customer1 = BankUser("Daniel ", 6050, " Engineering500 ")
# print(bank_customer1.name, bank_customer1.pin, bank_customer1.password, bank_customer1.balance)


#----Driver Code For Task 4----

# bank_customer2 = BankUser("Daniel", 6050, " Engineering500 ")
# bank_customer2.show_balance()
# bank_customer2.deposit(500)
# bank_customer2.show_balance()
# bank_customer2.withdraw(250)
# bank_customer2.show_balance()


#----Driver Code For Task 5----

bank_customer3 = BankUser("Daniel", 6050, "Engineering500")
bank_customer4 = BankUser( "Chris", 7000, "Optical50")
bank_customer3.deposit(1000)
bank_customer3.show_balance()
bank_customer4.show_balance()
bank_customer3.transfer_money(bank_customer4, 500)
bank_customer3.show_balance()
bank_customer4.show_balance()
bank_customer3.request_money(bank_customer4, 250)
bank_customer3.show_balance()
bank_customer4.show_balance()

