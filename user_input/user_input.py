import random
import sys, math
while True:
    try:
        player_choice = int(input("Enter your Choice in number\n1.Rock\n2.Scissors\n3.Paper\n4.Exit\n\n"))
        if player_choice < 1 and player_choice > 4:
            sys.exit("Please enter the number in the given range.")
        if player_choice == 4:
             print("Exiting......")
             break
        computer_choice = int(random.choice("123"))
        print("")
        print("You chose",player_choice)
        print("Computer chose",computer_choice)
        if computer_choice == 3 and player_choice == 2:
            print("You won..\n")
        elif computer_choice == 2 & player_choice == 1:
                print("You won..\n")
        elif computer_choice == 1 and player_choice == 3:
                print("You won..\n")
        elif computer_choice == player_choice:
            print("The game was draw!\n")
        else:
            print("Computer won..\n")
    except:
        sys.exit("Please re-enter the correct number.\n")

    