# python-project
<h1> Find the last name of an employee in a dictionary</h1>

```
d = {
  "employee":[{"firstName" : "John", "lastName" : "Doe"},{"firstName" : "Anna", "lastName" : "Smith"}, {"firstName" : "Peter", "lastName" : "Jones"}],

"owners":[{"firstname": "Jack", "lastName": "Petter"},{"firstName": "Jessy", "lastName": "Petter"}]
           }

lastName = d["employee"][1]["lastName"]
print(f" The last Name of the second employee is: {lastName}")

```
<img width="872" alt="Screen Shot 2022-11-10 at 7 07 59 PM" src="https://user-images.githubusercontent.com/85723311/201231981-2d98d506-1388-4e5d-8a00-4d7d6aa3c8d6.png">

<h1> English to French and French to English dictionary</h1>

```

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
    
  ```
  <img width="839" alt="Screen Shot 2022-11-10 at 7 13 24 PM" src="https://user-images.githubusercontent.com/85723311/201232522-541e6180-a4cf-45fd-9fd5-c9669ff2d295.png">

