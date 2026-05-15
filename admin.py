class Admin:
    
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
        
        self.login_attempts = 0
        self.last_login = None
        self.activity_log = []
    
    def update_first_name(self, fname):
        try:
            if fname.strip() == "":
                print("\nInvalid first name.")
                return
            self.fname = fname
        except:
            print("\nError updating first name.")
    
    def update_last_name(self, lname):
        try:
            if lname.strip() == "":
                print("\nInvalid last name.")
                return
            self.lname = lname
        except:
            print("\nError updating last name.")
                        
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        try:
            if not isinstance(addr, list) or len(addr) != 4:
                print("\nInvalid address format.")
                return
            self.address = addr
            self.record_action("Updated address")
        except:
            print("\nError updating address.")
          
    def set_username(self, uname):
        try:
            if uname.strip() == "":
                print("\nInvalid username.")
                return
            self.user_name = uname
            self.record_action("Updated username")
        except:
            print("\nError updating username.")
        
    def get_username(self):
        return self.user_name
        
    def get_address(self):
        return self.address      
    
    def update_password(self, password):
        try:
            if not isinstance(password, str):
                print("\nPassword must be a string.")
                return
            if len(password) < 4:
                print("\nPassword too short. Must be at least 4 characters.")
                return
            self.password = password
            self.record_action("Updated password")
        except:
            print("\nError updating password.")
    
    def get_password(self):
        return self.password
    
    def set_full_admin_right(self, admin_right):
        try:
            if not isinstance(admin_right, bool):
                print("\nAdmin rights must be True/False.")
                return
            self.full_admin_rights = admin_right
            self.record_action(f"Admin rights changed to: {admin_right}")
        except:
            print("\nError updating admin rights.")
            
    def has_full_admin_right(self):
        return self.full_admin_rights
    
    def record_login_attempt(self, success):
        """Track login attempts and update last successful login."""
        try:
           import datetime
           self.login_attempts += 1
        
           if success:
              self.last_login = datetime.datetime.now()
              self.record_action("Successful login")  
           else:
              self.record_action("Failed login attempt")
        except:
            print("\nError recording login attempt.")     
            
    def record_action(self, action):
        """store admin activity for management reports."""
        try:
           import datetime
           timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           self.activity_log.append(f"{timestamp}: {action}")
        except:
            print("\nError logging admin action.")
            
    def print_admin_summary(self):
        """print a profile summary for administrators."""
        try:
           print("\n--- ADMIN PROFILE SUMMARY ---")
           print("\n--- ADMIN PROFILE SUMMARY ---")
           print("Name: %s %s" % (self.fname, self.lname))
           print("Username:", self.user_name)
           print("Full Admin Rights:", "Yes" if self.full_admin_rights else "No")
           print("Address:")
           for line in self.address:
              print(" ", line)
           print("Login Attempts:", self.login_attempts)
           print("Last Login:", self.last_login)
           print("Total Actions Logged:", len(self.activity_log))
           print("----------------------------------")
        except:
           print("\nError printing admin profile summary.") 
