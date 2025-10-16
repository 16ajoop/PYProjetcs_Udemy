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


import random
option = [ rock, paper, scissors ]
user_option = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_option = random.randint(0,2)
if computer_option >=0 and user_option<=2:
    print("Your choice: ", option[user_option])
    print("Computer choice: ",option[computer_option])


if user_option >= 3 or user_option <0:
    print("Invalid value")
elif user_option ==0 and computer_option == 2:
    print("You Win!")
elif user_option == 2 and computer_option == 0:
    print("You lose!")
elif computer_option > user_option :
    print("You lose!")
elif user_option > computer_option:
    print("You Win!")
elif computer_option == user_option:
    print("Match Draw")
