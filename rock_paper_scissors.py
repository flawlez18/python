# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇

# user = input("please enter rock, scissors or paper: ")
# system = ["rock", "scissors", "paper"]
# system_choice = random.choice(system)

# print(f'Your choice: {user}')

# print(f"system choice: {system_choice}")

# if user == "rock" and system_choice == "paper":
#     print("you lose")

# elif user == "rock" and system_choice == "scissors":
#     print("you win")

# elif user == "paper" and system_choice == "rock":
#     print("you win")

# elif user == "paper" and system_choice == "scissors":
#     print("you lose")

# elif user == "scissors" and system_choice == "rock":
#     print("you lose")

# elif user == "scissors" and system_choice == "paper":
#     print("you win")

# else:
#     print("This round is draw")

##############################################
#USed chatgpt to troubleshoot images not printing.
##############################################

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

user = input("please enter rock, scissors or paper: ")
system = ["rock", "scissors", "paper"]
system_choice = random.choice(system)

game_images = [rock, scissors, paper]

print(f'Your choice:')
if user == "rock":
    print(rock)
elif user == "scissors":
    print(scissors)
elif user == "paper":
    print(paper)

print(f"\nSystem choice:")
if system_choice == "rock":
    print(rock)
elif system_choice == "scissors":
    print(scissors)
elif system_choice == "paper":
    print(paper)

if user == "rock" and system_choice == "paper":
    print("\nYou lose!")

elif user == "rock" and system_choice == "scissors":
    print("\nYou win!")

elif user == "paper" and system_choice == "rock":
    print("\nYou win!")

elif user == "paper" and system_choice == "scissors":
    print("\nYou lose!")

elif user == "scissors" and system_choice == "rock":
    print("\nYou lose!")

elif user == "scissors" and system_choice == "paper":
    print("\nYou win!")

else:
    print("\nThis round is a draw.")
