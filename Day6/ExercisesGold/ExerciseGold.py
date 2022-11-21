#Exercise 1 : Hello World-I Love Python

print(('" Hello world"\n')*4,('" I love python"\n')*4,sep = "")


#Exercise 2 : What Is The Season ?
'''Ask the user to input a month (1 to 12).
Display the season of the month received :
Spring runs from March (3) to May (5)
Summer runs from June (6) to August (8)
Autumn runs from September (9) to November (11)
Winter runs from December (12) to February (2)
'''


month = int(input("Enter month (1 to 12): "))

if month >= 1 and month <=12:

    if month >=3 and month <=5:
        print("Spring")
    elif month >=6 and month <=8:
        print("Summer")
    elif month >= 9 and month <=11:
        print("Autum")
    else:
        print("Winter")

else:
    print("Enter a number from 1 to 12")



