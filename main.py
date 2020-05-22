from random import randint
name = input("Enter your name:")
print("Hi,", name, "welcome to Rock, Paper, Scissors game.")

t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0, 2)]

player = False

while player == False:

    player = input("Rock, Paper, Scissors?")

    if player == computer:
        print("Oh Good,the game is Tie!")
    elif player == "Rock":

        if computer == "Paper":
            print(name, "You lose!", computer, "covers", player)
        else:
            print(name, "You win!", player, "smashes", computer)
    elif player == "Paper":

        if computer == "Scissors":
            print(name, "You lose!", computer, "cut", player)
        else:
            print(name, "You win!", player, "covers", computer)
    elif player == "Scissors":

        if computer == "Rock":
            print(name, "You lose...", computer, "smashes", player)
        else:
            print(name, "you win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = t[randint(0, 2)]

