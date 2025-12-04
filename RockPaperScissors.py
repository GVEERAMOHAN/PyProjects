import random

opt = ["rock", "paper", "scissors"]
def make_choice():
    my_choice = input("Enter your choice(rock, paper, scissors): ")
    my_choice = my_choice.lower()
    com_choice = random.choice(opt)
    choices = {"Player": my_choice, "Computer": com_choice}
    return choices

def check_choice(Player, Computer):
    print(f"Your choice is: ({Player}), and Computer choice is: ({Computer})")
    if Player == Computer:
        return "It's a tie!"
    elif Player == "rock":
        if Computer == "scissors":
            return "Rock breakes Scissors, You Win!"
        else:
            return "Paper wrapes Rock, You lose."
    elif Player == "paper":
        if Computer == "rock":
            return "Paper wrapes Rock, You Win!"
        else:
            return "Scissors will cut Paper, You lose."
    elif Player == "scissors":
        if Computer == "paper":
            return "Scissors will cut Paper, You Win!"
        else:
            return "Rock breakes Scissors, You lose."

choices = make_choice()
result = check_choice(choices["Player"], choices["Computer"])
print(result)