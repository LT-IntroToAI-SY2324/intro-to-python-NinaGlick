# We will write a rock paper scissors game in class - Complete it in this file

import random

player_choice="rock"
computer_choice="rock"

def get_choices():
    
    options = ['rock', 'paper', 'scissors']
    player_choice=input("enter rock, paper, or scissors: ")
    computer_choice = random.choice(options)
    choices={"player": player_choice, "computer": computer_choice}

    return choices 

choices=get_choices()
# print(choices)

def check_winner(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player==computer:
        return "it's a tie"
    
    elif player=="rock":
        if computer=="scissors":
            return "rock smasshes scissors. you win"
        else:
            return "paper covers rock. you lose"
        
    elif player == "scissors":
        if computer=="paper":
            return "scissors cuts paper. you win"
        else:
            "rock crushes scissors. you lose"
    elif player=="paper":
        if computer=="rock":
            return "paper covers rock. you win"
        else:
            return "scissors cuts paper. you lose"
        
    else:
        return "you spelled something wrong"


result=check_winner(choices["player"], choices["computer"])
print(result)
    
    

# def get_player():
#     choices=get_choices()
#     player=choices["player"]
#     return(player)

# def get_computer():
#     choices=get_choices()
#     computer=choices["computer"]
#     return(computer)

# print(get_player())
# print(get_computer())

# def get_winner():
#     if()