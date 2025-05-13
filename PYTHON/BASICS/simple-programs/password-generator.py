# ### PASSWORD GENERATOR
import random
letters = ["q","w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
print(f"Welcome to the PyPassword Generator!")
l = int(input("How many letters would you like to have in your password\n"))
s = int(input("How many symbols would you like to have in your password\n"))
n = int(input("How many numbers would you like to have in your password\n"))
password = []
for char in range(0,l):
    password.append(random.choice(letters))
for sym in range(0, s):
    password.append(random.choice(symbols))
for num in range(0, n):
    password.append(random.choice(numbers))
random.shuffle(password)
print(password)
new_password = ""
for char in password:
    new_password += char
print(new_password)