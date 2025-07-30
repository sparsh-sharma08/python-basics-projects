def ai_guess_number():
    low = 1
    high = 100
    attempts = 0

    print("Think of a number between 1 and 100. I’ll guess it!")

    input("Press Enter when you're ready...")

    while low <= high:
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

        if feedback == 'c':
            print(f"I guessed your number in {attempts} tries!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input. Use H, L, or C.")

ai_guess_number()
