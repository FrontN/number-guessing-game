from number_guessing_art import logo
import random
import time
import os

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

def get_game_settings():
    """Choose a difficulty and return a random number between 1 and total_nb and the attempts remaining.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    int
        Random number between 1 and total_nb
    int
        Total number of attempts remaining
    int
        Number of attempts remaining
    """
    while True:
        clear_screen()
        difficulty = input("Choose a difficulty, type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            total_nb = 10
            attempts = 5
            break

        elif difficulty == 'hard':
            total_nb = 100
            attempts = 3
            break
        else:
            clear_screen()
            print("Non valid option, try again")
            time.sleep(1.5)
    return random.randint(1, total_nb), total_nb, attempts

def play_round(target, max_range, attempts):
    """Play a round of the number guessing game.
    
    Parameters
    ----------
    target : int
        The number to guess
    max_range : int
        The maximum number that can be guessed
    attempts : int
        The number of attempts remaining
    
    Returns
    -------
    bool
        True if the user guessed the number correctly, False if the user ran out of attempts
    """
    tried_number = set()
    while attempts > 0:
        print(f"I'm thinking of a number between 1 and {max_range} ", end="")
        download()
        try:
            clear_screen()
            if tried_number:
                print(f"You've already tried: {sorted(list(tried_number))}")
            user_guess = int(input(f"You have {attempts} attempts remaining to guess the number. Make a guess: "))
        except ValueError:
            clear_screen()
            print("Only numbers are allowed")
            time.sleep(1.5)
            continue
            
        if user_guess > max_range or user_guess < 1:
            clear_screen()
            print(f"Out of range. please insert a number between 1 and {max_range}")
            time.sleep(1.5)
            continue

        if user_guess in tried_number:
            clear_screen()
            print(f"{user_guess}! You've already tried that number. Please try a different one.")
            time.sleep(1.5)
            continue

        if user_guess == target:
            clear_screen()
            print(f"You got it! The answer was {target}")
            return True
        
        clear_screen()
        attempts -= 1
        hint = "Too high" if user_guess > target else "Too low"
        if attempts > 0:
            print(f"{hint}. Try again")
            tried_number.add(user_guess)
            time.sleep(1.5)

    print(f"Game Over. The right answer was {target}")
    return False

def main():
    """Main entry point of the number guessing game.
    
    Initializes the game, prompts the user to play again, 
    and keeps track of the user's current streak.
    """
    score = 0
    print(logo)
    print("Welcome to the number guessing game")
    time.sleep(2)
    keep_going = True

    while keep_going:
        nb_to_guess, total_nb, nb_attempts = get_game_settings()
        won = play_round(nb_to_guess, total_nb, nb_attempts)
        if won:
            score += 1
        else:
            score = 0

        print(f"Your current Streak: {score}")
        choice = input("Play again? (y/n): ").lower()
        if not choice.startswith('y'):
            print("See You")
            break

if __name__ == "__main__":
    main()