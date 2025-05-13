letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# action = input("What action do u wish to perform\n").lower()
# message = input(f"what's the message you wish to {action}\n").lower()
# shift = input("how many numbers do u want to shift\n")

# def encrypt(message, shift):
#     encrypted_message = ""
#     # encrypted_message = []
#     for letter in message:
#         current_index = letters.index(letter)
#         new_index = (current_index + int(shift)) % len(letters)  ## ==> To handle index out of range error
#         # print(len(letters))
#         # encrypted_message.append(letters[new_index])
#         encrypted_message+=letters[new_index]
#     print(str(encrypted_message))
#     # print("".join(encrypted_message))

# def decrypt(message, shift):
#     decrypted_message = ""
#     # encrypted_message = []
#     for letter in message:
#         current_index = letters.index(letter)
#         new_index = (current_index - int(shift)) % len(letters)  ## ==> To handle index out of range error
#         # print(len(letters))
#         # encrypted_message.append(letters[new_index])
#         decrypted_message+=letters[new_index]
#     print(str(decrypted_message))
#     # print("".join(encrypted_message))


# if action == "encrypt":
#     encrypt(message= message, shift= shift)
# elif action == "decrypt":
#     decrypt(message= message, shift= shift)
# else:
#     print(f"Unknown action")

def caesar(message, action, shift):
    output = ""
    for letter in message:
        new_index = shift
        if letter not in letters:
            output += letter
        else:
            if action == "decrypt":
                new_index = -1 * shift
            new_index = letters.index(letter) + new_index
            new_index = new_index % len(letters)
            output += letters[new_index]
    print(f"{action} message: {output}")

should_continue = True
while should_continue:
    action = input("What action do you wish to perform\n").lower()
    message = input(f"What's the message you wish to {action}\n").lower()
    shift = int(input("How many numbers do you want to shift\n"))
    caesar(message=message, action=action, shift=shift)
        
    restart = input("Want to continue? yes or no\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!!")