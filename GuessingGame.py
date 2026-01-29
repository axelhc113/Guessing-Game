# Name: Axel Hidrovo
# Course: CIS261
# Lab: Guessing Game

import random


def display_heading():
    print("===================================")
    print("        Number Guessing Game       ")
    print("===================================\n")
def get_limit():
    while True:
        value = input("Enter a limit (whole number greater than 1): ")
        try:
            limit = int(value)
            if limit > 1:
                return limit
            print("Limit must be greater than 1.\n")
        except ValueError:
            print("Please enter a valid whole number.\n")

def get_guess():
    while True:
        value = input("Enter your guess: ")
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid whole number.\n")
def play_game(limit):
    secret = random.randint(1, limit)

    # Message showing range to be guessed
    print(f"\nI'm thinking of a number from 1 to {limit}.\n")

    # Loop: prompt user, compare guess, retry until correct
    while True:
        guess = get_guess()

        if guess > secret:
            print("Too high. Try again.\n")
        elif guess < secret:
            print("Too low. Try again.\n")
        else:
            print(f"Correct! The number was {secret}.\n")
            break

def ask_play_again():
        while True:
            choice = input("Play again? (y/n): ").strip().lower()
            if choice in ("y", "n"):
                return choice
            print("Please enter y or n.\n")

def main():
    display_heading()

    while True:
        limit = get_limit()
        play_game(limit)

        if ask_play_again() == "n":
            print("Goodbye!")
            break
        print()  # blank line before next round


if __name__ == "__main__":
    main()