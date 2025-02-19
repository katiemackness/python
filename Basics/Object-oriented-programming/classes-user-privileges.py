# Katie Mackness
# 28/06/24 - Updated 19/02/2025

# --------------------------------------------------------
# Object-oriented programming - Classes and Instances
# --------------------------------------------------------

# This model creates a user and admin class.
# The admin class has a privileges class that is a list of privileges that the admin has. 
# The admin class has a method that displays the privileges of the admin.
class User:
    """Model of a user"""
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def define_user(self):
        """Describes user"""
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

    def greet_user(self):
        """Greets the user"""
        print(f"Hello, {self.first_name}. Welcome!")

    def increment_login_attempts(self):
        """Increments the login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the login attempts to 0"""
        self.login_attempts = 0

class Privileges:
    """Model of privileges"""
    def __init__(self, 
                 privileges=["can add post", "can ban user", "can create group"]):
        self.privileges = privileges

    def show_privileges(self):
        """Displays privileges of the user"""
        print("User privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """Model of an admin"""
    def __init__(self, first_name, last_name,age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()


# Examples creating new users and admins
rhonda = User("Rhonda", "Willis", 56, "Kabul")
terry = User("Terry", "Dillis", 23, "Timbuktu")
sherry = User("Sherry", "Daniels", 100, "New York")

admin = Admin("Bhonda", "Billis", 56, "Kabul")
admin.privileges.show_privileges()


