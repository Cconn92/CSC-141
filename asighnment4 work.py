# 4.1
pizzas = ['pepperoni', 'cheese', 'deluxe']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("\nI really love pizza!")
# 4.2
animals = ['dog', 'cat', 'fish']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("\nAny of these animals would make a great pet!")
# 4.3
for number in range(0, 21):
    print(number)
# 4.4
numbers = list(range(0, 1000001))
#print(number)
#4.5
numbers = list(range(0, 1000001))
print("Min:", min(numbers))
print("Max:", max(numbers))
total = sum(numbers)
print("Sum:", total) 
#4.6
for number in range(1, 21, 2):
    print(number)
#4.7
for number in range(3, 31, 3):
    print(number)
#4.8
for number in range(1, 11):
    cube = number ** 3
    print(cube)
#4.9
cubes = [number ** 3 for number in range(1, 11)]
print(cubes)
# 4.10
pizzas = ['Pepperoni', 'Margarita', 'BBQ Chicken', 'Hawaiian', 'Veggie']
print("The first three items in the list are:")
print(pizzas[:3])
middle_index = len(pizzas) // 2  
print("\nThree items from the middle of the list are:")
print(pizzas[middle_index-1:middle_index+2])
print("\nThe last three items in the list are:")
print(pizzas[-3:])
#4.11
pizzas = ['Pepperoni', 'Margarita', 'BBQ Chicken']
friend_pizzas = pizzas[:]
pizzas.append('Hawaiian')
friend_pizzas.append('Veggie')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
#4.12
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
foods = ['Pizza', 'Sushi', 'Burgers', 'Pasta']
print("My favorite foods are:")
for food in foods:
    print(food)
friend_foods = ['Tacos', 'Salad', 'Pasta', 'Steak']
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
# 4.13
buffet_menu = ('Pizza', 'Sushi', 'Pasta', 'Burger', 'Salad')
print("The restaurant offers the following foods:")
for food in buffet_menu:
    print(food)
try:
    buffet_menu[1] = 'Tacos' 
except TypeError:
    print("\nYou can't modify a tuple!")
buffet_menu = ('Pizza', 'Tacos', 'Pasta', 'Steak', 'Fruit Salad')
print("\nThe updated menu includes the following foods:")
for food in buffet_menu:
    print(food)
#4.14
    def mypizzas():
        print("My Favorite Pizzas Are:")
pizzas = ['Pepperoni','Margarita','BBQChicken','Veggie']
for p in pizzas: print(p)

mypizzas()

