import random 
#defining a function to accept user input
def user_input():
    while True:
        user_choice = input('What is it gonna be, Rock, Paper, Scissors: ').lower()
        choices = ['rock','paper','scissors']
        if user_choice in ['rock', 'paper','scissors']:
            return user_choice 
        else:
            return 'invalid input try again'
        
#defining a function to randomize the computer's choice 

def com_input():
    while True:
        choices = ['rock','paper','scissors']
        com_choice = random.choice(choices)
        return com_choice
    
#defining the rules of the game using afunction

def game_rules(user_choice, com_choice):
    
    choices = ['rock','paper', 'scissors']

    #.if the user's input is the same as what the computer generated the program should display 'ITs A TIE'
    if user_choice == com_choice:
        return'IT as tie'
    #.declaring the rule rock beats scissors, scissors beats paper and paper beats rock.
    elif user_choice == 'rock' and com_choice == 'scissors' or \
         user_choice == 'paper' and com_choice == 'rock' or \
         user_choice == 'scissors'and com_choice == 'paper':
        return 'you WIN!!!'
    #. this condition is in the event where the user inputs anything other than Rock, paper or scissors
    elif user_choice not in ['rock', 'paper', 'scissor'] and com_choice == 'rock' or\
         user_choice not in ['rock', 'paper', 'scissor'] and com_choice == 'scissor' or \
         user_choice not in ['rock', 'paper','scissor'] and com_choice == 'paper':
        return 'You\'ve got to choose rock, paper or scissors!!!'    
    else:
        return 'COM wins'
    
    #now lets play the game

def game():
    while True:
        print('WELCOME TO OUR LITTLE ROCK, PAPER, SCISSORS GAME. \n THE RULES ARE SIMPLE, ROCK BEATS SCISSORS, SCISSORS BEATS PAPER WHILST PAPER BEATS ROCK')
        user = user_input()
        com = com_input()
        print('You chose',user)
        print ('COM chose', com)
        print (game_rules(user, com))


        playOn = input('Do you wish to continue, yes or no: ').lower()
        
        if playOn != 'yes':
            break
        
      

game()

    


    
