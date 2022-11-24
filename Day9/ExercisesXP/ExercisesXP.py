#Exercise 1 : What Are You Learning ?
def display_message():
    msg = "I'm learning javascript and python"
    print(msg)

display_message()

#Exercise 2: What’s Your Favorite Book ?
'''
Write a function called favorite_book() that accepts one parameter called title.
The function should print a message, such as "One of my favorite books is <title>".
For example: “One of my favorite books is Alice in Wonderland”
Call the function, make sure to include a book title as an argument when calling the function.
'''
def favorite_book(title):
    print(title + " is one of my favorite books.")


favorite_book('365 Quotes')


#Exercise 3 : Some Geography
'''
Write a function called describe_city() that accepts the name of a city and its country as parameters.
The function should print a simple sentence, such as "<city> is in <country>".
For example “Reykjavik is in Iceland”
Give the country parameter a default value.
Call your function.
'''

def describe_city(city, country='Canada'):
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Paris', 'France')
describe_city('Toronto')


#Exercise 4 : Random
'''
Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
'''
import random

while True:
    number = int(input("Enter a number between 1 to 100: "))
    if number >0 and number <101:
        break

random_number = random.randint(0,100)

if number == random_number:
    print("Yaaay!!! It's a match")
else:
    print("Booooh!!! Better luck next time")

print("The number you entered is: ", number)
print("Random number generated is: " , random_number)


#Exercise 5 : Let’s Create Some Personalized Shirts !
'''
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
Call the function make_shirt().

Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
Make a large shirt with the default message
Make medium shirt with the default message
Make a shirt of any size with a different message.

Bonus: Call the function make_shirt() using keyword arguments.
'''

def make_shirt(size='large', message='I love Python!'):
    print("\nI'm going to make a " + size + " t-shirt.")
    print('It will say, "' + message + '"')


make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Stay young, wild and free')


#Exercise 6 : Magicians …
'''
Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
Pass the list to a function called show_magicians(), which prints the name of each magician in the list.

Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
Call the function make_great().
Call the function show_magicians() to see that the list has actually been modified.
'''

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magician_names):
    for magician in magician_names:
        print(magician.title())

show_magicians(magician_names)


def make_great(magician_names):
    great_magicians_list = []

    while magician_names:
        new_magician = magician_names.pop()
        great_magician = (new_magician + " the Great")
        great_magicians_list.append(great_magician)

    for great_magician in great_magicians_list:
        magician_names.append(great_magician)


print("\n")
make_great(magician_names)
show_magicians(magician_names)


#Exercise 7 : Temperature Advice

import random

def get_random_temp():
    return random.randrange(-10,40)
function = [get_random_temp() for i in range(5)]

print(function)


def main():
    temperature = get_random_temp()
    print(f"La temperature is {temperature}°C")
    if(temperature < 0):
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif (temperature > 0 and temperature <= 16):
        print("Quite chilly! Don’t forget your coat")
    elif (temperature > 16 and temperature <= 23):
        print("The temp is good enough")
    elif (temperature > 24 and temperature <= 32):
        print(" Its warm enough")
    elif (temperature > 30 and temperature <= 40):
        print("It is  hot")
main()

def get_random_temp(season):
    if season == "Summer":
        return random.randrange(-10,16)
    if season == "autumn":
        return random.randrange(16,23)
    if season == "Winter":
        return random.randrange(24,32)
    if season == "Spring":
        return random.randrange(33,40)
    else:
        return random.randrange(-10,40)

def main():
    season = input("Type in a season - ‘summer’, ‘autumn’, ‘winter' or ‘spring’ : ")
    temperature = get_random_temp(season)
    if(temperature < 0):
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif (temperature > 0 and temperature <= 16):
        print("Quite chilly! Don’t forget your coat")
    elif (temperature > 16 and temperature <= 23):
        print("The temp is good enough")
    elif (temperature > 24 and temperature <= 32):
        print("The temp is warm")
    elif (temperature > 30 and temperature <= 40):
        print("It is  hot")

main()