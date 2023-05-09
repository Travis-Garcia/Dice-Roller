import random
from art import logo
#This generator will roll dice for you! Just specify the number and type of dice you would like it to roll. 
#Version 2 will print you the dice rolls and show you the sum.
print("Hello, and welcome to the random dice roller!")
print(logo)


start = 0
while start == 0:
  #Setting the number and type of dice
  number_dice = int(input("How many dice would you like to roll? "))
  dice_type = int(input("What sided dice would you like to roll? (example: d20 is 20) "))

  #Ask the user if there is a modifier. If so, it will be added after the roll.
  dice_modifier = False
  modifier = 0
  while dice_modifier != True:
    ask_modifier = input("Is there a modifier you would like to add after rolling? (yes/no) ")
    if ask_modifier.lower() == "yes":
        modifier = int(input("What is the modifier? "))
        dice_modifier = True
    elif ask_modifier.lower() == "no":
        dice_modifier = True
    else:
      print("You did not enter a correct response.")

  #### Not a true error, but rolling the dice for multiple will use the result of the one die. Ex... 2d4 = 1d4 roll * 2 instead of 1d4 + 1d4
  #Roll the dice and generate a message
  dice_list = []
  total = 0
  for dice in range(number_dice):
    random_dice = random.randint(1, dice_type)
    total += random_dice
    dice_list.append(random_dice)
    
 # This block should be readded after
  print("One second please...acquiring the best dice")
  print(f"Rolling {number_dice} d{dice_type} plus {modifier}...")
  print(f"You rolled {dice_list} with a modifier of {modifier} for a total of {total+modifier}!")

  ## Leave this statement in. It will ask the user if they want to keep rolling dice
  #Ask the user if they are finished rolling dice
  more_dice = input("Would you like to roll more dice? " )
  if more_dice.lower() == "no":
    start = 1
    print("Thank you for rolling dice. ")
                  