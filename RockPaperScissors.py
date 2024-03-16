import random
while True:
    game=["rock","paper","scissor"]
    computer=random.choice(game)
    user=None
    while user not in game:
        user=input("Enter your choice: ").lower()
    if user==computer:
        print(user)
        print(computer)
        print("Tie!!!")
    elif user=="rock":
        if computer=="paper":
            print(user)
            print(computer)
            print("You lost!!!")
        elif computer=="scissor":
            print(user)
            print(computer)
            print("You Won!!!")
    elif user=="scissor":
        if computer=="paper":
            print(user)
            print(computer)
            print("You Won!!!")
        elif computer=="rock":
            print(user)
            print(computer)
            print("You lost!!!")
    elif user=="paper":
        if computer=="rock":
            print(user)
            print(computer)
            print("You Won!!!")
        elif computer=="scissor":
            print(user)
            print(computer)
            print("You lost!!!")
    play=input("Do you want to play again? (yes/no): ").lower()
    if play!="yes":
        break
print("Thank you for playing, Bye!!!")



