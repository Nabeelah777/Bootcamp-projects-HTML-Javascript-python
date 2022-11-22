#Challenge 1

number = int(input("Enter a number "))
length = int(input("Enter length "))

def multiples(number, length):
    l = []
    for i in range(1, length+1):
        l.append(number*i)
    return l

print(multiples(number, length))


#Challenge 2

string = str(input("Enter string "))
p=""
for char in string:
    if char not in p:
        p=p+char
print(p)


