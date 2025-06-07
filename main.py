import random
def game(user_choice):
    choices=["snake", "water", "gun"]
    computer_choice= random.choice(choices)
    print(f"computer choice:{computer_choice}")
    if user_choice == computer_choice:
        return "its a draw"
    elif (user_choice== "snake" and computer_choice== "water") or \
        (user_choice== "water" and computer_choice== "gun") or \
        (user_choice== "gun" and computer_choice== "snake"):
        return "you win"
    else:
        return "you lose"
    #take users input
user_choice = input("enter your choice (snake\water\gun) ").lower()
print(game(user_choice))