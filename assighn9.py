
# 9-1

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves wonderful {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open! Welcome!")
restaurant = Restaurant("crab shack", "Seafood")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
# 9-2
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves wonderful {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open! Welcome!")
restaurant1 = Restaurant("crab shack", "Seafood")
restaurant2 = Restaurant("tonys", "Italian")
restaurant3 = Restaurant("pizza bros", "pizza")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
# 9-3
class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        """Prints a summary of the user's information."""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back!")
user1 = User("robby", "Johnson", 20, "virginia", "robby.j@addr.com")
user2 = User("riley", "winchell", 19, "colorado", "riley.w@addr.com")
user3 = User("brice", "Micheals", 20, "maryland", "brice.m@addr.com")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
# 9-4recieved Help

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves wonderful {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open! Welcome!")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, additional_customers):
        """Increment the number of customers served by a given amount."""
        if additional_customers > 0:
            self.number_served += additional_customers
        else:
            print("Increment must be a positive number.")

restaurant = Restaurant("crab shack", "Seafood")

# Print the number of customers served (default)
print(f"Customers served: {restaurant.number_served}")

# 9-5

class User:
    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0  

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting."""
        print(f"Hello, {self.first_name}! Welcome back!")

    def increment_login_attempts(self):
        """Increase the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0

user = User("robby", "Johnson", 20, "virginia", "robby.j@addr.com")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")
# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "rocky road", "Cookie dough"]
    def display_flavors(self):
        """Display the list of ice cream flavors."""
        print(f"\n{self.restaurant_name} offers the following ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
ice_cream_stand = IceCreamStand("Frosty Delights")
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
# 9-7
class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = ["can add post",
            "can delete post",
            "can ban user",
            "can modify settings" ]

    def show_privileges(self):
        """Display the administrator's privileges."""
        print(f"\nAdministrator Privileges for {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")
admin_user = Admin("Emma", "bryer", 19, "Los Angeles", "emma.admin@example.com")
admin_user.describe_user()
admin_user.show_privileges()
# 9-8
class Privileges:
    def __init__(self, privileges=None):
        """Initialize the privileges attribute."""
        if privileges is None:
            privileges = [  "can add post",
                "can delete post",
                "can ban user",
                "can modify settings" ]
        self.privileges = privileges

    def show_privileges(self):
        """Display the administrator's privileges."""
        print("\nAdministrator Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges()

admin_user = Admin("joe", "Bro", 40, "new york city", "joe.admin@example.com")

admin_user.describe_user()
admin_user.privileges.show_privileges()
# 9-9
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You must add positive miles!")
class Battery:
    def __init__(self, battery_size=40):

        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh!")
        else:
            print("Battery is already upgraded.")
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() 
my_tesla = ElectricCar('tesla', 'model 3', 2024)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
