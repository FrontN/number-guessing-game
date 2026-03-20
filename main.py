from number_guessing_art import logo
import random
import time
import os

TOTAL_NB ={
    "easy": 10,
    "hard": 100
}

ATTEMPTS = {
    "easy": 5,
    "hard": 3
}

def clear_screen():
    """Clear the terminal screen and print the logo.
    
    This function clears the terminal screen on both Windows and Unix systems and then prints the logo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

def download():
    """Print a loading animation of three dots, each separated by a second of delay."""
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

def get_valid_input(prompt, valid_options):
    """
    Prompts the user for input and validates it against a list of valid options.

    Parameters:
    prompt (str): The message to display to the user when asking for input.
    valid_options (list): A list of valid options that the user's input must match.

    Returns:
    str: The valid input entered by the user.
    """
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")
            time.sleep(1.5)
            clear_screen()

def get_game_settings():
    """
    Clears the terminal screen and prompts the user to choose a difficulty.
    Then it sets the total number of guesses and the number of attempts based on the difficulty.
    Finally, it returns a random number between 1 and the total number, the total number, and the number of attempts.
    """
    clear_screen()
    difficulty = get_valid_input("Choose a difficulty. Type 'easy' or 'hard': ", ['easy', 'hard'])
    total_nb = TOTAL_NB[difficulty]
    attempts = ATTEMPTS[difficulty]
    return random.randint(1, total_nb), total_nb, attempts

def play_round(target, max_range, attempts):
    """
    Plays a round of the number guessing game.

    Prompts the user for input and validates it against a list of valid options.
    Then it sets the total number of guesses and the number of attempts based on the difficulty.
    Finally, it returns a random number between 1 and the total number, the total number, and the number of attempts.

    Parameters:
    target (int): The number to guess.
    max_range (int): The highest number that can be guessed.
    attempts (int): The number of attempts remaining to guess the number.

    Returns:
    bool: True if the user guessed the number, False otherwise.
    """
    clear_screen()
    tried_number = set()
    print(f"I'm thinking of a number between 1 and {max_range} ", end="")
    download()
    while attempts > 0:
        try:
            clear_screen()
            if tried_number:
                print(f"You've already tried: {sorted(list(tried_number))}")
            user_guess = int(input(f"You have {attempts} attempts remaining to guess the number. Make a guess: "))
        except ValueError:
            print("Only numbers are allowed")
            time.sleep(1.5)
            continue
            
        if user_guess > max_range or user_guess < 1:
            print(f"Out of range. please insert a number between 1 and {max_range}")
            time.sleep(1.5)
            clear_screen()
            continue

        if user_guess in tried_number:
            print(f"{user_guess}! You've already tried that number. Please try a different one.")
            time.sleep(1.5)
            clear_screen()
            continue

        if user_guess == target:
            clear_screen()
            print(f"You got it! The answer was {target}")
            return True
        
        attempts -= 1
        hint = "Too high" if user_guess > target else "Too low"
        if attempts > 0:
            print(f"{hint}. Try again")
            tried_number.add(user_guess)
            time.sleep(1.5)
    clear_screen()
    print(f"Game Over. The right answer was {target}")
    return False

def main():
    """Main entry point of the number guessing game.
    
    Initializes the game, prompts the user to play again, 
    and keeps track of the user's current streak.
    """
    score = 0
    clear_screen()
    print("Welcome to the number guessing game")
    time.sleep(1.5)
    keep_going = True

    while keep_going:
        nb_to_guess, total_nb, nb_attempts = get_game_settings()
        won = play_round(nb_to_guess, total_nb, nb_attempts)
        if won:
            score += 1
        else:
            score = 0

        print(f"Your current Streak: {score}")
        choice = get_valid_input("Do you want to play again? Type 'y' or 'n': ", ['y', 'yes', 'no', 'n'])
        if choice.startswith('n'):
            print("See You")
            break

if __name__ == "__main__":
    main()
