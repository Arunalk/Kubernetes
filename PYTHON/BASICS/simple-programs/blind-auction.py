bidding_art = '''
        💰💰💰  
         |||  
    💵==> 💵==> 💵==> 💵==> 💰💰💰  (Bids increasing)
         |||  
         |||  
        🔨🔨🔨  (Sold!)
'''
print(bidding_art)
def get_bidders():
    print("Welcome to the secret auction program\n")
    Game_over = True
    secret_bidders = {}
    while Game_over:
        name = input("What is your name?\n")
        secret_bidders[name] = int(input("What's your bid?\n"))
        Game_over = bool(input("Are there are other bidders? Type 'yes' or 'no'\n") == 'yes')
        print("\n" * 10) # To clear the screen
    return secret_bidders
def highest_score():
    secret_bidders = get_bidders()
    # max_score=0
    # for key, value in secret_bidders.items():   => without using max function
    #     if value > max_score:
    #         max_score = value
    #         winner = key
    # print(f"The winner is {winner} with a bid of {max_score}")
    max_score=max(secret_bidders)
    print(f"The winner is {max_score} with bid of {secret_bidders[max_score]}")

highest_score()


