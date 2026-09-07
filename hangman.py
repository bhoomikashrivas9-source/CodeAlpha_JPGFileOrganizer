import random

def choose_word():
    words = ["python", "hangman", "computer", "keyboard", "internship"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while wrong_guesses < max_wrong:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            wrong_guesses += 1
            print("Wrong guess.")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

    print("\nGame over! The word was:", word)

play_hangman()