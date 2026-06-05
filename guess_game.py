import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

print(Fore.CYAN + "=== Number Guessing Game ===")

# Generate random number
secret_number = random.randint(1, 100)

# Show secret number for testing
print(Fore.GREEN + f"Secret Number is: {secret_number}")

attempts = 0

while True:

    # User input
    guess = int(input(Fore.YELLOW + "Guess a number between 1 and 100: "))

    attempts += 1

    # Conditions
    if guess < secret_number:
        print(Fore.RED + "Too Low! Try Again.")

    elif guess > secret_number:
        print(Fore.RED + "Too High! Try Again.")

    else:
        print(Fore.CYAN + f"Congratulations! You guessed the number in {attempts} attempts.")
        break