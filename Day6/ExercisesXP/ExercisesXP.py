
#Exercise 1 : Hello World

print("Hello world\nHello world\nHello world\nHello world")



#Exercise 2 : Some Math
#Write code that calculates the result of: (99^3) * 8 (99 to the power of 3 times 8)

x = pow(99, 3) *8
print(x)


'''
#Exercise 3

5 < 3 #False
3 == 3 #True
3 == "3" #False
"3" > 3 #Error
"Hello" == "hello" #False
'''


#Exercise 4 : Your Computer Brand
computer_brand = "HP"
print(f"I have a {computer_brand} computer") 


#Exercise 5 : Your Information

name = "Nabeelah"
age = 26
shoe_size = 38
info = (" Hello, my name is {0}. I am {1} years old. My shoe size is {2} and I am a creative person.".format(name,age,shoe_size))
print(info)


#Exercise 6 : A & B

a = 10
b = 5

if a > b:
    print("Hello World")



#Exercise 7 : Odd Or Even
#Write code that asks the user for a number and determines whether this number is odd or even.
num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")



#Exercise 8 : What’s Your Name ?
user_name = (str(input("Enter your name: "))).capitalize()
my_name = "Nabeelah"
if user_name ==my_name:
    print("Hello Copycat, glad to know you")
else: 
    print (f'Hello {user_name}')


#Exercise 9 : Tall Enough To Ride A Roller Coaster

user_height_inches = int(input("Enter your height(inches): "))
user_height_cm = user_height_inches * 2.54
if user_height_cm > 145:
    print("You are tall enough to ride. ")
else:
    print("You need to grow some more to ride.")


  
