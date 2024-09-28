import random
import sys

# Display the winning rules of the game
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      +"Rock vs Paper -> Paper wins\n"
      +"Rock vs Scissors -> Rock wins\n"
      +"Paper vs Scissors -> Scissors wins")

# Check if a user choice is provided as an argument
if len(sys.argv) < 2:
    print("Please provide your choice as a command-line argument: 0 for Rock, 1 for Paper, 2 for Scissors")
    sys.exit(1)

# Convert the argument to an integer
user_choice = int(sys.argv[1])

# Define game images
rock = '''
      ____
_- '    ___)
          (__)   
(rock)    (__)
__      (__)
    '--(__)
            '''
paper = '''
       ___
__-'     _)__
             ___)
(paper)     ____)
__      _____)
    '--____)            
'''
scissor = '''
        ___
__-'     )__  
            ___)
(scissor)   ____)
__    (__)
      '-(_)
'''
game_images = [rock, paper, scissor]

# Validate user choice
if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number. You Lose.")
else:
    print("User choice is:", game_images[user_choice])
    print("Now it's Computer's Turn...")
    computer_chance = random.randint(0, 2)
    print("Computer choice:")
    print(game_images[computer_chance])
    
    # Determine the result of the game
    if user_choice == computer_chance:
        result = "DRAW"
    elif computer_chance == 0 and user_choice == 2:
        result = "You Lose"
    elif user_choice == 0 and computer_chance == 2:
        result = "You Win"
    elif computer_chance > user_choice:   
        result = "You Lose"
    else:
        result = "You Win"

    # Display the result
    if result == "DRAW":
        print("<--It's a tie-->")
    elif result == "You Win":
        print("<---User Wins!--->")
    else:
        print("<---Computer Wins!--->")

print("Thanks for playing!")

