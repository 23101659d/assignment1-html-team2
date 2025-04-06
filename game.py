import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")
    
    while True:
        try:
            difficulty = int(input("Enter difficulty (1-3): "))
            if difficulty in [1, 2, 3]:
                break
            print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Enter a number.")

    # Set range based on difficulty
    ranges = {1: 50, 2: 100, 3: 200}
    max_number = ranges[difficulty]
    secret_number = random.randint(1, max_number)
    attempts = 0
    
    print(f"I'm thinking of a number between 1 and {max_number}. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    number_guessing_game()