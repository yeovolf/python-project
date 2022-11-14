# Giving list
list1=[3, 4, 5, 6]
list2=[-1, -2, -3, -4]
list3=[0, 0, 0, 0]
# empty list condition
if len(list1) == 0 or len(list2) == 0 or len(list3) == 0:
  print([])
  print("none")
# print max and min number from the giving lst
else:
  print(f"{max(list1)} {min(list1)}\n{max(list2)} {min(list2)}\n{max(list3)} {min(list3)}")

  