#This Program will first ask a user for a username and password using while loop

credential = {
 "username":"soho" ,
  "password" : "Yeo"}
username = ""
password = ""
count = 0 
limit = 5      
while n < 5:
  username= str(input("enter your username\n")).lower()
  password= str(input("enter your passwor\n")).lower()
  if username != credential["username"]  or password != credential["password"]:
    print("access denied try again")
    n += 1
  elif username == credential["username"] and password == credential["password"] :
    print("you have access")
    break
  
print("Your account is locked")    
