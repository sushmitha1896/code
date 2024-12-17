print("Welcome to pizza deliveries!!")
size=input("what size pizza you want?s,m or l ? ")
extracheese=input("do you want extra cheese? y or n? ")
add_pepporoni=input("do you want pepperoni?y or n? ")
bill=0
if size=="s":
  bill+=15
elif size=="l":
  bill+=20
else:
  bill+=25

if add_pepporoni=="y":
  if size=="s":
    bill+=2
  else:
    bill+=3

if extracheese=="y":
  bill+=1


print(f"your final bill is $ {bill}.")
