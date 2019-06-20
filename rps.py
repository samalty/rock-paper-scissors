import random

def game_menu():
    print("Welcome to this rock, paper scissors app. What would you like to play?")
    print("1. First to 3")
    print("2. First to 5")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option

def first_to_3():
    
    user_score = 0
    computer_score = 0
    options = ['rock', 'paper', 'scissors']
    
    while (user_score < 5 and computer_score < 5):
        
        print("Rock, paper, scissors on 3.")
        print("One...")
        print("Two...")
        print("Three...\n")
    
        answer = input("Your answer: ")
        computer_answer = random.choice(options)
    
        print("Computer says... " + computer_answer + "\n")
    
        if answer == computer_answer:
            print("Draw. Let's go again.\n")
        elif answer == "rock" and computer_answer == "scissors":
            user_score += 1
            print("Rock blunts scissors. You win.\n")
        elif answer == "scissors" and computer_answer == "paper":
            user_score += 1
            print("Scissors cut paper. You win.\n")
        elif answer == "paper" and computer_answer == "rock":
            user_score += 1
            print("Paper covers rock. You win.\n")
        elif answer == "paper" and computer_answer == "scissors":
            computer_score += 1
            print("Scissors cut paper. You lose.\n")
        elif answer == "scissors" and computer_answer == "rock":
            computer_score += 1
            print("Rock blunts scissors. You lose.\n")
        elif answer == "rock" and computer_answer == "paper":
            computer_score += 1
            print("Paper covers rock. You lose.\n")
        else:
            print("Invalid option. Please try again.\n")
        
        if user_score == 3:
            print("You win {0} - {1}\n".format(user_score, computer_score))
            user_score = 0
            computer_score = 0
            game_loop()
        elif computer_score == 3:
            print("Computer wins {0} - {1}\n".format(computer_score, user_score))
            user_score = 0
            computer_score = 0
            game_loop()

def first_to_5():
    
    user_score = 0
    computer_score = 0
    options = ['rock', 'paper', 'scissors']
    
    while (user_score < 5 and computer_score < 5):
    
        print("Rock, paper, scissors on 3.")
        print("One...")
        print("Two...")
        print("Three...\n")
    
        answer = input("Your answer: ")
        computer_answer = random.choice(options)
    
        print("Computer says... " + computer_answer + "\n")
    
        if answer == computer_answer:
            print("Draw. Let's go again.\n")
        elif answer == "rock" and computer_answer == "scissors":
            user_score += 1
            print("Rock blunts scissors. You win.\n")
        elif answer == "scissors" and computer_answer == "paper":
            user_score += 1
            print("Scissors cut paper. You win.\n")
        elif answer == "paper" and computer_answer == "rock":
            user_score += 1
            print("Paper covers rock. You win.\n")
        elif answer == "paper" and computer_answer == "scissors":
            computer_score += 1
            print("Scissors cut paper. You lose.\n")
        elif answer == "scissors" and computer_answer == "rock":
            computer_score += 1
            print("Rock blunts scissors. You lose.\n")
        elif answer == "rock" and computer_answer == "paper":
            computer_score += 1
            print("Paper covers rock. You lose.\n")
        else:
            print("Invalid option. Please try again.\n")
        
        if user_score == 5:
            print("You win {0} - {1}\n".format(user_score, computer_score))
            user_score = 0
            computer_score = 0
            game_loop()
        elif computer_score == 5:
            print("Computer wins {0} - {1}\n".format(computer_score, user_score))
            user_score = 0
            computer_score = 0
            game_loop()

def game_loop():
    while True:
        option = game_menu()
        if option == "1":
            print("OK, first to 3.\n")
            first_to_3()
        elif option == "2":
            print("OK, first to 5.\n")
            first_to_5()
        elif option == "3":
            print("Thanks for playing.\n")
            break
        else:
            print("Invalid option\n")
        print("")

game_loop()