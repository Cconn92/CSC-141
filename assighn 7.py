#7.1
car = input("What rental car would you like? ")
print(f"Lets see if I can find you a {car}.")
#7.2
group_size = int(input("How many people are in your group? "))
if group_size > 8:
    print("You’ll have to wait for a table.")
else:
    print("Your table is ready.")
#7.3
number = int(input("Give me a number, hint something like 10: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
#7.4
while True:
    topping = input("Enter a pizza topping (or type 'quit' to stop): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")
#7.5
while True:
    age_input = input("Enter your age (or type 'quit' to exit): ")
    if age_input.lower() == 'quit':
        break
    age = int(age_input)
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"Your ticket cost is ${cost}.")
#7.6
age_input = ""
while age_input.lower() != 'quit':
    age_input = input("Enter your age (or 'quit' to stop): ")
    if age_input.lower() != 'quit':
        age = int(age_input)
        if age < 3:
            cost = 0
        elif age <= 12:
            cost = 10
        else:
            cost = 15
        print(f"Ticket cost: ${cost}")
#7.6-2
active = True
while active:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")
#7.6-3
while True:
    age_input = input("Enter your age (or 'quit' to exit): ")
    if age_input.lower() == 'quit':
        break
    age = int(age_input)
    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"Ticket cost: ${cost}")
#7.7 code has comment for the loop
#while True:
   # print("This loop will run forever. Press CTRL-C to stop.")
#7.8
sandwich_orders = ['italian', 'ham', 'turkey']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
#7.9
sandwich_orders = ['pastrami', 'italian', 'pastrami', 'ham']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches made (no pastrami):")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
#7.10
responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    vacation = input("If you could visit one place in the world, what would it be? ")

    responses[name] = vacation

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() != 'yes':
        polling_active = False

print("\n--- Poll Results ---")
for name, vacation in responses.items():
    print(f"{name.title()} would like to visit {vacation}.")
