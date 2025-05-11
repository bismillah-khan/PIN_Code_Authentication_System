
def set_pin():
    while True:
        new_pin = input("Set your 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            print("PIN set successfully!\n")
            return new_pin
        else:
            print("Invalid PIN! Please enter exactly 4 digits.\n")
def authenticate(pin):
    attempts = 0
    while attempts < 3:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == pin:
            print("Access Granted")
            return
        else:
            attempts += 1
            if attempts < 3:
                print("Incorrect PIN! Try again.\n")
            else:
                print("Too many incorrect attempts! Access Denied.")

def main():
    user_pin = set_pin()
    authenticate(user_pin)

if __name__ == "__main__":
    main()