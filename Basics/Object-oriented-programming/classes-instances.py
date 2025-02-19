# Katie Mackness
# 28/06/24 - Updated 19/02/2025

# --------------------------------------------------------
# Object-oriented programming - Classes and Instances
# --------------------------------------------------------

class Restaurant:
    """Simple model for a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Tells the restaurant and what it serves"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Tells that the restaurant is open"""
        print(f"{self.restaurant_name} is now open!")

    def give_number_served(self):
        """Gives the number of customers served."""
        print(
            f"{self.restaurant_name} has served {self.number_served} customers."
            )
    
    def set_number_served(self, number):
        """Change the number of customers"""
        self.number_served = number

    def increment_number_served(self, number):
        """Increase the number served by the given amount"""
        self.number_served += number

class IceCreamStand(Restaurant):
    """A basic attempt at describing an ice cream stand."""
    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['strawberry', 'chocolate', 'vanilla']

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

restaurant = IceCreamStand("Roberta's Ice Cream")
restaurant.describe_restaurant()
restaurant.display_flavors()