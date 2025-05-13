menu = {
    "espresso": {
        "price": 2.50, 
        "ingredients": {
            "Water": 50, "Coffee": 18, "Milk": 0
        }
    },
    "cappuccino": {
        "price": 3.50, 
        "ingredients": {
            "Water": 150, "Coffee": 24, "Milk": 100
        }
    },
    "latte": {
        "price": 4.00,
        "ingredients": {
            "Water": 200, "Coffee": 24, "Milk": 150
        }
    }
}

game_over = True
resources = {
    "Water" : 300,
    "Coffee" : 150,
    "Milk" : 200
}
profit = 0

def generate_report():
    print(f"Water: {resources['Water']}\nCoffee: {resources['Coffee']}\nMilk: {resources['Milk']}\n")
    if profit > 0:
        print(f"Profit: {profit}")


def resource_efficiency(order):
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry there is no enough of {item}")
            return None
        else:
            resources[item] = resources[item] - order[item]
    return resources
    
def refill_resources():
    global resources
    print("🔄 Refilling the machine....!!\n")
    resources = {
        "Water" : 300,
        "Coffee" : 150,
        "Milk" : 200
    }

def money():
    quarters = int(input("How many quarters\n"))
    dimes = int(input("How many dimes\n"))
    nickels = int(input("How many Nickels\n"))
    pennies = int(input("How many pennies\n"))
    return round((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01), 2)

def calculate_change(price, cost):
    return round(price - cost, 2)

def coffee_order():
    global resources, profit, game_over
    order = input("What would you like? (espresso/latte/cappuccino) | 'report' | 'refill' | 'exit'\n").lower()
    if order == 'report':
        generate_report()
    
    elif order in menu:  
        temp_resources = resource_efficiency(menu[order]["ingredients"])
        if temp_resources == None:
            print(f"Not efficient resources")
        else:
            price = money()
            cost = menu[order]['price']
            while price < cost:
                print(f"Not efficient money\nInsert {(cost-price)} more money")
                additional_money = money()
                price = additional_money + price
            resources = temp_resources
            print(f"Here is your change {calculate_change(price, cost)}")
            profit += cost
            print(f"Here is your {order}!!Enjoy ☕")
    elif order == 'exit':
        game_over = False
        print(f"👋 Exiting the coffee machine. Have a great day! ☕")
    elif order == 'refill':
        refill_resources()
    else:
        print(f"Print a valid input")

while game_over:
    coffee_order()
