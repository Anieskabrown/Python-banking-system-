import datetime

class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
        
        try:
            self.balance = float(balance)
        except:
            self.balance = 0.0
            print("\n[Warning] Invalid initial balance. Set to 0.")
            
        self.transactions = []
        self.account_type = "regular"
        self.overdraft_limit = 0.0
        self.interest_rate = 0.0
        
        
    def update_first_name(self, fname):
        if fname.strip() == "":
           print("\nInvalid first name.")
           return
        self.fname = fname
    
            
    def update_last_name(self, lname):
        if lname.strip() == "":
            print("\nInvalid last name.")
            return
        self.lname = lname
              
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        if not isinstance(addr, list) or len(addr) != 4:
            print("\nInvalid address format. Must contain 4 lines.")
            return
        self.address = addr
               
    def get_address(self):
        return self.address
    
    def record_transaction(self, tran_type, amount):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{timestamp} | {tran_type}: £{amount}")
    
    def deposit(self, amount):
        try:
            amount = float(amount)
        except:
            print("\nDeposit failed. Amount must be a number.")
            return
        
        if amount <= 0:
            print("\nInvalid deposit amount. Try again.")
            return
        
        self.balance += amount
        self.record_transaction("Deposit", amount) 
        
    def withdraw(self, amount):
        try:
            amount = float(amount)
        except:
                print("\nInvalid withdrawal amount.")
                return
         
        if amount <= 0:          
            print("\nInvalid withdrawal amount.")
            return

        if self.account_type == "advanced":
            if self.balance - amount < -self.overdraft_limit:
                print("\nOverdraft limit exceeded! Withdrawal denied.")
                return

            self.balance -= amount
            self.record_transaction("Withdraw", amount)
            print("\nWithdrawal successful (advanced account).")
            return
            
        if amount > self.balance:
            print("\nInsufficient funds! Withdrawal denied.")
        else:   
            self.balance -= amount
            self.record_transaction("Withdraw", amount)
            print("\nWithdrawal successful.")
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def set_account_type(self, acc_type):
        if acc_type in ["regular", "savings", "advanced"]:
            self.account_type = acc_type
        else:
            print("\nInvalid account type.")

    def set_overdraft_limit(self, limit):
        try:
            self.overdraft_limit = float(limit)
        except:
            print("\nInvalid overdraft limit. Set to 0.")
            self.overdraft_limit = 0.0

    def set_interest_rate(self, rate):
        try:
            self.interest_rate = float(rate)
        except:
            print("\nInvalid interest rate. Set to 0.")
            self.interest_rate = 0.0
            
    def calculate_yearly_interest(self):
        if self.account_type == "savings":
            return (self.balance * self.interest_rate) / 100
        return 0.0 
      
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        
        try:
            option = int(input ("Choose your option: "))
        
        except ValueError:
            print("\nInvalid inpuy. Please enter a number from 1-7.")
            return -1
        
        return option
    
    def print_details(self):
        #STEP A.4.3
        print("First name: %s" % self.fname)
        print("Last name: %s" % self.lname)
        print("Account No: %s" % self.account_no)
        print("Balance: £%.2f" % self.balance)

        print("Address:")
        for line in self.address:
            print("   ", line)

        print("Account Type:", self.account_type)

        if self.account_type == "advanced":
            print("Overdraft Limit: £%.2f" % self.overdraft_limit)

        if self.account_type == "savings":
            print("Interest Rate: %.2f%%" % self.interest_rate)

        print(" ")

    def show_transactions(self):
        print("\n--- Transaction History ---")
        if len(self.transactions) == 0:
            print("No transactions recorded.")
            return

        for t in self.transactions:
            print(t)
        print("---------------------------")

    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()

            if choice == 1:
                amt = input("\nEnter amount to deposit: ")
                self.deposit(amt)
                self.print_balance()

            elif choice == 2:
                amt = input("\nEnter amount to withdraw: ")
                self.withdraw(amt)
                self.print_balance()

            elif choice == 3:
                self.print_balance()
                
            elif choice == 4:
                fname = input("\nEnter new first name: ")
                self.update_first_name(fname)

                lname = input("Enter new last name: ")
                self.update_last_name(lname)

            elif choice == 5:
                print("\nEnter new address:")
                line1 = input("Address line 1: ")
                line2 = input("Address line 2: ")
                line3 = input("Address line 3: ")
                line4 = input("Address line 4: ")

                self.update_address([line1, line2, line3, line4])
                print("\nAddress updated.")

            elif choice == 6:
                self.print_details()

            elif choice == 7:
                return
            
            else:
                print("\nInvalid choice. Please select from 1–8.")

        print("\nExit account operations")   