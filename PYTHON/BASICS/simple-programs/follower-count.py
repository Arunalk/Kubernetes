import random

celebrities = [
    {"name": "Cristiano Ronaldo", "followers": 600, "country": "Portugal", "occupation": "Footballer"},
    {"name": "Lionel Messi", "followers": 480, "country": "Argentina", "occupation": "Footballer"},
    {"name": "Kylie Jenner", "followers": 400, "country": "USA", "occupation": "Entrepreneur"},
    {"name": "Dwayne Johnson", "followers": 350, "country": "USA", "occupation": "Actor/Wrestler"},
    {"name": "Ariana Grande", "followers": 320, "country": "USA", "occupation": "Singer"},
    {"name": "Taylor Swift", "followers": 280, "country": "USA", "occupation": "Singer"},
    {"name": "Kim Kardashian", "followers": 330, "country": "USA", "occupation": "Entrepreneur"},
    {"name": "Selena Gomez", "followers": 400, "country": "USA", "occupation": "Singer/Actress"},
    {"name": "Virat Kohli", "followers": 260, "country": "India", "occupation": "Cricketer"},
    {"name": "Beyoncé", "followers": 250, "country": "USA", "occupation": "Singer"},
    {"name": "Justin Bieber", "followers": 290, "country": "Canada", "occupation": "Singer"},
    {"name": "Billie Eilish", "followers": 180, "country": "USA", "occupation": "Singer"},
    {"name": "Zendaya", "followers": 190, "country": "USA", "occupation": "Actress/Singer"},
    {"name": "Drake", "followers": 210, "country": "Canada", "occupation": "Rapper"},
    {"name": "Shah Rukh Khan", "followers": 150, "country": "India", "occupation": "Actor"},
    {"name": "Tom Holland", "followers": 140, "country": "UK", "occupation": "Actor"},
    {"name": "Chris Hemsworth", "followers": 170, "country": "Australia", "occupation": "Actor"},
    {"name": "Robert Downey Jr.", "followers": 130, "country": "USA", "occupation": "Actor"},
    {"name": "LeBron James", "followers": 180, "country": "USA", "occupation": "Basketball Player"},
    {"name": "Roger Federer", "followers": 120, "country": "Switzerland", "occupation": "Tennis Player"},
    {"name": "Conor McGregor", "followers": 100, "country": "Ireland", "occupation": "MMA Fighter"},
    {"name": "Emma Watson", "followers": 140, "country": "UK", "occupation": "Actress"},
    {"name": "Gal Gadot", "followers": 160, "country": "Israel", "occupation": "Actress"},
    {"name": "Rihanna", "followers": 250, "country": "Barbados", "occupation": "Singer"},
    {"name": "Ed Sheeran", "followers": 170, "country": "UK", "occupation": "Singer"},
    {"name": "Miley Cyrus", "followers": 180, "country": "USA", "occupation": "Singer"},
    {"name": "The Weeknd", "followers": 190, "country": "Canada", "occupation": "Singer"},
    {"name": "Shakira", "followers": 220, "country": "Colombia", "occupation": "Singer"},
    {"name": "Priyanka Chopra", "followers": 140, "country": "India", "occupation": "Actress"},
]

logo = r'''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/  

'''
against = r'''
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
'''

def format_data(account):
    account_name = account["name"]
    account_desc = account["occupation"]
    account_place = account["country"]
    return f"{account_name}, {account_desc} , from {account_place}"

def check_answer(user_choice, first_follow_count, second_follow_count):
    if first_follow_count > second_follow_count:
        return user_choice == 'a'
    else:
        return user_choice == 'b'

print(logo)
game_should_continue = True
score = 0
first_celeb = random.choice(celebrities)
while game_should_continue:
    second_celeb = random.choice(celebrities)
    while first_celeb == second_celeb:
        second_celeb = random.choice(celebrities)
    print(f"Compare A: {format_data(first_celeb)}")
    print(against)
    print(f"Against {format_data(second_celeb)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = first_celeb["followers"]
    b_follower_count = second_celeb["followers"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct == True:
        score += 1
        print(f"You're right!! Current score : {score}")
        first_celeb = second_celeb
    else:
        print(f"Sorry that's wrong! Final Score: {score}")
        game_should_continue = False