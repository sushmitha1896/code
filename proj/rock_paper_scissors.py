#rock paper scissors
print("WELCOME TO ROCK PAPER SCISSORS GAME!!!")
my_choice=int(input("what do you choose?Type 0 for ROCK,1 for PAPER or 2 for SCISSORS."))
rock='''                 _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\ '''

paper='''  _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|               '''

scissors='''           _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/
                                    '''

                                   

import random
computer_choice=random.randint(0, 2)

if my_choice==0:
  print(rock)
  print("computer chose  :")
  if my_choice==0 and computer_choice==0:
    print(rock)
    print("Draw")
  if my_choice==0 and computer_choice==1:
    print(paper)
    print("you lose")
  elif my_choice==0 and computer_choice==2:
    print(scissors)
    print("you won")
elif my_choice==1:
  print(paper)
  print("computer chose:")
  if my_choice==1 and computer_choice==0:
    print(rock)
    print("you won")
  if my_choice==1 and computer_choice==2:
    print(scissors)
    print("you lose")
  elif my_choice==1 and computer_choice==1:
    print(paper)
    print("Draw")
if my_choice==2:
  print(scissors)
  print("computer chose :")
  if my_choice==2 and computer_choice==1:
    print(paper)
    print("you win")
  if my_choice==2 and computer_choice==0:
    print(rock)
    print("you lose")
  elif my_choice==2 and computer_choice==2:
    print(scissors)
    print("Draw") 
elif my_choice>=3:
  print("invalid number.you lose.")
