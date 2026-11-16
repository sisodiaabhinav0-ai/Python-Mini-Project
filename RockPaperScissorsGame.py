import random
choice = ["rock", "paper", "scissors"]
userScore = 0
comScore = 0

while True:
    user = input(f"Choose one {choice} or type 'stop' to quit: ").lower()

    #Stop condition 
    if user == "stop":
        print("\nGame End")
        print(f"Your score is {userScore}")
        print(f"Computer score is {comScore}")
        break

    #Invalid input check
    if user not in choice:
        print("Invalid input, try again!\n")
        continue

    #Computer choice
    com = random.choice(choice)

    # Compare choices
    if com == user:
        print("It's a tie")
    elif user == "rock" and com == "scissors" or user == "paper" and com == "rock" or user == "scissors" and com == "paper":
        print("You won 🕺🏼")
        userScore += 1
    else:
        print("Computer won ")
        comScore += 1

    #Score after every round
    print(f"Score = You: {userScore} | Computer: {comScore}")

