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
    Clears the terminal screen and asks the user to choose a difficulty.

    Then it generates a random number between 1 and the total number of options
    and returns it along with the total number of options and the number of attempts.

    Returns:
    tuple: A tuple containing the randomly generated number, the total number of options, and the number of attempts.
    """
    clear_screen()
    difficulty = get_valid_input("Choose a difficulty. Type 'easy' or 'hard': ", ['easy', 'hard'])
    total_nb = TOTAL_NB[difficulty]
    attempts = ATTEMPTS[difficulty]
    return random.randint(1, total_nb), total_nb, attempts

def play_round(target, max_range, attempts):
    """
    Clears the terminal screen and starts a round of number guessing.
    Prints a message with the maximum range of numbers and waits for a second.
    Then it enters a loop where it asks the user to guess a number between 1 and the maximum range.
    If the user guesses a number outside the range, it prints an error message and waits for a second.
    If the user guesses a number they have already tried, it prints an error message and waits for a second.
    If the user guesses the correct number, it prints a success message and returns True.
    If the user uses up all their attempts, it prints a failure message and returns False.

    Parameters:
    target (int): The correct answer to be guessed.
    max_range (int): The maximum range of numbers to be guessed.
    attempts (int): The number of attempts remaining.

    Returns:
    bool: True if the user guesses the correct number, False if they use up all their attempts.
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
