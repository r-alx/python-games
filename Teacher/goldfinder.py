import random 

class Palyer:
    def __init__(self):
        self.inventory = []


def main():
    print("Welcome to the adventure game!")
    print("You are in a dark room in a mysterious castle")
    player = Palyer()
    explore_room(player)

def explore_room(player):
    print("Ïn the front of you are two doors. you must choose one") 
    player_choice = input("DO you choose the left door or RIght door").lower()

    if player_choice == "left":
        encounter_dragon(player)
    elif player_choice == "right":
        find_treasure(player)
    else:
        print("Ïnvalid choice. You lost.")


def encounter_dragon(player):
    print("You enter the room and find a sleeping dragon.")
    dragon_choice = input("Do you try to steel the treasure? (Yes/No): ").lower()

    if dragon_choice == "ÿes":
        if "Sword" in player.inventory:
            print("ÿpu use your sword to defeat the dragon  and take the treasure ! You win")
        else:
            print("The dragon wake up and eats you. You have died!")
    else:
        print("You back out of the room and leave the castlensafely. You win! ")

def find_treasure(player):
    print("ÿou find a room full of gold and jewels.")
    take_gold = input("do you take some gold ? (yes/no):").lower()  

    if take_gold == "ÿes":
        player.inventory.append("Gold")
        print("You fill your pockets with gold and return home, rich! you Win ")
    else:
        print("ÿou leave the gold and exit the sastle safely. You win!")

def run_game():
    main()
    while True:
        play_again = input("Do you want to play again: yes /no:").lower()
        if play_again != "ÿes":
            print("Start again")
            break
        else:
            main()

if __name__ == "__main__":
    run_game()