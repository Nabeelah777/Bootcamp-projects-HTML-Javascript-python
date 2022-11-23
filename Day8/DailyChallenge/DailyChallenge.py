#Daily Challenge: Dictionaries
#Challenge 1

word = input("Type a word : ")
import re
pattern = re.compile(r"(^[a-zA-Z]+$)+")
cond = pattern.fullmatch(word)
if cond ==None:
    print("Enter a word")
else :
      list = {}
      fin=len(word)
      for i in range(0,fin) :
              if word[i] in list :
                  list[word[i]].append(i)
              else :
                  list[word[i]]=[i]
      print(list)


#Challenge 2
items_purchase = {
   "Apple": "$4",
   "Honey": "$3",
   "Fan": "$14",
   "Bananas": "$4",
   "Pan": "$100",
   "Spoon": "$2"
 }

wallet = "$100"
sorted= items_purchase
print(sorted)
buy =[]
for i in sorted:
    if(int(sorted[i][1:]) <= int(wallet[1:])):
          buy.append(i)

if buy == []:
    print("Nothing")
else :
    print(buy)

def higest_even(li):
    evens = []
    for sorted in li:
         if sorted % 2 == 0:
              evens.append(sorted)
         return max(evens)
print(higest_even([4,5,7,9,9,9,9,9,9,9,9]))

def super_func(*args, **kwargs):
   total = 0
   for items in kwargs.values():
    total += items
    return sum(args) + total
print(super_func(1,2,3,4,5, num1 = 5, num2 = 10))