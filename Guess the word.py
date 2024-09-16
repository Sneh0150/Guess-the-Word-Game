import random

# Step 1: List of words
words = ["baboon", "monkey", "camel","donkey","elephant"]

# Step 2: Randomly choose a word from the list
chosen_word = random.choice(words)

# Step 3: Create a list of blanks
blanks = ["_"] * len(chosen_word)

# Step 4: Set the number of chances and initialize variables
max_chances = 5
wrong_guesses = 0
guessed_letters = []

# Step 5: Game loop
while wrong_guesses < max_chances:
    # Display the current state of blanks
    print(f"Word to guess: {' '.join(blanks)}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the guess is valid (a single letter)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a valid single letter.")
        continue
    
    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        # Replace blanks with the guessed letter where it appears
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                blanks[i] = guess
        print(f"Good guess! '{guess}' is in the word.")

    else:
        # Increment wrong guesses if the guess is incorrect
        wrong_guesses += 1
        print(f"Wrong guess! '{guess}' is not in the word. You have {max_chances - wrong_guesses} chances left.")

    # Check if the user has guessed all the letters
    if "_" not in blanks:
        print(f"Congratulations! You guessed the word: {''.join(blanks)}")
        break

# If the user runs out of chances
if wrong_guesses == max_chances:
    print(f"Game Over! You've run out of chances. The word was '{chosen_word}'.")