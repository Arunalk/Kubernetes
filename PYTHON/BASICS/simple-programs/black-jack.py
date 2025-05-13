import random
black_jack = r'''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      '------'                           |__/   
'''
def choose_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def caculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) >= 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!!"
    elif computer_score == 0:
        return "Lose, Opponent has blackjack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "Lose, You went over 21!"
    elif computer_score > 21:
        return "Win, Opponent went over 21!"
    elif user_score > computer_score:
        return "You win!!"
    elif user_score == 21:
        return "You win!!"
    else:
        return "You Lose!"

def blackjack():
    print(black_jack)
    user_card = []
    computer_card = []
    computer_score = -1
    user_score = -1
    game_over = False
    for i in range(2):
        user_card.append(choose_card())
        computer_card.append(choose_card())

    while not game_over:
        user_score = caculate_score(user_card)
        computer_score = caculate_score(computer_card)
        print(f"Your cards: {user_card}, Current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_deal = input("Type 'yes' to get another card or 'no' to pass\n")
            if user_deal == 'yes':
                user_card.append(choose_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(choose_card())
        computer_score = caculate_score(computer_card)

    print(f"Your final hand {user_card}, Final Score {user_score}")
    print(f"Computer's final hand {computer_card}, Final Computer Score {computer_score}")
    print(compare(user_score, computer_score))

while (input("Do you want to play BlackJack 'yes' or 'no' \n") == 'yes'):
    blackjack()
    print("\n" * 20)