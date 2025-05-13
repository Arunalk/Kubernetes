import random
word_list = ["blue", "queen", "butterfly", "orion", "constellation"]
computer_choice = random.choice(word_list)
print(computer_choice)
# placeholder = "_" * len(computer_choice)
# display = list(placeholder)
# print(placeholder)
# game_over = False
# while not game_over:
#     i = 0
#     guess = input("Guess a letter\n")
#     for letter in computer_choice:
#         if letter == guess:
#             print("Right!")
#             display[i] = letter 
#         else:
#             print("Wrong!")
#         i += 1
#     if "_" not in display:
#         game_over = True
#     print(''.join(display))


# Hangman ASCII Art Stages
# Reversed Hangman ASCII Art Stages
stages = [
    r'''  
  ------
  |    |
  O    |
 /|\   |
 / \   |
       |
 ========
    ''', 
    r'''  
  ------
  |    |
  O    |
 /|\   |
 /     |
       |
 ========
    ''',
    r'''  
  ------
  |    |
  O    |
 /|\   |
       |
       |
 ========
    ''',
    r'''  
  ------
  |    |
  O    |
 /|    |
       |
       |
 ========
    ''',
    r'''  
  ------
  |    |
  O    |
  |    |
       |
       |
 ========
    ''',
    r'''  
  ------
  |    |
  O    |
       |
       |
       |
 ========
    ''',
    r'''  
  ------
  |    |
       |
       |
       |
       |
 ========
    '''
]

placeholder = "_" * len(computer_choice)
display = ""
print(placeholder)
game_over = False
correct_letters = []
lives = 6
while not game_over:
    print(f"You've have *********{lives}/6*********** left")
    guess = input("Guess a letter\n").lower()
    display = ""
    if guess in correct_letters:
        print(f"You've already guessed this letter: {guess}")
    for letter in computer_choice:
        if letter == guess:
            print("Right!")
            display += letter 
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in computer_choice:
        lives-=1
        if lives == 0:
            game_over = True
            print(f"********It was {computer_choice} You lose :(*******")
       
    print(f"Current guess: {display}")
    if "_" not in display:
        game_over = True
        print("********You Win!!**********")
    print(stages[lives]) 