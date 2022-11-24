#DailyCHallenge


phrase = input("Input a list of words separated by commas: ")
phrase_list = phrase.split(",")
phrase_list.sort()
length_phraselist = len(phrase_list)
print(phrase_list[0:length_phraselist])
