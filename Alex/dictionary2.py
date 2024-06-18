word_data = {
             "cold":{
                 "definition":"shivering to death",
                 "opposite":["hot","warm"]
                 }, 
            "dash":{
                "definition":"to run fast with lighting speed",
                "opposite":["slow"]
                 },
            "rainy":{
                "definition":"dark stormy cloud,and water drop down from the sky",
                "opposite":["sunny"]
                 }
                }
print(word_data)
def look_word():
    word = input("Enter the word that you want:]").lower()
    if word in word_data:
        print(f"Definition of {word}:{word_data[word]['definition']}")
        print(f"Opposite of {word}:{','.join(word_data[word]['opposite'])}")
    else:
        print(f"the word '{word}'is not in dictionary[._.]")

def add_new_word():
    word = input("Enter the new word:").lower()
    if word in word_data:
        print(f"The word '{word}'already in the dictionary")
    else:
        definition = input(f"Enter the definition of '{word}'['-']")
        opposites = input(f"Enter the opposite of '{word}'").split()
        word_data[word] = {
            "definition":definition,
            "opposites":[opposite.strip() for opposite in opposites]

        }
        print(f"The word '{word} has been added!!!'")
def print_menu():
    print("Dic/The saurus")
    print("1.look up word")
    print("2.add word")
    print("3.Exit")
def main():
    while True:
        print_menu()
        choice = input("Choose an option(1/2/3):")
        if choice =='1':
            look_word()
        elif choice == '2':
            add_new_word()
        elif choice =='3':
            print("!!!BYE!!!")
            break
        else:
            print("you son of bitch")
      
if __name__ == "__main__":
      main()