#leap year calculator
print("Leap year calculation!!")
year=int(input("which year do you want to calculate? "))
if year%4==0:
  if year%100==0:
    if year%400==0:
      print("this is a leap year")
    else:
      print("this is not a leap year")
  else:
    ("this is a leap year")
else:
  print("this is not a leap year")
