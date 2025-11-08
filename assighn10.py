#10-1
file_path = 'Learning_python.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print("Reading the entire file:\n")
print(contents)
print("\nReading line by line:\n")
with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())
#couldnt figure this out
#10-2
file_path = 'learning_python.txt'

with open(file_path) as file_object:
    for line in file_object:
        
        modified_line = line.replace('Python', 'C')
        print(modified_line.strip())
#10-3
with open(file_path) as file_object:
    for line in file_object:
        print(line.strip())
#10-4
filename = 'guest.txt'
name = input("What is your name? ")
with open(filename, 'w') as file_object:
    file_object.write(name)
print(f"Thanks, {name}. Your name has been written to {filename}.")
# 10-5
filename = 'guest_book.txt'
print("Enter 'quit' when you are done.\n")
while True:
    name = input("Please enter your name: ")
    if name.lower() == 'quit':
        print("Goodbye!")
        break
    else:
        print(f"Welcome, {name}!")
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
#10-6
print("Enter two numbers and I’ll add them together:")

try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
except ValueError:
    print("Sorry, you must enter numeric values only.")
else:
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")
#10-7
print("Enter two numbers to add (or 'q' to quit).")
while True:
    num1 = input("\nFirst number: ")
    if num1.lower() == 'q':
        break
    num2 = input("Second number: ")
    if num2.lower() == 'q':
        break
    try:
        sum_result = int(num1) + int(num2)
    except ValueError:
        print("Oops! Please enter valid numbers.")
    else:
        print(f"The sum of {num1} and {num2} is {sum_result}.")
#10-8
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} could not be found.")
    else:
        print(f"\nContents of {filename}:")
        print(contents.strip())
#10-9
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass  # fail silently
    else:
        print(f"\nContents of {filename}:")
        print(contents.strip())
#10-10
def count_word(frank.txt, the):
    try:
        with open(frank.txt, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {frank.txt} was not found.")
    else:
        word_count = contents.lower().count(word)
        print(f"'{word}' appears about {word_count} times in {frank.txt}.")
#10-11, recieved help didndt understand
import json

filename = 'favorite_number.json'
number = input("What is your favorite number? ")

with open(filename, 'w') as f:
    json.dump(number, f)

print("Thanks! I’ll remember that.")
#10-12
import json
filename = 'favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Thanks! I’ll remember that next time.")
else:
    print(f"I know your favorite number! It’s {number}.")
#10-13
import json
filename = 'user_info.json'
def get_new_user_info():
    """Prompt for user info and store it."""
    user_info = {}
    user_info['username'] = input("What is your name? ")
    user_info['age'] = input("How old are you? ")
    user_info['city'] = input("Which city do you live in? ")

    with open(filename, 'w') as f:
        json.dump(user_info, f)
    return user_info
def greet_user():
    """Load stored info and greet the user."""
    try:
        with open(filename) as f:
            user_info = json.load(f)
    except FileNotFoundError:
        user_info = get_new_user_info()
        print("Thanks! Your information has been saved.")
    else:
        print(f"\nWelcome back, {user_info['username']}!")
        print(f"You're {user_info['age']} years old and live in {user_info['city']}.")
greet_user()
#10-14
import json
filename = 'username.json'
def get_new_username():
    """Prompt for a new username and store it."""
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
def get_stored_username():
    """Get stored username if available."""
    try:
        with open(filename) as f:
            return json.load(f)
    except FileNotFoundError:
        return None
def greet_user():
    """Greet the user by name, verifying identity."""
    username = get_stored_username()
    if username:
        verify = input(f"Are you {username}? (yes/no): ")
        if verify.lower() == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We’ll remember you next time, {username}!")
    else:
        username = get_new_username()
        print(f"We’ll remember you next time, {username}!")
greet_user()
#all in all had alot of trouble didnt do alot of it right and i know some of the code doesnt work. i recieved help but i dont think alot was right.