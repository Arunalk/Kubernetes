import random
guess_number = r'''

 / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  

'''
def guess_game(number_of_choices, real_value):
    while number_of_choices != 0:
        guess = int(input("Make a guess\n"))
        if guess == real_value:
            print(f"You got it! The answer was {guess}.")
            return
        number_of_choices-=1
        if guess > real_value:
            print("Too high")
        if guess < real_value:
            print("Too low")
        if number_of_choices != 0:
            print(f"Guess again: You have {number_of_choices} remaining to guess the number")
    print(f"You have ran out of guesses")

def main():
    print(guess_number)
    print("Welcome to Guessing Game!!\nI'm thinking of a number between 1 and 100.")
    real_value = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        number_of_choices = 10
        print("You have 10 attempts")
    else:
        number_of_choices = 5
        print("You have 5 attempts")
    guess_game(number_of_choices, real_value)

main()