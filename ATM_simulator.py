import datetime
import getpass

# user data management
users = {}

# log transaction
def log_transaction(user, action, amount):
    timestamp = datetime.datetime.now()
    print(f"{timestamp}: {user} - {action} ${amount:.2f}")

# register a user
def register_user():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already taken. Please try another.")
        return False
    else:
        password = getpass.getpass("Enter a new password: ")
        users[username] = {'password': password, 'balance': 0.0, 'categories': {}}
        print("Registration successful!")
        return True

# authenticate user info
def authenticate_user(username, password):
    if username in users and users[username]['password'] == password:
        return True
    else:
       return False

# check balance
def check_balance(username):
    balance = users[username]['balance']
    print(f"Your total balance is: ${balance:.2f}")
    return balance

# deposit money
def deposit(username, amount):
    users[username]['balance'] += amount
    log_transaction(username, 'Deposit', amount)
    print(f"Deposited ${amount:.2f}. New balance is ${users[username]['balance']:.2f}.")

# withdraw money
def withdraw(username, amount):
    if users[username]['balance'] >= amount:
        users[username]['balance'] -= amount
        log_transaction(username, 'Withdraw', amount)
        print(f"Withdrew ${amount:.2f}. New balance is ${users[username]['balance']:.2f}.")
    else:
        print("Insufficient funds.")


# ATM simulation program
def atm_program():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")

            if authenticate_user(username, password):
                print(f"Welcome {username}!")
                while True:
                    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Logout")
                    action = input("Choose an option: ")

                    if action == '1':
                        check_balance(username)
                    elif action == '2':
                        amount = float(input("Enter amount to deposit: "))
                        deposit(username, amount)
                    elif action == '3':
                        amount = float(input("Enter amount to withdraw: "))
                        withdraw(username, amount)
                    elif action == '4':
                        print("Logging out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Authentication failed. Please check your username and password.")
        elif choice == '3':
            print("Exiting. Thank you for using our ATM!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    atm_program()