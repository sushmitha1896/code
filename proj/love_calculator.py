#love calculator
print("Welcome to the love calculator!")
name=input("what is your name? \n" )
name1=input("what is your lover name?\n")

lower123=name.lower() + name1.lower()

TRUE=lower123.count("t") + lower123.count("r") + lower123.count("u") + lower123.count("e")
LOVE=lower123.count("l") + lower123.count("o") + lower123.count("v") + lower123.count("e")
SCORE1=(f"{TRUE}" + f"{LOVE}")
score=int(SCORE1)
#print(type(score))
#variable name is not case sensitive.

if score<50 or score<90:
  print(f"your score is {score},you go together like coke and mentos.")
elif score<40 and score>50:
  print(f"your score is {score},you are alright together.")
else:
  print(f"your score is {score}.")
