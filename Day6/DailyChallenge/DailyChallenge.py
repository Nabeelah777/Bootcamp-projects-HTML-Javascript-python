#Daily Challenge: Build Up A String
#1 & 2

sentence = str(input("Type a sentence: "))
sentence_length = int(len(sentence))
first_letter = sentence[0:1]
last_letter = sentence[sentence_length-1]
if sentence_length < 10:
    print("string not long enough")
elif sentence_length > 10:
    print("string too long")
else:
    print(f"first letter: {first_letter}, Last letter: {last_letter}")


#Using a for loop, construct the string character by character: Print the first character, then the second, then the third, 
# until the full string is printed. For example:

user_sentence = "Hello World"
user_sentence_length = int(len(user_sentence))
print(user_sentence_length)
# using list()
# to split string to character list
res = list(user_sentence)  
print(res)
res_index = 0
word = ""       
numbers = range(0 ,user_sentence_length)

for res_index in numbers:
    word = word + res[res_index]
    print(word)

#4
import random
random.shuffle(res)
print(res)
shuffle_word = ""
print(shuffle_word.join(res))
