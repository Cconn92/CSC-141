# 3.1
names = ['ted', 'Bob', 'Charles', 'riley']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
for name in names:
    print(name)
# 3.2
names = ['ted', 'Bob', 'Charles', 'riley']

print(f"Hello, {names[0]}! good morning!")
print(f"Hello, {names[1]}! good evening!")
print(f"Hello, {names[2]}! good afternoon!")
print(f"Hello, {names[3]}! good night!")
#3.3
motorcycles = ['Harley-Davidson', 'Ducati']
print(f"I would like to own a {motorcycles[0]} motorcycle.")
print(f"I would like to ride a {motorcycles[1]} on the highway.")
#3.4
names = ['Jay Z', 'Elon Musk', 'Lebron']
print(f"Hello, {names[0]}, would you like to go to dinner?")
print(f"Hello, {names[1]}, would you like to go to dinner?")
print(f"Hello, {names[2]}, would you like to go to dinner?")
#3.5 Recieved Example
guest_list = ['Jay Z', 'Elon Musk', 'Lebron']
for guest in guest_list:
    print(f"Dear {guest}, would you like to go to dinner?")
unable_to_attend = guest_list[2]
print(f"\nUnfortunately, {unable_to_attend} can't make it to the dinner.")
guest_list[2] = 'Nikola Tesla'
print("\nUpdated Guest List Invitations:")
for guest in guest_list:
    print(f"Dear {guest}, you are still invited to dinner at my place!")
#3.6
guest_list = ['Jay Z', 'Elon Musk', 'Lebron']
print("found a bigger table!")
guest_list.insert(0, "Lamar Jackson")
guest_list.insert(1,"Tom Brady")
print("\nUpdated Guest List Invitations:")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to dinner at my place!")
#3.7
print("the dinner table got smaller")
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner this time.")
    print("\nGuests still invited:")
for guest in guest_list:
    print(f"{guest}, you're still invited to dinner!")
del guest_list[0]
del guest_list[0]
#3.8
places_list = ['florida', 'arizona']
print(places_list)
print(sorted(places_list))
print(sorted(places_list, reverse=True))
places_list.reverse()
print(places_list)
#3.9
guest_list = ['Lamar Jackson', 'lebron']
print(f"\nNumber of people invited to dinner: {len(guest_list)}")
#3.10 recieved example
languages = ['Python', 'JavaScript', 'C++']
print(languages)
print("\nFirst language in the list:", languages[0])
print("Last language in the list:", languages[-1])
languages.append('Swift')
print(languages)
languages.insert(2, 'TypeScript')
print(languages)
del languages[3]
print(languages)
popped_language = languages.pop()
print(languages)
languages.remove('JavaScript')
print(languages)
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
print(sorted(languages))
languages.reverse()
print(languages)
print("\nNumber of programming languages in the list:", len(languages))
#3.11
#i revevied an index error in 3.10 trying to pop and item that was not there.