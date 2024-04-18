import random
def rockpaperscissors():
    choicess = ["paper","rock","scissors"]
    com_choice =random.choice(choicess)

    your_choice = input("enter rock paper scissor or else:").lower()

    if your_choice not in choicess:
        print("!!SUS!! you were killed by ...")
        return
    print(f"computer chose:{com_choice}")

    if your_choice == com_choice:
        print("bruh no fun when its a tie...")
    elif(your_choice == "rock" and com_choice == "scissors")or(your_choice == "paper" and com_choice == "rock")or(your_choice == "scissors"and com_choice == "paper"):
        print("good job but you still on game")
    else:
        print("!!LOSER!! LOL !!HAHAHAHAAHAHAHAHAHA!!")

rockpaperscissors()