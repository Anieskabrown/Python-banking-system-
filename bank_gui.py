import tkinter
from tkinter import messagebox
from bank_system import BankSystem
from customer_account import CustomerAccount  

class Bank_GUI:

    def __init__(self):
        
        # ---- main window ----
        self.mw = tkinter.Tk()
        self.mw.title("Python Bank System - GUI Version")

        # backend system
        self.bank = BankSystem()

        # start at login screen
        self.show_login_screen()

        tkinter.mainloop()

    #   UTILITY — CLEAR ALL FRAMES
    def clear_window(self):
        for widget in self.mw.winfo_children():
            widget.destroy()

    #   LOGIN
    def show_login_screen(self):
        self.clear_window()

        # create frames
        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame1 = tkinter.Frame(self.mw)
        self.mid_frame2 = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)

        # ----- TOP -----
        self.login_label = tkinter.Label(self.top_frame, text="Admin Login Panel", font=("Arial", 16))
        self.login_label.pack()

        # ----- MID 1 -----
        self.user_label = tkinter.Label(self.mid_frame1, text="Username:")
        self.user_entry = tkinter.Entry(self.mid_frame1, width=20)
        self.user_label.pack(side="left")
        self.user_entry.pack(side="left")

        # ----- MID 2 -----
        self.pass_label = tkinter.Label(self.mid_frame2, text="Password:")
        self.pass_entry = tkinter.Entry(self.mid_frame2, width=20, show="*")
        self.pass_label.pack(side="left")
        self.pass_entry.pack(side="left")

        # ----- BOTTOM -----
        self.login_button = tkinter.Button(self.bottom_frame, text="Login", command=self.process_login)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.mw.destroy)

        self.login_button.pack(side="left", padx=5)
        self.quit_button.pack(side="left", padx=5)

        # pack frames
        self.top_frame.pack(pady=10)
        self.mid_frame1.pack(pady=5)
        self.mid_frame2.pack(pady=5)
        self.bottom_frame.pack(pady=10)

    def process_login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()

        msg, admin_obj = self.bank.admin_login(username, password)

        if admin_obj is None or msg != "\nLogin successful":
            messagebox.showerror("Error", "Invalid login details.")
            return
        
        self.admin_obj = admin_obj
        self.show_dashboard()

    #   ADMIN DASHBOARD
    def show_dashboard(self):
        self.clear_window()

        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame1 = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)

        # ----- TOP -----
        welcome = f"Welcome Admin {self.admin_obj.get_first_name()} {self.admin_obj.get_last_name()}"
        self.welcome_label = tkinter.Label(self.top_frame, text=welcome, font=("Arial", 15))
        self.welcome_label.pack()

        # ----- MID -----
        # All options as buttons
        options = [
            ("Transfer Money", self.show_transfer_screen),
            ("Customer Operations", self.show_customer_ops_screen),
            ("Create New Customer", self.show_create_customer),
            ("Delete Customer", self.show_delete_customer),
            ("View All Customers", self.show_all_customers),
            ("Management Report", self.show_management_report),
            ("Logout", self.show_login_screen)
        ]

        for text, cmd in options:
            btn = tkinter.Button(self.mid_frame1, text=text, width=25, command=cmd)
            btn.pack(pady=3)

        # pack frames
        self.top_frame.pack(pady=10)
        self.mid_frame1.pack(pady=10)
        self.bottom_frame.pack()

    #   TRANSFER MONEY
    def show_transfer_screen(self):
        self.clear_window()

        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame1 = tkinter.Frame(self.mw)
        self.mid_frame2 = tkinter.Frame(self.mw)
        self.mid_frame3 = tkinter.Frame(self.mw)
        self.mid_frame4 = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)

        # ----- TOP -----
        tkinter.Label(self.top_frame, text="Transfer Money", font=("Arial", 16)).pack()

        # ----- MID FRAME 1 -----
        tkinter.Label(self.mid_frame1, text="Sender Last Name:").pack(side="left")
        self.sender_entry = tkinter.Entry(self.mid_frame1, width=20)
        self.sender_entry.pack(side="left")

        # ----- MID FRAME 2 -----
        tkinter.Label(self.mid_frame2, text="Receiver Last Name:").pack(side="left")
        self.receiver_entry = tkinter.Entry(self.mid_frame2, width=20)
        self.receiver_entry.pack(side="left")

        # ----- MID FRAME 3 -----
        tkinter.Label(self.mid_frame3, text="Receiver Account No:").pack(side="left")
        self.accno_entry = tkinter.Entry(self.mid_frame3, width=20)
        self.accno_entry.pack(side="left")

        # ----- MID FRAME 4 -----
        tkinter.Label(self.mid_frame4, text="Amount: £").pack(side="left")
        self.amount_entry = tkinter.Entry(self.mid_frame4, width=20)
        self.amount_entry.pack(side="left")

        # ----- BOTTOM -----
        tkinter.Button(self.bottom_frame, text="Transfer", command=self.do_transfer).pack(side="left", padx=5)
        tkinter.Button(self.bottom_frame, text="Back", command=self.show_dashboard).pack(side="left", padx=5)

        # pack frames
        self.top_frame.pack(pady=10)
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.mid_frame3.pack()
        self.mid_frame4.pack()
        self.bottom_frame.pack(pady=10)


    def do_transfer(self):
        s = self.sender_entry.get()
        r = self.receiver_entry.get()
        acc = self.accno_entry.get()
        amount = self.amount_entry.get()

        self.bank.transferMoney(s, r, acc, amount)
        messagebox.showinfo("Transfer", "Process Completed (see console for validation).")
        self.show_dashboard()

    #   CUSTOMER OPERATIONS
    def show_customer_ops_screen(self):
        self.clear_window()

        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame1 = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)

        tkinter.Label(self.top_frame, text="Customer Operations", font=("Arial", 16)).pack()

        tkinter.Label(self.mid_frame1, text="Customer Last Name:").pack(side="left")
        self.cust_lname_entry = tkinter.Entry(self.mid_frame1, width=20)
        self.cust_lname_entry.pack(side="left")

        tkinter.Button(self.bottom_frame, text="Load", command=self.load_customer).pack(side="left", padx=5)
        tkinter.Button(self.bottom_frame, text="Back", command=self.show_dashboard).pack(side="left", padx=5)

        self.top_frame.pack(pady=10)
        self.mid_frame1.pack(pady=10)
        self.bottom_frame.pack(pady=10)


    def load_customer(self):
        lname = self.cust_lname_entry.get()
        customer = self.bank.search_customers_by_name(lname)

        if customer is None:
            messagebox.showerror("Error", "Customer not found.")
        else:
            self.show_customer_menu(customer)

    #   CUSTOMER MENU
    def show_customer_menu(self, customer):
        self.clear_window()

        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame1 = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)

        tkinter.Label(
            self.top_frame,
            text=f"Customer: {customer.fname} {customer.lname}",
            font=("Arial", 16)
        ).pack()

        # Buttons
        tkinter.Button(self.mid_frame1, text="Deposit", width=25,
                       command=lambda: self.deposit_screen(customer)).pack(pady=3)

        tkinter.Button(self.mid_frame1, text="Withdraw", width=25,
                       command=lambda: self.withdraw_screen(customer)).pack(pady=3)

        tkinter.Button(self.mid_frame1, text="Update Name", width=25,
                       command=lambda: self.update_name_screen(customer)).pack(pady=3)

        tkinter.Button(self.mid_frame1, text="Update Address", width=25,
                       command=lambda: self.update_address_screen(customer)).pack(pady=3)

        tkinter.Button(self.mid_frame1, text="View Details", width=25,
                       command=lambda: self.show_customer_details(customer)).pack(pady=3)

        tkinter.Button(self.bottom_frame, text="Back", width=25, command=self.show_customer_ops_screen).pack(pady=3)

        self.top_frame.pack(pady=10)
        self.mid_frame1.pack(pady=10)
        self.bottom_frame.pack()

    #   DEPOSIT
    def deposit_screen(self, customer):
        self.clear_window()

        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame1 = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)

        tkinter.Label(self.top_frame, text="Deposit Money", font=("Arial", 16)).pack()

        tkinter.Label(self.mid_frame1, text="Amount £:").pack(side="left")
        amount_entry = tkinter.Entry(self.mid_frame1, width=20)
        amount_entry.pack(side="left")

        def deposit_action():
            try:
                amt = float(amount_entry.get())
                customer.deposit(amt)
                messagebox.showinfo("Success", "Deposit completed.")
            except:
                messagebox.showerror("Error", "Invalid amount")

        tkinter.Button(self.bottom_frame, text="Submit", command=deposit_action).pack(side="left")
        tkinter.Button(self.bottom_frame, text="Back", command=lambda: self.show_customer_menu(customer)).pack(side="left")

        self.top_frame.pack(pady=10)
        self.mid_frame1.pack(pady=10)
        self.bottom_frame.pack(pady=10)

    #   WITHDRAW
    def withdraw_screen(self, customer):
        self.clear_window()

        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame1 = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)

        tkinter.Label(self.top_frame, text="Withdraw Money", font=("Arial", 16)).pack()

        tkinter.Label(self.mid_frame1, text="Amount £:").pack(side="left")
        amount_entry = tkinter.Entry(self.mid_frame1, width=20)
        amount_entry.pack(side="left")

        def withdraw_action():
            try:
                amt = float(amount_entry.get())
                customer.withdraw(amt)
                messagebox.showinfo("Success", "Withdrawal completed.")
            except:
                messagebox.showerror("Error", "Invalid amount")

        tkinter.Button(self.bottom_frame, text="Submit", command=withdraw_action).pack(side="left")
        tkinter.Button(self.bottom_frame, text="Back", command=lambda: self.show_customer_menu(customer)).pack(side="left")

        self.top_frame.pack(pady=10)
        self.mid_frame1.pack(pady=10)
        self.bottom_frame.pack(pady=10)

    #   UPDATE NAME
    def update_name_screen(self, customer):
        self.clear_window()

        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame1 = tkinter.Frame(self.mw)
        self.mid_frame2 = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)

        tkinter.Label(self.top_frame, text="Update Name", font=("Arial", 16)).pack()

        tkinter.Label(self.mid_frame1, text="New First Name:").pack(side="left")
        fname_entry = tkinter.Entry(self.mid_frame1, width=20)
        fname_entry.pack(side="left")

        tkinter.Label(self.mid_frame2, text="New Last Name:").pack(side="left")
        lname_entry = tkinter.Entry(self.mid_frame2, width=20)
        lname_entry.pack(side="left")

        def update_action():
            customer.update_first_name(fname_entry.get())
            customer.update_last_name(lname_entry.get())
            messagebox.showinfo("Success", "Customer name updated.")

        tkinter.Button(self.bottom_frame, text="Submit", command=update_action).pack(side="left")
        tkinter.Button(self.bottom_frame, text="Back", command=lambda: self.show_customer_menu(customer)).pack(side="left")

        self.top_frame.pack(pady=10)
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.bottom_frame.pack(pady=10)

    #   UPDATE ADDRESS
    def update_address_screen(self, customer):
        self.clear_window()

        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame1 = tkinter.Frame(self.mw)
        self.mid_frame2 = tkinter.Frame(self.mw)
        self.mid_frame3 = tkinter.Frame(self.mw)
        self.mid_frame4 = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)

        tkinter.Label(self.top_frame, text="Update Address", font=("Arial", 16)).pack()

        address_entries = []

        for i, frame in enumerate([self.mid_frame1, self.mid_frame2, self.mid_frame3, self.mid_frame4]):
            tkinter.Label(frame, text=f"Line {i+1}:").pack(side="left")
            entry = tkinter.Entry(frame, width=20)
            entry.pack(side="left")
            address_entries.append(entry)

        def update_addr():
            new_address = [e.get() for e in address_entries]
            customer.update_address(new_address)
            messagebox.showinfo("Success", "Address updated.")

        tkinter.Button(self.bottom_frame, text="Submit", command=update_addr).pack(side="left")
        tkinter.Button(self.bottom_frame, text="Back", command=lambda: self.show_customer_menu(customer)).pack(side="left")

        self.top_frame.pack(pady=10)
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.mid_frame3.pack()
        self.mid_frame4.pack()
        self.bottom_frame.pack(pady=10)

    #   VIEW DETAILS
    def show_customer_details(self, customer):
        details = (
            f"Name: {customer.fname} {customer.lname}\n"
            f"Account Number: {customer.account_no}\n"
            f"Balance: £{customer.balance:.2f}\n"
            f"Account Type: {customer.account_type}\n"
        )
        messagebox.showinfo("Customer Details", details)

    #   CREATE CUSTOMER
    def show_create_customer(self):
        self.clear_window()

        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frames = []
        for _ in range(7):
            self.mid_frames.append(tkinter.Frame(self.mw))
        self.bottom_frame = tkinter.Frame(self.mw)

        tkinter.Label(self.top_frame, text="Create New Customer", font=("Arial", 16)).pack()

        labels = [
            "First Name", "Last Name",
            "Address Line 1", "Address Line 2",
            "Address Line 3", "Address Line 4",
            "Initial Balance"
        ]

        self.entries = []

        for i, lbl in enumerate(labels):
            tkinter.Label(self.mid_frames[i], text=lbl + ":").pack(side="left")
            entry = tkinter.Entry(self.mid_frames[i], width=20)
            entry.pack(side="left")
            self.entries.append(entry)

        def create_customer_action():
            try:
                fname = self.entries[0].get()
                lname = self.entries[1].get()
                address = [e.get() for e in self.entries[2:6]]
                balance = float(self.entries[6].get())

                new_acc_no = max([c.get_account_no() for c in self.bank.accounts_list]) + 1
                new_customer = CustomerAccount(fname, lname, address, new_acc_no, balance)

                self.bank.accounts_list.append(new_customer)
                messagebox.showinfo("Success", f"Account Created.\nAcc No: {new_acc_no}")
            except:
                messagebox.showerror("Error", "Invalid input.")

        tkinter.Button(self.bottom_frame, text="Create", command=create_customer_action).pack(side="left")
        tkinter.Button(self.bottom_frame, text="Back", command=self.show_dashboard).pack(side="left")

        self.top_frame.pack(pady=10)
        for frame in self.mid_frames:
            frame.pack()
        self.bottom_frame.pack(pady=10)

    #   DELETE CUSTOMER
    def show_delete_customer(self):
        self.clear_window()

        self.top_frame = tkinter.Frame(self.mw)
        self.mid_frame1 = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)

        tkinter.Label(self.top_frame, text="Delete Customer", font=("Arial", 16)).pack()

        tkinter.Label(self.mid_frame1, text="Customer Last Name:").pack(side="left")
        lname_entry = tkinter.Entry(self.mid_frame1, width=20)
        lname_entry.pack(side="left")

        def delete_action():
            if not self.admin_obj.has_full_admin_right():
                messagebox.showerror("Access Denied", "You do not have permission to delete customers.")
                return

            lname = lname_entry.get()
            customer = self.bank.search_customers_by_name(lname)

            if customer:
                self.bank.accounts_list.remove(customer)
                messagebox.showinfo("Deleted", "Customer removed successfully.")
            else:
                messagebox.showerror("Error", "Customer not found.")

        tkinter.Button(self.bottom_frame, text="Delete", command=delete_action).pack(side="left")
        tkinter.Button(self.bottom_frame, text="Back", command=self.show_dashboard).pack(side="left")

        self.top_frame.pack(pady=10)
        self.mid_frame1.pack(pady=10)
        self.bottom_frame.pack(pady=10)

    #   VIEW ALL CUSTOMERS
    def show_all_customers(self):
        customers = self.bank.accounts_list

        if not customers:
            messagebox.showinfo("Customers", "No customers found.")
            return

        text = ""
        for c in customers:
            text += f"{c.account_no} — {c.fname} {c.lname} — £{c.balance:.2f}\n"

        messagebox.showinfo("All Customers", text)

    #   MANAGEMENT REPORT
    def show_management_report(self):
        self.clear_window()

        self.top_frame = tkinter.Frame(self.mw)
        self.bottom_frame = tkinter.Frame(self.mw)

        tkinter.Label(self.top_frame, text="Management Report", font=("Arial", 16)).pack()

        total_customers = len(self.bank.accounts_list)
        total_balance = sum(c.get_balance() for c in self.bank.accounts_list)
        total_interest = sum(c.calculate_yearly_interest() for c in self.bank.accounts_list)

        total_overdraft_used = sum(
            abs(c.get_balance())
            for c in self.bank.accounts_list
            if c.account_type == "advanced" and c.get_balance() < 0
        )

        report = (
            f"Total Customers: {total_customers}\n"
            f"Total Balance: £{total_balance:.2f}\n"
            f"Total Overdraft Used: £{total_overdraft_used:.2f}\n"
            f"Total Interest Payable: £{total_interest:.2f}"
        )

        tkinter.Label(self.bottom_frame, text=report, font=("Arial", 12)).pack()

        tkinter.Button(self.bottom_frame, text="Back", command=self.show_dashboard).pack(pady=5)

        self.top_frame.pack(pady=10)
        self.bottom_frame.pack(pady=10)

# RUN GUI
if __name__ == "__main__":
    gui = Bank_GUI()
