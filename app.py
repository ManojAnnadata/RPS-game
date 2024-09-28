import random
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
    +"Rock vs Paper -> Paper wins\n"
    +"Rock vs Scissors -> Rock wins\n"
    +"Paper vs Scissors -> Scissors wins")
while True:
    rock='''
          ____
    _-'    ___)
              (__)   
    (rock)    (__)
    __      (__)
        '--(__)
                '''
    papper='''
           ___
    __-'     _)__
                 ___)
    (papper)     ____)
    __      _____)
        '--____)            
    '''
    scissor ='''
            ___
    __-'     )__  
                ___)
    (scissor)   ____)
    __    (__)
          '-(_)
    '''
    game_images =[rock,papper,scissor]
    print("Enter your choice \n 0 - Rock \n 1 - Paper \n 2 - Scissors \n")
    user_choice =int(input("Enter your choice:"))
    if user_choice>=3 or user_choice<0:
        print("You entered into invalid numbere,You Lose")
    else:
        print("User choice is:",game_images[user_choice])
        print("Now it's Computer's Turn...")
        computer_chance =random.randint(0,2)
        print("computer choice:")
        print(game_images[computer_chance])
        if user_choice == computer_chance:
            result="DRAW"
        elif computer_chance==0 and user_choice== 2:
            result="You Lose"
        elif user_choice==0 and computer_chance==2:
            result="You Win"
        elif computer_chance>user_choice:   
            result="You Lose"
        elif user_choice>computer_chance:
            result="You Win"
        if result=="DRAW":
            print("<--It's a tie-->")
        elif result =="You Win":
            print("<---User Wins!--->")
        else:
            print("<---computer wins!--->")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
print("Thanks for playing!")
