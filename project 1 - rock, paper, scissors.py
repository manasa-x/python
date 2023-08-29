
import random

def func():
    player = input("Rock(r), Paper(p), Scissors(s): Your choice? \n")
    player2 = random.choice(["r", "p", "s"])

    if player == "r":
        if player2 == "p":
            print("p\nYou lost")
        elif player2 == "s":
            print("s\nYou won")
        else:
            print("r\nDraw match")
    elif player == "p":
        if player2 == "s":
            print("s\nYou lost")
        elif player2 == "r":
            print("r\nYou won")
        else:
            print("p\nDraw match")
    elif player == "s":
        if player2 == "r":
            print("r\nYou lost")
        elif player2 == "p":
            print("p\nYou won")
        else:
            print("s\nDraw match")
    else:
        print("Invalid choice. Try Again!")
        
func()
while True:
    print("\nPlay Again: ")
    func()