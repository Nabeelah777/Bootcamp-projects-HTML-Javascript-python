#Daily Challenge Gold

from datetime import date
import calendar

date_of_birth=input("Enter your birth date: (dd/mm/yyyy)")

dob = date_of_birth.split("/")

year=int(dob[2])
month=int(dob[1])
day=int(dob[0])

cdate = date.today()
birthdate = date(year,month,day)
diff = cdate - birthdate
age = int(diff.days/365)

agestr=str(age)
num=int(agestr[-1])

print(age)

print("    "+"-"*int((11-num)/2)+"i"*num+"-"*int((11-num)/2))

print("   |:H:a:p:p:y:|")
print(" __|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")



import calendar

if calendar.isleap(year)==True:
    print("    "+"-"*int((11-num)/2)+"i"*num+"-"*int((11-num)/2))

    print("   |:H:a:p:p:y:|")
    print(" __|___________|__")
    print("|^^^^^^^^^^^^^^^^^|")
    print("|:B:i:r:t:h:d:a:y:|")
    print("|                 |")
    print("~~~~~~~~~~~~~~~~~~~")