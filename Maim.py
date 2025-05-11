# main.py

# Set the correct 4-digit PIN
CORRECT_PIN = "1234"

# Number of allowed attempts
MAX_ATTEMPTS = 3

# Track the number of attempts
attempts = 0

while attempts < MAX_ATTEMPTS:
    user_input = input("Enter 4-digit PIN: ")
    
    if user_input == CORRECT_PIN:
        print("Access Granted")
        break
    else:
        attempts += 1
        if attempts < MAX_ATTEMPTS:
            print("Incorrect PIN! Try again.")
        else:
            print("Too many incorrect attempts! Access Denied.")
