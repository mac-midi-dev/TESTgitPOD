from random import randint

""""
#------------------------------------------*
#   Rock.Paper.Scissors written in Python  |
#                      Author: MACmidiDev  | 
#  _Build RPSshoot!                        |
#   1: setGame to LOOP                     |
#   2: setAI to randomly pick-(RPS)        |
#   3: setGame Logic-(RPS)                 |
#                                          |
######################################### -*
"""


#   3).
#   uses parameters to compare(AI-choice VS Input-PLAYERs choice)
#   if-else covers all possible outcomes stringMethod.lower() 
#   ensures correct case when comparing
#   ************ * * *  *  ---------------- >>>   lastly we must end the gameLOOP
def compare(user, computer):
    if user.lower() == computer.lower():
        print("It's a tie!")
    elif user.lower() == 'rock' or 'r':
        if computer.lower() == 'scissors':
            print("You win!")
        else:
            print("The computer wins!")
    elif user.lower() == 'scissors' or 's':
        if computer.lower() == 'paper':
            print("You win!")
        else:
            print("The computer wins!")
    elif user.lower() == 'paper' or 'p':
        if computer.lower() == 'rock':
            print("You win!")
        else:
            print("The computer wins!")
    else:
        print("Invalid input! You have not entered rock, paper or scissors, try again.")


#   2).
#   AI-choice(RETURN)s (R P S)-from random int via index
def get_computers_choice():
    choices = ["Rock", "Paper", "Scissors"]
    choice_index = randint(0, 2)
    choice = choices[choice_index]
    return choice


#   1).
#   bool to True sets LOOP 
#       get Input-PLAYERs choice
#           create AI-choice(RETURN)_and compare
#                 now we need a compare function
#   victor will select the winner PROMTPto playAgain_(N): SETplay_game(False)=endGameLOOP
def game_loop():
    play_game = True
    
    while play_game:
        user = input("Rock(r), Paper(p), or Scissors(s) ?")
        computer = get_computers_choice()
        
        victor = compare(user, computer)
        
        play_again = input("Would you like to play again? Y/N:")
        
        if play_again.lower() == "n":
            play_game = False
            
    print("Thanks for playing!")

game_loop()