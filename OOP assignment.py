class Staff:
    def __init__(self, s_name, access_code):
        self.s_name = s_name          
        self.__access_code = None     
        self.access_code = access_code  

    # Getter method using @property
    @property
    def access_code(self):
        """View the access code (authorized users only simulated here)"""
       
        return self.__access_code

    # Setter method using @access_code.setter
    @access_code.setter
    def access_code(self, new_code):
        """Update the access code after validating its length"""
        # Validating length  
        if len(str(new_code)) >= 4:
            self.__access_code = new_code
            print(f"[Success] Access code for {self.s_name} updated successfully.")
        else:
            print("[Error] Access code is too short! It must be at least 4 characters long.")

    # Method to display staff information
    def display_staff_info(self):
        """Display staff information"""
        print(f"\n--- Staff Details ---")
        print(f"Staff Name : {self.s_name}")
        print(f"Access Code: {self.access_code}")
        print(f"---------------------")


# --- Testing the Implementation ---

# 1. Create a new staff member with a valid code
staff1 = Staff("Kwaku Mensah", "98765")

# 2. Display staff information
staff1.display_staff_info()

# 3. Try to update with too short or invalide access code
staff1.access_code = "12" 

# 4. Update with a valid access code
staff1.access_code = "43210A"

# 5. Display staff info again to see the changes
staff1.display_staff_info()
