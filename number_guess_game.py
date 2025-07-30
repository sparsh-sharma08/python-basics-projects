import random

def number_guess():
    number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

number_guess()
