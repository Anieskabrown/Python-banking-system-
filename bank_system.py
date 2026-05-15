from customer_account import CustomerAccount
from admin import Admin

accounts_list = []
admins_list = []


class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()

    def load_bank_data(self):

        # create customers
        account_no = 1234
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00)
        self.accounts_list.append(customer_1)

        account_no += 1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no,
                                     3200.00)
        self.accounts_list.append(customer_2)

        account_no += 1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no,
                                     18000.00)
        self.accounts_list.append(customer_3)

        account_no += 1
        customer_4 = CustomerAccount("Ali", "Abdallah", ["44", "Churchill Way West", "Basingstoke", "RG21 6YR"],
                                     account_no, 40.00)
        self.accounts_list.append(customer_4)

        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "id1188", "1441", True)
        self.admins_list.append(admin_1)

        admin_2 = Admin("Cathy", "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "id3313", "2442", False)
        self.admins_list.append(admin_2)

    def search_admins_by_name(self, admin_username):
        # STEP A.2
        found_admin = None
        for a in self.admins_list:
            username = a.get_username()
            if username == admin_username:
                found_admin = a
                break

        if found_admin is None:
            print("\nThe Admin %s does not exist! Try again...\n" % admin_username)

        return found_admin

    def search_customers_by_name(self, customer_lname):
        # STEP A.3
        found_customer = None
        for c in self.accounts_list:
            if c.get_last_name() == customer_lname:
                found_customer = c
                break

        if found_customer is None:
            print("\nThe customer with last name '%s' does not exist! Try again...\n" % customer_lname)

        return found_customer

    def search_customer_by_account_no(self, account_no):
        for c in self.accounts_list:
            if str(c.get_account_no()) == str(account_no):
                return c
        print("\nNo customer found with account number:", account_no)
        return None

    def admin_login(self, username, password):
        found_admin = self.search_admins_by_name(username)
        msg = "\nLogin failed"

        if found_admin is not None:
            if found_admin.get_password() == password:
                msg = "\nLogin successful"
            try:
                found_admin.record_login_attempt(True)
            except:
                pass

        else:
            try:
                found_admin.record_login_attempt(False)
            except:
                pass

        return msg, found_admin

    def main_menu(self):
        # print the options you have
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Welcome to the Python Bank System")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Admin login")
        print("2) Quit Python Bank System")
        print(" ")

        try:
            option = int(input("Choose your option: "))

        except ValueError:
            print("\nInvalid input. Enter a number.")
            return -1

        return option

    def run_main_options(self):
        loop = True
        while loop:
            choice = self.main_menu()

            if choice == 1:
                username = input("\n Please input admin username: ")
                password = input("\n Please input admin password: ")

                msg, admin_obj = self.admin_login(username, password)
                print(msg)

                if admin_obj is not None and msg == "\nLogin successful":
                    self.run_admin_options(admin_obj)

            elif choice == 2:
                loop = False
            else:
                print("\nInvalid choice. Try again.")

        print("\nThank-You for stopping by the bank!")

    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount):
        try:
            amount = float(amount)
        except:
            print("\nInvalid amount. Transaction cancelled.")
            return

        if amount <= 0:
            print("\nAmount must be positive.")
            return

        sender = self.search_customers_by_name(sender_lname)
        receiver = self.search_customers_by_name(receiver_lname)

        if sender is None or receiver is None:
            print("\nTransaction failed.")
            return

        if str(receiver.get_account_no()) != str(receiver_account_no):
            print("\nReceiver account number does not match.")
            return

        if sender.account_type == "regular" and sender.get_balance() < amount:
            print("\nSender does not have enough funds.")
            return

        sender.withdraw(amount)
        receiver.deposit(amount)

        print("\nTransfer successful.")
        print("Sender new balance: %.2f" % sender.get_balance())
        print("Receiver new balance: %.2f" % receiver.get_balance())

    def admin_menu(self, admin_obj):
        print("\nWelcome Admin %s %s : Available options are:" %
              (admin_obj.get_first_name(), admin_obj.get_last_name()))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1) Transfer money")
        print("2) Customer account operations & profile settings")
        print("3) Delete customer")
        print("4) Print all customers detail")
        print("5) Sign out")
        print("6) Update admin profile")
        print("7) Create new customer account")
        print("8) Management report")
        print("9) View admin details")
        print(" ")

        try:
            option = int(input("Choose your option: "))
        except ValueError:
            print("\nInvalid input. Enter a number.")
            return -1

        return option

    def run_admin_options(self, admin_obj):
        loop = True
        while loop:
            choice = self.admin_menu(admin_obj)

            if choice == 1:
                sender_lname = input("\n Please input sender surname: ")
                try:
                    amount = float(input("\nPlease input the amount to be transferred: "))
                except:
                    print("\nInvalid amount.")
                    continue

                receiver_lname = input("\n Please input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")

                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)

            elif choice == 2:
                customer_name = input("\nPlease input customer surname:\n")
                customer_account = self.search_customers_by_name(customer_name)

                if customer_account != None:
                    customer_account.run_account_options()

            elif choice == 3:
                if not admin_obj.has_full_admin_right():
                    print("\nAccess denied. You do not have permission to delete customers.")
                    continue

                lname = input("\nEnter surname of customer to delete: ")
                customer = self.search_customers_by_name(lname)

                if customer is not None:
                    self.accounts_list.remove(customer)
                    print("\nCustomer deleted successfully.")
                else:
                    print("\nCustomer not found.")

            elif choice == 4:
                self.print_all_accounts_details()

            elif choice == 5:
                loop = False

            elif choice == 6:
                print("\n--- Update Admin Profile ---")
                admin_obj.update_first_name(input("New first name: "))
                admin_obj.update_last_name(input("New last name: "))

                line1 = input("Address line 1: ")
                line2 = input("Address line 2: ")
                line3 = input("Address line 3: ")
                line4 = input("Address line 4: ")

                admin_obj.update_address([line1, line2, line3, line4])
                admin_obj.update_password(input("New password: "))
                print("\nAdmin profile updated.")

            elif choice == 7:
                print("\n--- Create New Customer Account ---")

                fname = input("First name: ")
                lname = input("Last name: ")

                line1 = input("Address line 1: ")
                line2 = input("Address line 2: ")
                line3 = input("Address line 3: ")
                line4 = input("Address line 4: ")

                try:
                    balance = float(input("Initial balance: "))
                except:
                    print("\nInvalid balance amount.")
                    continue

                print("\nSelect account type:")
                print("1) Regular")
                print("2) Savings")
                print("3) Advanced")
                acc_type = input("Choose: ")

                new_account_no = max([c.get_account_no() for c in self.accounts_list]) + 1
                new_customer = CustomerAccount(
                    fname, lname, [line1, line2, line3, line4], new_account_no, balance
                )

                if acc_type == "2":
                    try:
                        new_customer.account_type = "savings"
                        new_customer.interest_rate = float(input("Interest rate (%): "))
                    except:
                        print("\nInvalid interest rate. Set to 0%.")
                        new_customer.interest_rate = 0.0

                elif acc_type == "3":
                    try:
                        new_customer.account_type = "advanced"
                        new_customer.overdraft_limit = float(input("Overdraft limit: "))
                    except:
                        print("\nInvalid overdraft limit. Set to 0.")
                        new_customer.overdraft_limit = 0.0

                self.accounts_list.append(new_customer)
                print("\nCustomer created successfully. Account No:", new_account_no)

            elif choice == 8:
                self.generate_management_report()

            elif choice == 9:
                admin_obj.print_admin_summary()

            else:
                print("\nInvalid choice. Try again.")

        print("\nExiting admin panel.....")

    def print_all_accounts_details(self):
        i = 0
        for c in self.accounts_list:
            i += 1
            print('\n %d. ' % i, end=' ')
            c.print_details()
            print("------------------------")

    def generate_management_report(self):
        print("\n--- MANAGEMENT REPORT ---")

        total_customers = len(self.accounts_list)
        total_balance = sum(c.get_balance() for c in self.accounts_list)

        total_overdraft_used = sum(
            abs(c.get_balance())
            for c in self.accounts_list
            if c.account_type == "advanced" and c.get_balance() < 0
        )

        total_interest = sum(
            c.calculate_yearly_interest()
            for c in self.accounts_list
            if c.account_type == "savings"
        )

        print("Total customers:", total_customers)
        print("Total balance: £%.2f" % total_balance)
        print("Total overdraft used: £%.2f" % total_overdraft_used)
        print("Total yearly interest payable: £%.2f" % total_interest)
        print("----------------------------------")
        print (" ")


if __name__ == "__main__":
    app = BankSystem()
    app.run_main_options()