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

choice_list = [rock,paper,scissors]

user_choice = int(input("What do you choose, Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

computer_choice = random.randint(0,2)

print(f"{choice_list[user_choice]}")
print("Computer chooses")
print(f"{choice_list[computer_choice]}")


if user_choice == 0:
  if computer_choice == 0:
    print("Draw it is!")
  elif computer_choice == 1:
    print("You lose")
  else:
    print("You won")

elif user_choice == 1:
  if computer_choice == 1:
    print("Draw it is")
  elif computer_choice == 0:
    print("You Won")
  else:
    print("You lose")
  
elif user_choice == 2:
  if computer_choice == 2:
    print("Draw it is")
  elif computer_choice == 0:
    print("You lose")
  else:
    print("You won")
else:
  print("Not a correct choice !!")