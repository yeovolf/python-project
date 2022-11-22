#This Program will first ask a user for a username and password using while loop

credential = {
  "username":"soho" ,"password" : "Yeo"}
username = ""
password = ""
count = 0 
limite = 5
while count < limit:
  username= str(input("enter your username\n")).lower()
  password= str(input("enter your passwor\n")).lower()
  if username != credential["username"]  or password != credential["password"]:
    print("access denied try again")
    count += 1
  elif username == credential["username"] and password == credential["password"] :
    print("you have access")
    break
  
print("Your account is locked")    
