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

from random import randint

rps = int(input("What dou you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer = randint(0, 2)

if rps == 0:
    print(rock)
    if computer ==0:
        print(f"Computer chose:\n{rock}")
        print("Draw")
    elif computer ==1:
        print(f"Computer chose:\n{paper}")
        print("You lost")
    else:
        print(f"Computer chose:\n{scissors}")
        print("You win")
        


elif rps == 1:
    print(paper)
    if computer ==0:
        print(f"Computer chose:\n{rock}")
        print("You win")
    elif computer ==1:
        print(f"Computer chose:\n{paper}")
        print("Draw")
    else:
        print(f"Computer chose:\n{scissors}")
        print("You lost")
        


elif rps ==2:
    print(scissors)
    if computer == 0:
        print(f"Computer chose:\n{rock}")
        print("You lost")
    elif computer ==1:
        print(f"Computer chose:\n{paper}")
        print("You win")
    else:
        print(f"Computer chose:\n{scissors}")
        print("Draw")

else:
    print("Wrong choice")




