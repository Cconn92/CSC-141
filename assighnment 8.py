#8-1
def display_message():
    print("I'm learning about functions.")
display_message()
#8-2
def favorite_book(title):
    print(f"my favorite books is {title}.")
favorite_book("Python Crash Course")
#8-3
def make_shirt(size, message):
    print(f"Making a size {size} T-shirt with the message: '{message}' printed on it.")

make_shirt("Medium", "Keep Calm and Code On")

make_shirt(message="Hello, World!", size="Large")
#8-4
def make_shirt(size="Large", message="I love Python"):
    print(f"Making a size {size} T-shirt with the message: '{message}' printed on it.")

make_shirt()
make_shirt(size="Medium")
make_shirt("Small", "Code every day") 
#8-5
def describe_city(city, country="USA"):
    print(f"{city} is in {country}.")
describe_city("baltimore")
describe_city("detriot")
describe_city("tokyo")
#8-6
def city_country(city, country):
    return f"{city}, {country}"
print(city_country("Santiago", "Chile"))
print(city_country("Tokyo", "Japan"))
print(city_country("Paris", "France"))
#8-7
def make_album(artist, title, songs=None):
    album = { 'artist': artist,
        'title': title }
    if songs is not None:
        album['songs'] = songs
    return album

album1 = make_album("Travis scott", "astroworld")
album2 = make_album("lil uzi vert", "eternal atake")
album3 = make_album("kanye west", "graduation")

print(album1)
print(album2)
print(album3)

album4 = make_album("Drake", "views", songs=20)
print(album4)
#8-8
def make_album(artist, title, songs=None):
    album = { 'artist': artist,
        'title': title }
    if songs:
        album['songs'] = songs
    return album

print("\nEnter 'q' at any time to quit.")

#while True:
    #artist = input("Enter the artist's name: ")
    #if artist.lower() == 'q':
     #   break

    #title = input("Enter the album title: ")
    #if title.lower() == 'q':
     #   break

    #songs_input = input("Enter the number of songs (or press Enter to skip): ")
    #if songs_input.lower() == 'q':
     #   break

    #if songs_input:
    #    album = make_album(artist, title, songs=int(songs_input))
    #else:
     #   album = make_album(artist, title)

    #print("Album created:", album)
#8-9
def show_messages(messages):
    for message in messages:
        print(message)

messages = ["Hi!", "how are you?", "we have a meeting later.", "text me later."]

show_messages(messages)
#8-10
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hi!", "how are you?", "we have a meeting later.", "text me later."]
sent_messages = []

send_messages(messages, sent_messages)

print("\nFinal Lists:")
print("Messages:", messages)
print("Sent Messages:", sent_messages)
#8-11
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

original_messages = ["Hi!", "how are you?", "we have a meeting later.", "text me later."]
sent_messages = []

send_messages(original_messages[:], sent_messages) 

print("\nOriginal Messages (should be unchanged):", original_messages)
print("Sent Messages:", sent_messages)
#8-12
def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('peanut butter', 'jelly')
make_sandwich('ham', 'cheese', 'pickles')
#8-13
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile( 'chris', 'connors',
    location='Reading',
    profession='student',
    hobby='football')

print(my_profile)
#8-14
def make_car(manufacturer, model, **options):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    for key, value in options.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)