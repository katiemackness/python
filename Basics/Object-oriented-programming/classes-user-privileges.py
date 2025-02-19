# Katie mackness
# 28/06/24
# Chapter 9 exercises

class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def define_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")

    def greet_user(self):
        print(f"Hello, {self.first_name}. Welcome!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self, 
                 privileges=["can add post", "can ban user", "can create group"]):
        self.privileges = privileges

    def show_privileges(self):
        print("User privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name,age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()


rhonda = User("Rhonda", "Willis", 56, "Kabul")
terry = User("Terry", "Dillis", 23, "Timbuktu")
sherry = User("Sherry", "Daniels", 100, "New York")

admin = Admin("Bhonda", "Billis", 56, "Kabul")
admin.privileges.show_privileges()


