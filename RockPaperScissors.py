import random

computer_list = ["rock","paper","scissors"]

while True:
    computer_random_choice = computer_list[random.randint(0, 2)]
    your_choice = input("enter your choice - Rock Paper Scissors or (end the game) :").lower()
    if your_choice == "end the game":
        print("Game ended!")
        break
    elif your_choice == computer_random_choice:
        print("its a tie!")
    elif your_choice == "rock":
            if computer_random_choice == "scissors":
                print("you Won..rock crushes scissors")
            elif computer_random_choice == "paper":
               print("you loss..Paper covers rock")
    elif your_choice == "paper":
            if computer_random_choice == "scissors":
                print("you loss..Scissors cuts Paper")
            elif computer_random_choice == "rock":
                print("You Won..Paper covers rock")
    elif your_choice == "scissors":
            if computer_random_choice == "rock":
                print("You loss..rock crushes scissors")
            elif computer_random_choice == "paper":
               print("You Won..Scissors cuts Paper")
    else:
        print("Please check your spelling!")






