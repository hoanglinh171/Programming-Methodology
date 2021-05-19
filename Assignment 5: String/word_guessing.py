"""
File: word_guess.py
-------------------
Game: guessing word. The word is generated randomly from a txt file. The players start with a number of guesses. If they
can guess the word correctly within the number of guesses allowed, they win, otherwise, lose
"""


import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """
    guess_word = ""
    guess_count = INITIAL_GUESSES
    for i in range(len(secret_word)):
        guess_word += "-"

    print("The word now look like this: " + str(guess_word))
    print(f"You have {guess_count} guesses left")

    while guess_count >= 0:
        if guess_word.isalpha():
            print(f"Congratulations, the word is: {guess_word}")
            break
        else:
            guess_char = get_guess()
            guess_word = update_word(secret_word, guess_word, guess_char)
            if len(guess_char) == 1:
                guess_count -= 1
            if guess_count >= 0 and guess_word.isalpha():
                print(f"Congratulations, the word is: {guess_word}")
                break
            elif guess_count == 0 and (not guess_word.isalpha()):
                print(f"Sorry, you lost. The secret word was: {secret_word}")
                break
            else:
                print(f"The word now look like this: {guess_word}")
                print(f"You have {guess_count} guesses left.")


def get_guess():
    guess_char = input("Type a single character here, then press enter: ")
    if len(guess_char) > 1:
        print("Guess should only be a single character.")

    return guess_char.upper()


def update_word(secret_word, guess_word, guess_char):  # with repeated char?
    """
    >>> update_word("PYTHON", "------", "T")
    '--T---'
    >>> update_word("PYTHON", "------", "E")
    '------'
    """
    updated_word = guess_word
    if len(guess_char) == 1:
        for i in range(len(secret_word)):
            if guess_char == secret_word[i]:
                updated_word = updated_word[:i] + guess_char + updated_word[i+1:]

        if updated_word != guess_word:
            print("The guess is correct")
        else:
            print(f"There are no {guess_char}'s in the word")

    return updated_word


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    word_list = []
    file = open(LEXICON_FILE)
    for line in file:
        line = str(line.strip())
        word_list.append(line)

    index = random.randrange(0, len(word_list))
    chosen_word = word_list[index]

    return chosen_word


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
