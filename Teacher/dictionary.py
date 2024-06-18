word_data = {
            "happpy":{
                      "definition":"feeling or showing pleasure.",
                      "synonyms": ["joyful","cheerful","dejected"]
                      },
            "sad":{
                      "definition":"feeling or showing sorrow.",
                      "synonyms":["ünhappy","sorrowful","dejected"]
                      },
            "fast":{
                      "definition":"moving or capable of moving at high speed",
                      "synonyms":["quick","speedy","rapid"]
                      }
            }


def look_up_word():
    word = input("Ënter the word you want to look up:").lower()
    if word in word_data:
        print(f"Definition of {word}:{word_data[word]['definition']}")
        print(f"Synonyms of {word}:{', '.join(word_data[word]['synonyms'])}")
    else:
        print(f"The word '{word}''is not in the dictionary.")


def add_new_word():
    word = input("Ënter the new word you want to add:").lower()
    if word in word_data:
        print(f"The word '{word}' already exists in the dictionary.")
    else:
        definition = input(f"Ënter the definition of '{word}':")
        synonyms = input(f"Ënter synonyms of '{word}' separated by commas:").split()
        word_data[word] = {
            "definition":definition,
           "synonyms":[synonym.strip() for synonym in synonyms]
        }
        print(f"The word 'word' has been added to the dictionary.")

def print_menu():
    print("Dictionary/Thesaurus")
    print("1. look up a word")
    print("2. add a new word")
    print("3. Exit")

def main():
    while True:
        print_menu()
        choice = input("Choose an option (1/2/3):" )
        if choice == '1':
            look_up_word()
        elif choice == '2':
            add_new_word()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Ïnvalid choice. Please choose again.")

if __name__ == "__main__":
    main()
