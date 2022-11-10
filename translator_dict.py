
# Giving english to french dictionary
English_to_French={"water" : "eau","pen" : "stylo","battle" : "Comba", "botle": "bouteille","butter" : "beurre", "house" : "maison", "computer" : "ordinateur","plum" : "prune"
}
# Giving french to english dictionary 
French_to_English ={"eau" : "water","stylo" : "pen", "combat" : "battle", "bouteille" : "botle", "beurre" : "butter", "maison" : "house","ordinateur" : "computer","brune" : "Plum"
 }

language = ["french", "english"]
trans_language = ""
word = ""

# repeat if the the loop if user enter a language different that french or english
while trans_language not in language:
  trans_language = str(input("Enter the translate either french or english: \n")
  )
else:
  Word = str(input("Enter the word you need the translation  the into chosen language: \n"))

# check if the work is in memory
  if Word in English_to_French or Word in French_to_English:
    
# give the french translation of the english word
    if trans_language == "french":
      if Word in English_to_French:
        translate = English_to_French[Word]
        print(f"\nthe translation of {Word} in french is {translate}")
      else:
        print(f"\n{Word} is not in my english to french dictionary memory")

# give the french translation of the english word
    elif trans_language == "english":
      if Word in French_to_English:
        translate = French_to_English[Word]
        print(f"\nthe translation of {Word} in english is {translate}")
      else:
        print(f"\n{Word} is not in my french to english dictionary memory")
  else:
    print(f"\n{Word} is not in my memory")  
