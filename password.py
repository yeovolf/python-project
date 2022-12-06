#This Program will first ask a user for a username and password using while loop

<<<<<<< HEAD
credential = {
 "username":"soho" ,
  "password" : "Yeo"}
username = ""
password = ""
count = 0 
limit = 5      
while n < 5:
=======
credential = {"username":"soho" ,"password" : "Yeo"}

username = ""
password = ""

count = 0 
limite = 5

while count < limite:
  count += 1
  
>>>>>>> acd5905943d5b5984d371ae3bbf4de786f455d5e
  username= str(input("enter your username\n")).lower()
  password= str(input("enter your passwor\n")).lower()
  
  if username != credential["username"]  or password != credential["password"]:
    print("access denied try again")
    continue
    
  elif username == credential["username"] and password == credential["password"] :
    print("you have access")
    break
  
print("Your account is locked")    
