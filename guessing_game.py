# guessing game
# specify a secret word and the user can interact to try to guess the secret word

import random

give_clue = {

    "Giraffe": ["mammal", "herbivore", "yellow polkadots"],
    "Cat": ["domestic", "cute", "low maintenance"],
    "Chicken": ["morning", "jollibee", "cuckucuroookook"]

}

secret_word = random.choice(list(give_clue.keys()))
clue = give_clue[secret_word]
user_guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

# while the user has not guessed the word & guess limit is not reached
while user_guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        user_guess = input("Enter your guess: ")
        if user_guess != secret_word:
            try:
                blues_clues = random.choice(clue)
                print(f"Here is a clue: {blues_clues}")
                clue.remove(blues_clues)
            except:
                if guess_count != guess_limit-1:
                    print("No more clues :(")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print(f"You lost! The word was {secret_word}")
else:
    print("You have guessed the word!")

# Bugs in the code
# Repeated clues
# Clue still given even after guess has run out
