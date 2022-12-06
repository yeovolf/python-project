# count down from 10 to 0

limite = 11 # set the limite
count = 0 # initial count value
count_down = 10 # countdown initial value
print(f"Starting to countdown backward from {count_down} - {count} \n")
# while loop
while count < limite:
  count += 1
  print (f"{count_down} \n")
  count_down -= 1

  if count_down == 0:
    print("Countdown is over")