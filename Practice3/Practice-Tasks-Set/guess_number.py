"""An interactive guess-the-number game."""

from random import randint


def play_guess_number():
    """Run the game until the player guesses the secret number."""
    name = input("Hello! What is your name?\n")
    secret_number = randint(1, 20)
    guesses = 0
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    while True:
        try:
            guess = int(input("Take a guess.\n"))
        except ValueError:
            print("Please enter a whole number.")
            continue
        guesses += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break


if __name__ == "__main__":
    # Here is the game start point.
    play_guess_number()
