import random

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

CHOICES = [rock, paper, scissors]
#using max choice to increase number of choices if required in futre
MAX_CHOICE = 2

def input_from_user(message):
  while True:
    try:
       user_input = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return user_input 
       break 



user_choice = input_from_user("What do you choose, Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

computer_choice = random.randint(0, MAX_CHOICE)

#by using constant CHOICES we can now write better/ readable code by mapping the user/computer choice with constant CHOICES list
print(f"{CHOICES[user_choice]}")
print("Computer chooses")
print(f"{CHOICES[computer_choice]}")

#updating if block for code readability

def play_game():
  if user_choice == computer_choice:
    print("Draw it is!")
  elif user_choice == 0 and computer_choice == 1:
      print("You lose")
  elif user_choice == 1 and computer_choice == 0:
      print("You won")
  elif user_choice == 1 and computer_choice == 2:
      print("You lose")
  elif user_choice == 2 and computer_choice == 1:
      print("You won")
  elif user_choice == 2 and computer_choice == 0:
      print("You lose")
  elif user_choice == 0 and computer_choice == 2:
      print("You won")
  else:
      print("Not a correct choice !!")


while input("Do you want to play the game, y or n: ").lower == "y":
  play_game()