# 6-1
person = {'first_name': 'chris',
    'last_name': 'Connors',
    'age': 20,
    'city': 'maryland'}
print(f"First Name: {person['first_name']}")
print(f"Last Name: {person['last_name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")
# 6-2
favorite_numbers = {'chris': 7,
    'riley': 42,
    'tim': 20,}
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
    # 6-3
glossary = { 'variable': 'store data values.',
    'function': 'A block of code.',
    'loop': 'A sequence  that is continually repeated until a certain condition is met.',
    'dictionary': 'A collection of words.',
    'list': 'A collection of items in order.'}
for word, meaning in glossary.items():
    print(f"{word}:\n  {meaning}\n")
# 6-4
glossary = {'variable': 'store data values.',
    'function': 'A block of code.',
    'loop': 'A sequence  that is continually repeated until a certain condition is met.',
    'dictionary': 'A collection of words.',
    'list': 'A collection of items in order.',
    'boolean': 'A data type that can be either True or False.',
    'if statement': 'A conditional statement used to make decisions in code.',
    'comment': 'Text in a program that is ignored by the interpreter but helps humans understand the code.',
    'indentation': 'Spacing at the beginning of a line of code, used to define blocks in Python.'}
for word, meaning in glossary.items():
    print(f"{word}:\n  {meaning}\n")
# 6-5
rivers = {'missisipi river': 'mississipi',
    'amazon river': 'brazil',
    'nile river': 'egypt'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(f"- {river.title()}")
print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(f"- {country.title()}")
# 6-6
favorite_languages = { 'james': 'python',
    'riley': 'java',
    'chris': 'c++',}
people_to_poll = ['james', 'riley', 'chris']
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our favorite programming language poll!")
# 6-7
person_1 = {'first_name': 'riley',
    'last_name': 'kay',
    'age': 19,
    'city': 'boulder'}
person_2 = {'first_name': 'chris' ,
   'last_name': 'Connors',
    'age': 20,
    'city': 'baltimore'}
person_3 = {'first_name': 'joesph',
    'last_name': 'coral',
    'age': 77,
    'city': 'atlantis'}
people = [person_1, person_2, person_3]
for person in people:
    print("\nPerson Info:")
    for key, value in person.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
# 6-8
pet_1 = {'animal': 'dog', 'owner': 'robert'}
pet_2 = {'animal': 'cat', 'owner': 'riley'}
pet_3 = {'animal': 'fish', 'owner': 'Chris'}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print("\nPet Info:")
    for key, value in pet.items():
        print(f"{key.title()}: {value}")
# 6-9
favorite_places = {'chris': ['colorado', 'maryland', 'wyoming'],
    'joseph': ['atlantis'],
    'riley': ['mexico', 'europe']}
for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")
# 6-10
favorite_numbers = { 'chris': [7, 3],
    'riley': [42],
    'joseph': [1, 0, 55],}
for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
# 6-11
cities = { 'New York': { 'country': 'america',
        'population': '8.5 million',
        'fact': 'buisy all day and night' },
    'boulder': {'country': 'america',
        'population': '106 thousand',
        'fact': 'home to deion sanders' },
    'maryland': {'country': 'america',
        'population': '6.2 million',
        'fact': 'home to chris connors'}}
for city, info in cities.items():
    print(f"\nCity: {city}")
    for key, value in info.items():
        print(f"{key.title()}: {value}")
# 6-12 (recieved an example on like two)
cities = { 'New York': { 'country': 'america',
        'population': '8.5 million',
        'fact': 'buisy all day and night',
        'founded': 1788  },
    'boulder': {'country': 'america',
        'population': '106 thousand',
        'fact': 'home to deion sanders',
        'founded': 1858 },
    'maryland': {'country': 'america',
        'population': '6.2 million',
        'fact': 'home to chris connors',
        'founded': 1788 }
        }
print(" City Information\n" + "="*20)
for city, info in cities.items():
    print(f"\n {city.upper()}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Founded: {info['founded']}")
    print(f"  Fact: {info['fact']}")