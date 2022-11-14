
word = input("Enter a word:\n") # Enter a word

word_list = word.split(",") #Split the word 
print("\n",word[::-1],"\n") # reverse the word

word_list = list(reversed(word))
print(word_list,"\n") #list the word

print("".join(word_list[::-1])) # return the word

#
