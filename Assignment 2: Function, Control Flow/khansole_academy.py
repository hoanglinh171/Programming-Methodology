"""
File: khansole_academy.py
-------------------------
Generate two random numbers. The user need to guess their sum. If they guess correctly for CORRECT_TIMES consecutively,
the game will stop with "Congratulations
"""

import random


CORRECT_TIMES = 3
MAX, MIN = 99, 10


def main():
    n = 0
    while True:
        # generate problems and solutions
        rand1 = random.randint(MIN, MAX)
        rand2 = random.randint(MIN, MAX)
        total = rand1 + rand2
        print("What is", rand1, "+", rand2, "?")
        # take user input for answer
        answer = int(input("Your answer: "))
        # assess validity
        if answer == total:
            n += 1  # count correct times
            print("Correct! You've got", n, "correct in a row")
            if n == CORRECT_TIMES:
                print("Congratulations! You've mastered addition!")
                break
        else:
            n = 0  # reset the streak to 0 when user answers wrong
            print("Incorrect, the expected answer is", total)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
