#tip calculator

print("Welcome to the tip calculator.")
X=input("what was the total bill? $")
xx=float(X)
percentage=input("what percentage tip would you like to give?10,12 or 15?")
cc=int(percentage)
split=int(input("how many people to split the bill?"))
dd=int(split)

calculate_1=cc/100
##print(calculate_1)
calculate_2=str(xx*calculate_1)
m=calculate_2[0]
xyz=int(m)+calculate_1
calculate=round(xx/dd*xyz,3)

print(f"Each person should pay: ${calculate}")