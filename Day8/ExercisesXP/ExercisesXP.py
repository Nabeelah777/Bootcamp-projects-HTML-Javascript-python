#ExercisesXP
#Exercise 1 : Convert Lists Into Dictionaries

num_keys = ['Ten', 'Twenty', 'Thirty']
num_values = [10, 20, 30]

# using zip()
res = dict(zip(num_keys, num_values))
print("Resultant dictionary is : " + str(res))



#Exercise 2 : Cinemax
'''
list_name = []
list_age = []
while True:
    name = str(input("Please enter your name! (type quit when done)?"))
    list_name.append(name)
    age = str(input("Please enter your age! (type quit when done)?"))
    list_age.append(age)
    if name and age == 'quit':
        break

list_name.remove("quit")
list_age.remove("quit")
new_age_list = list(map(int, list_age))
family = dict(zip(list_name, new_age_list))
print(family)
cost = 0

for name, age in family.items():
    
    if age < 3:
        print(name + " ticket is free")
    elif age < 12:
        print(name + " ticket is $10") 
        cost = cost + 10
    else:
        print(name + " ticket is $15")
        cost = cost + 15
  
print("Your total cost is $", cost)

'''

#Exercise 3: Zara
'''
name: Zara 
creation_date: 1975 
creator_name: Amancio Ortega Gaona 
type_of_clothes: men, women, children, home 
international_competitors: Gap, H&M, Benetton 
number_stores: 7000 
major_color: 
    France: blue, 
    Spain: red, 
    US: pink, green
'''

brand = {
  'name': 'Zara',
  'creation_date': 1975,
  'creator_name': 'Amancio Ortega Gaona',
  'type_of_clothes': ['men', 'women', 'children', 'home'],
  'international_competitors': ['Gap', 'H&M', 'Benetton'],
  'number_stores': 7000,
  'major_color': {
    'France': 'blue',
    'Spain': 'red',
    'US': ['pink', 'green']
  }
}
print(brand)
print('\n')

#3. Change the number of stores to 2.
brand["number_stores"] = 2
print(brand)
print('\n')

#4. Print a sentence that explains who Zaras clients are.

#5. Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"
print(brand)
print('\n')

#6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
    print(brand)
print('\n')

#7. Delete the information about the date of creation.
brand.pop("creation_date")
print(brand)
print('\n')

#8. Print the last international competitor.
InternationalCompetitors = list(brand.get("international_competitors"))
print("The last international competitor is: "  + InternationalCompetitors[-1])


#9. Print the major clothes colors in the US.
print(brand["major_color"])

A = list(brand["major_color"]['US'])
print(', '.join(A))
print(*A)

#10 Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))

#11 Print the keys of the dictionary.
print(brand.keys())

#12 Create another dictionary called more_on_zara with the following details:
more_on_zara = {
     "creation_date": 1975, 
     "number_stores": 10000,
}

#13 Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)

#14 Print the value of the key number_stores. What just happened ?
print(brand ['number_stores'])



#Exercise 4: Disney Characters
disney_users_A={}
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
for count, value in enumerate(users):
     if ("i" in value) == False:
         disney_users_A[value]=count
         print("works")
     else: continue
print(disney_users_A)

disney_users_A={}
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
for count, value in enumerate(users):
     if ((value.startswith("M")) or (value.startswith("P")))==0:
         disney_users_A[value]=count
print(disney_users_A)



