from random import *
from time import *
from colorama import Fore
from goto import *

Developer_details='''******** Thanks for playing the game 'BlackJack' ********
********** Game Developer Tejvir Chauhan **********
                     '''

def quickresult(user_choice,cpu_choice,user_choice_sum,cpu_choice_sum):
  print()
  print(Fore.LIGHTMAGENTA_EX + "Your cards are: ", Fore.LIGHTCYAN_EX)
  for i in user_choice:
    print(i, end="  ")
  print()
  print(Fore.MAGENTA + "Computer cards are: ", Fore.CYAN)
  for j in cpu_choice:
    print(j, end="  ")

  print(Fore.LIGHTGREEN_EX + "\n\nAnalizing scores....")
  sleep(3)
  print(Fore.RESET)
  print()
  print("Your cards score:", user_choice_sum)
  print("Computer cards score:", cpu_choice_sum)
  print()
  sleep(3)
  quit(Developer_details)

while True:
  print()
  print(Fore.BLACK + "****************", Fore.RESET + "Welcome to 'BlackJack'",
        Fore.BLACK + "****************")
  print(Fore.BLACK + "*****************", Fore.RESET + "Let's start the game",
        Fore.BLACK + "*****************")
  print(Fore.RESET)
  cards = ['♠', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Ⓙ', 'Ⓚ', 'Ⓠ']
  numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
  ace = [11]
  user_choice = []
  cpu_choice = []
  user_ace_choice = []
  cpu_ace_choice = []
  user_choice_sum = 0
  cpu_choice_sum = 0
  user_choice += choices(cards, k=2)
  cpu_choice += choices(cards, k=2)

  while True:
    user_choice_sum = 0
    cpu_choice_sum = 0
    user_ace_choice = []
    cpu_ace_choice = []
    print()
    print(Fore.LIGHTMAGENTA_EX + "Your cards are: ", Fore.LIGHTCYAN_EX)
    for i in user_choice:
      print(i, end="  ")
      if "♠" == i:
        user_ace_choice += choices(ace, k=1)

    print()
    print(Fore.MAGENTA + "Computer cards are: ", Fore.CYAN)
    for j in cpu_choice:
      print("✽", end="  ")
      if "♠" == j:
        cpu_ace_choice += choices(ace, k=1)

    for s in user_choice:
      if s in numbers:
        user_choice_sum += s
      elif s == 'Ⓙ' or s=='Ⓚ' or s== 'Ⓠ':
        user_choice_sum += 10
    user_choice_sum += sum(user_ace_choice)
  
    for t in cpu_choice:
      if t in numbers:
        cpu_choice_sum += t
      elif t == 'Ⓙ' or t=='Ⓚ' or t== 'Ⓠ':
        cpu_choice_sum += 10
    cpu_choice_sum += sum(cpu_ace_choice)

    if user_choice_sum == 21:
      print(Fore.GREEN + "\n\n🏆🤩 You Won 🤩🏆")
      quickresult(user_choice,cpu_choice,user_choice_sum,cpu_choice_sum)

    elif user_choice_sum == 21:
      print(Fore.RED + "\n\n😔 You loose 😔")
      quickresult(user_choice,cpu_choice,user_choice_sum,cpu_choice_sum)

    elif user_choice_sum > 21:
      if "♠" in user_choice and 11 in user_ace_choice:
        if (user_choice_sum - 10) > 21:
          print(Fore.RED + "\n\n😔 You loose 😔")
          quickresult(user_choice,cpu_choice,user_choice_sum,cpu_choice_sum)
        else:
          user_ace_choice.remove(11)
          user_ace_choice.append(1)
          user_choice_sum -= 10

      else:
        print(Fore.RED + "\n\n😔 You loose 😔")
        quickresult(user_choice,cpu_choice,user_choice_sum,cpu_choice_sum)
    print()
    print()
    choice = input(Fore.LIGHTYELLOW_EX +
                   "You want to pick one more card[y/n]: ")
    if choice == "Y" or choice == "y":
      user_choice += choices(cards, k=1)
      continue
    else:
      if cpu_choice_sum < 17:
        cpu_choice += choices(cards, k=1)
      break

  user_choice_sum = 0
  cpu_choice_sum = 0
  
  for s in user_choice:
    if s in numbers:
      user_choice_sum += s
    elif s == 'Ⓙ' or s=='Ⓚ' or s== 'Ⓠ':
      user_choice_sum += 10
  user_choice_sum += sum(user_ace_choice)
  
  for t in cpu_choice:
    if t in numbers:
      cpu_choice_sum += t
    elif t == 'Ⓙ' or t=='Ⓚ' or t== 'Ⓠ':
      cpu_choice_sum += 10
  cpu_choice_sum += sum(cpu_ace_choice)
      
  print()
  print(Fore.LIGHTMAGENTA_EX + "Your cards are: ", Fore.LIGHTCYAN_EX)
  for i in user_choice:
    print(i, end="  ")
  print()
  print(Fore.MAGENTA + "Computer cards are: ", Fore.CYAN)
  for j in cpu_choice:
    print(j, end="  ")

  print(Fore.LIGHTGREEN_EX + "\n\nAnalizing scores....")
  sleep(3)
  print(Fore.RESET)
  print()
  print("Your cards score:", user_choice_sum)
  print("Computer cards score:", cpu_choice_sum)
  print()

  if user_choice_sum == cpu_choice_sum and user_choice_sum < 21:
    print(Fore.WHITE + "👏 It's a Draw 👏")
  elif user_choice_sum > 21:
    print(Fore.RED + "😔 You loose 😔")
  elif cpu_choice_sum > 21:
    print(Fore.GREEN + "🏆🤩 You Won 🤩🏆")
  elif user_choice_sum > cpu_choice_sum and user_choice_sum <= 21:
    print(Fore.GREEN + "🏆🤩 You Won 🤩🏆")
  elif cpu_choice_sum > user_choice_sum and cpu_choice_sum <= 21:
    print(Fore.RED + "😔 You loose 😔")
  else:
    print(Fore.BLACK + "There is some error. Please try again!!!")

  print()

  run_again = input(Fore.LIGHTYELLOW_EX + "You want to play again[y/n]: ")
  if run_again == 'y' or run_again == "Y":
    continue
  else:
    break

print()
print()

print(Fore.BLACK + "********",
      Fore.BLUE + "Thanks for playing the game 'BlackJack'",
      Fore.BLACK + "********")
print(Fore.BLACK + "**********",
      Fore.LIGHTBLUE_EX + "Game Developer Tejvir Singh Chauhan",
      Fore.BLACK + "**********")
