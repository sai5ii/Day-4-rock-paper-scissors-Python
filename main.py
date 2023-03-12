import random
from replit import clear
  
rock = '''
    _______
---'R  ____)
    O(_____)
    C(_____)
    K (____)
---.__(___)
'''

paper = '''
    _______
---' P ____)____
     A    ______)
     P    _______)
     E   _______)
---._R________)
'''

scissors = '''
    _______
---'   ____)____
   SCI    ______)
   SSO __________)
   RS (____)
---.__(___)
'''

#Write your code below this line 👇
#updated version
#using CHOICES constant instead of variable

def input_from_user(message):
  while True:
    try:
       user_input = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       if user_input not in range(0,3):
         print("Choose 0 , 1 or 2 only ")
       else:
         return user_input
         break 


def play_game():
  
  CHOICES = [rock, paper, scissors]
#using max choice to increase number of choices if required in futre
  MAX_CHOICE = 2
  user_choice = input_from_user("What do you choose, Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
  computer_choice = random.randint(0, MAX_CHOICE)

  print(f"{CHOICES[user_choice]}")
  print("Computer chooses")
  print(f"{CHOICES[computer_choice]}")
  
  if user_choice == computer_choice:
    print("Draw it is!")
    return
  elif user_choice == 0 and computer_choice == 1:
    print("You lose")
    return
  elif user_choice == 1 and computer_choice == 0:
    print("You won")
    return
  elif user_choice == 1 and computer_choice == 2:
    print("You lose")
    return
  elif user_choice == 2 and computer_choice == 1:
    print("You won")
    return
  elif user_choice == 2 and computer_choice == 0:
    print("You lose")
    return
  elif user_choice == 0 and computer_choice == 2:
    print("You won")
    return
  else:
    print("Not a correct choice !!")
    return

#by using constant CHOICES we can now write better/ readable code by mapping the user/computer choice with constant CHOICES list

#updating if block for code readability
while input("Do you want to play the game, y or n: ").lower() == "y":
  clear()
  play_game()

print("Thanks for playing...")