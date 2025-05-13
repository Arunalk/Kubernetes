import random

# Global Variables
EASY_TURNS = 10  # Attempts for easy mode
HARD_TURNS = 5   # Attempts for hard mode
CHOICES = 0  # Total attempts based on difficulty
TURNS = 0  # Remaining attempts
REAL_VALUE = 0  # Number to guess

def choose_difficulty():
    global CHOICES, TURNS, REAL_VALUE
    print("Welcome to the Guessing Game!!\nI'm thinking of a number between 1 and 100.")
    
    REAL_VALUE = random.randint(1, 100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    CHOICES = EASY_TURNS if difficulty == 'easy' else HARD_TURNS
    TURNS = CHOICES 
    print(f"You have {CHOICES} attempts.")

def guess_game():
    global TURNS

    while TURNS > 0:
        guess = int(input("Make a guess: "))
        if guess == REAL_VALUE:
            print(f"You got it! The answer was {guess}.")
            return  # Exit function after correct guess

        TURNS -= 1
        print("Too high") if guess > REAL_VALUE else print("Too low")
        if TURNS != 0:
            print(f"Guess again: You have {TURNS} attempts remaining.")

    print(f"You've run out of guesses! The correct answer was {REAL_VALUE}. Play again.")

def main():
    choose_difficulty()
    guess_game()

if __name__ == "__main__":
    main()