calculator = ''' 
  ___________________  
 |  _________________  |  
 | |      C A L C     | |  
 | |_________________| |  
 |  ___  ___  ___  ___  |  
 | | 7 | 8 | 9 | ÷ | |  
 | |___|___|___|___| |  
 | | 4 | 5 | 6 | × | |  
 | |___|___|___|___| |  
 | | 1 | 2 | 3 | − | |  
 | |___|___|___|___| |  
 | | 0 | . | = | + | |  
 | |___|___|___|___| |  
 |___________________|  

'''
def add(num1, num2):
    return num1 + num2
def diff(num1, num2):
    return num1 - num2
def div(num1, num2):
    return num1//num2
def multiply(num1, num2):
    return num1 * num2
operators= {
    "+": add,
    "-": diff,
    "*": multiply,
    "/": div
    }
def calc():
    print(calculator)
    Continue = True
    result = 0
    number1 = int(input("What's the first number\n"))
    while Continue:
        print("+\n-\n*\n/")
        operator = (input("Pick an operation\n"))
        number2 = int(input("What's the next number\n"))
        if operator in operators:
            result = operators[operator](number1, number2)
            # if operator == '+':
            #     result = add(number1, number2)
            # elif operator == '-':
            #     result = diff(number1, number2)
            # elif operator == '/':
            #     result = div(number1, number2)
            # elif operator == '*':
            #     result = multiply(number1, number2)
        else:
            print("Provide a valid operator")
            return
        print(f"{number1} {operator} {number2} = {result}\n")
        number1 = result
        Continue = (input(f"Would you like to continue with {result} type 'yes' or if you want begin new calculation type 'no'\n") == 'yes')
        if Continue == False:
            print("\n"*10)
            calc()  # Recursion

calc()