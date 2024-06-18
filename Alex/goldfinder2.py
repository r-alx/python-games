import random

class Player:
    def __init__(self):
        self.inventory = []

def main():
    print("Welcome to alex goldfinder game.")
    print("you are at a haunted tower")
    player = Player()
    explore_room(player)

def explore_room(player):
    print("Ther are 2 doors in front of u you must found a tnt")
    player_choice = input("do you choose the left or the right:]").lower()

    if player_choice == "left":
       ender_dragon(player)
    elif player_choice == "right":
        explore_room(player)
    else:
        print("Player was banned from the sever.lol")

def ender_dragon(player):
    print("You find a sleepig ender dragon")
    ender_dragon = input("do you still want to get the treasure plus 2 tnt?(yes/no)").lower()
    
    if player == "yes":
        if "sword" in player.inventory:
            print("use your enchanted sword to attack the stubid dragon and go out")
        else:
            print("pov:player were kill by ender dragon")
    else:
        print("lol but you win and take everythng and fly away")
def find_treasure():
    print("you find a full room fill with diamond gold and tnt")
    take_gold = input("do you want to take all(yes/no)").lower()
    if take_gold == "yes":
       Player.inventory.append("Gold,Diamond,TNT")
       print("you fill your pocket and inventory full of diamond and gold and found TNT choose one")
    else:
        print("you leave the castle but you acidently step on something and you fell to a large and deep hole you died.lol ")
def run_game():
    main()
    while True:
        play_again = input("do you want to go again:]").lower()
        if play_again =="yes":
            print("start_again")
            break
        else:
            main()
if __name__ == "__main__":
    run_game()
    

