import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'computer', 'programming', 'keyboard']
    return random.choice(words)

def display(word, guessed):
    return ' '.join([letter if letter in guessed else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed = set()
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord:", display(word, guessed))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed:
            print("You've already guessed that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

        if all(letter in guessed for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    hangman()