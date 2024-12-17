#pizza excercise
print("Welcome to pizza deliveries!!")
size=input("what size pizza you want?s,m or l ? ")
extracheese=input("do you want extra cheese? y or n? ")
add_pepporoni=input("do you want pepperoni?y or n? ")

if size=="s":
  bill=15
  if add_pepporoni=="y":
    bill+=2
if size=="m":
  bill=20
  if add_pepporoni=="y":
    bill+=3
if size=="l":
  bill=25
  if add_pepporoni=="y":
    bill+=3
if extracheese=="y":
  bill+=1
print(f"your final bill is $ {bill}.")    