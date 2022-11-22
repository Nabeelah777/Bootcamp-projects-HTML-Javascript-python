#Exercise 1 : Set
my_fav_numbers = set((1,4,6,8,3,5))
my_fav_numbers.add(2)
my_fav_numbers.add(5)
print(my_fav_numbers)
my_fav_numbers.remove(8)
print(my_fav_numbers)
friend_fav_numbers = set((11,2,14,5,7,8))
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


#Exercise 2: Tuple
#Given a tuple which value is integers, is it possible to add more integers to the tuple?
#No,Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.


#Exercise 3: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)
basket.remove("Blueberries")
print(basket)
basket.append('Kiwi')
print(basket)
basket.insert(0, 'Apples')
print(basket)
apples = basket.count("Apples")
print(apples)
basket.clear()
print(basket)


#Exercise 4: Floats
#1 An integer is a whole number and a floating-point value, or float, is a number that has a decimal place.

xs = (x * 0.5 for x in range(3,11))
for x in xs:
   print(x)

#Exercise 5: For Loop
#1
for i in range(1,21):
    print (f'{i}' , end=' ')

#2
for y in range(2,21) :
    if y % 2 == 0 :
        print (y)



#Exercise 6 : While Loop
#Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
password = ''
while password != 'Nabeelah':
  password = (str(input("What's your name? "))).capitalize()
print('Hello Nabeelah!')



#Exercise 7: Favorite Fruits
fav_fruit = list(map(str, input("Enter your favorite fruits leaving space between each: ").split()))
print("List of favorite fruits: ", fav_fruit)

any_fruit = str(input("Name a fruit: "))

if any_fruit in fav_fruit:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')



#Exercise 8: Who Ordered A Pizza ?
price = 10
list = []
while True:
    topping = str(input("What topping would you like on your pizza (type quit when done)?"))
    list.append(topping)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        list.pop((len(list) -1))
        price = price + (len(list) * 2.5)
        for i in range(0,(len(list))):
            x = list[i]
            print(f'{x}' , end=', ')
        break

print("Your total price is $", price )


#Exercise 9: Cinemax
#1,2,3 
cost = 0
while True:
    age = input("How old are you? \nEnter 'quit' when you are finished. ")
    if age == "quit":
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free")
    elif age < 12:
        print("Your ticket is $10") 
        cost = cost + 10
    else:
        print("Your ticket is $15")
        cost = cost + 15
    
print("Your total cost is $", cost) 
 

#4
names= ["ouioui", "sarah", "Tom", "Jerry"]

for i in range(0,(len(names))):
    age = input("How old are you? \nEnter 'quit' when you are finished. ")
    if age == "quit":
        break
    age = int(age)
    if age < 16:
        names.pop(i-1)

print(names)



#Exercise 10 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
print()
for finished_sandwich in finished_sandwiches:
    print(" I made your " + finished_sandwich)



#Exercise 11 : Sandwich Orders#2
sandwich_orders = [
    'Pastrami sandwich', 'Tuna sandwich', 'Pastrami sandwich', 'Avocado sandwich',
    'Egg sandwich', 'Pastrami sandwich', 'Sabih sandwich']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'Pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print("I made a " + sandwich)

