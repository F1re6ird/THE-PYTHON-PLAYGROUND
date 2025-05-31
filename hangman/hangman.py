def play_hangman():
    
    import random
    from words import data

    hangman = [
        """
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
       /|
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =========
        """,
        """
        +---+
        |   |
            |
            |
            |
            |
        =========
        """,
        """
        +---+
            |
            |
            |
            |
            |
        =========
        """
    ]


    victory = """
        +---+
            |
            |
        \O/ |
         |  |
        /\  |
        =========
    """


    flag = True

    while flag:
        
        word_bank = random.choice(data)
        word = word_bank['word']
        category = word_bank['categories']
        
        lives = 7
        guessed_letters = []
        selected = []
        
        print("Please input (y) to continue (n) to stop playing")
        
        play = input("Play game? ")
        if play.lower() == "y":
            while lives > 0:
                print(hangman[lives])
                print(f"Hint word is a {", ".join(category)}")
                print()
                print("Guessed letters:", ", ".join(guessed_letters))
                print()

                dummy_word = ""
                for n in word:
                    if n in selected:
                        dummy_word += n
                    else:
                        dummy_word += "_"
                    
                        
                if dummy_word == word:
                    print("You've won!!!")
                    print()
                    print(victory)
                    print()
                    print(f"The word was: {word.upper()}")
                    print("Game Over. Returning to main menu.\n")
                    break
                print("Word:", " ".join(dummy_word).upper())

                print()
                
                guess = input(f"guess the letter: ")
                if not guess.isalpha() or len(guess) != 1:
                    print("! Please enter a single valid letter.")
                    print()
                    continue
                
                if guess in guessed_letters:
                    print()
                    print(f"{guess.capitalize()} is already a guessed letter")
                    print()
                    continue
                
                elif guess in word:
                    if guess in selected:
                        print(f"You already discovered '{guess}'. Try another letter.")
                        continue
                    selected.append(guess)
                    guessed_letters.append(guess)
                    continue
                else:
                    guessed_letters.append(guess)
                    lives -= 1
                    if lives == 0:
                        print(hangman[lives])
                        print()
                        print(f"The word was: {word.upper()}")
                        print("Game Over. Returning to main menu.")
                        print()
                        break
        elif play.lower() == "n":
            flag = False
        else:
            continue

if __name__ == "__main__":
    play_hangman()
