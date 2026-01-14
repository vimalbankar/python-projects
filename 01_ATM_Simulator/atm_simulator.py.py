def setup_password(account):
    """Set password for first-time user"""
    print("---- First Time Setup: Create Password ----")
    while True:
        password = input("Create a password: ").strip()
        confirm = input("Confirm password: ").strip()

        if password != confirm:
            print("Passwords do not match. Try again.\n")
        elif len(password) < 6:
            print("Password must be at least 6 characters.\n")
        else:
            account['password'] = password
            print("Password set successfully!\n")
            break


def login_password(account, max_attempts=3):
    """Verify password before PIN authentication"""
    attempts = 0
    while attempts < max_attempts:
        pwd = input("Enter your password: ").strip()
        if pwd == account['password']:
            print("Password verified!\n")
            return True
        else:
            attempts += 1
            print(f"Incorrect password. Attempts left: {max_attempts - attempts}")

    print("Too many incorrect password attempts. Access denied.")
    return False


def authenticate(account, max_attempts=3):
    """Authenticate user by PIN with limited attempts"""
    attempts = 0
    while attempts < max_attempts:
        pin_input = input("Enter your 4-digit PIN: ").strip()

        if not (pin_input.isdigit() and len(pin_input) == 4):
            print("PIN must be exactly 4 digits.")
            attempts += 1
            continue

        if pin_input == account['pin']:
            print("PIN verified successfully!\n")
            return True
        else:
            attempts += 1
            print(f"Incorrect PIN. Attempts left: {max_attempts - attempts}")

    print("Too many incorrect PIN attempts. Card blocked.")
    return False


def show_menu():
    print("========== ATM MENU ==========")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Transaction History")
    print("6. Exit")
    print("==============================")
    return input("Enter your choice (1-6): ").strip()


def check_balance(account):
    print(f"Current Balance: ₹{account['balance']:.2f}\n")


def deposit(account):
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Invalid amount.\n")
            return
        account['balance'] += amount
        account['history'].append(f"Deposited ₹{amount:.2f}")
        print("Deposit successful.\n")
    except ValueError:
        print("Enter valid numeric amount.\n")


def withdraw(account):
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0 or amount > account['balance']:
            print("Invalid or insufficient balance.\n")
            return
        account['balance'] -= amount
        account['history'].append(f"Withdrawn ₹{amount:.2f}")
        print("Please collect your cash.\n")
    except ValueError:
        print("Enter valid numeric amount.\n")


def change_pin(account):
    old_pin = input("Enter current PIN: ").strip()
    if old_pin != account['pin']:
        print("Wrong PIN.\n")
        return

    new_pin = input("Enter new 4-digit PIN: ").strip()
    confirm = input("Confirm new PIN: ").strip()

    if new_pin != confirm or not new_pin.isdigit() or len(new_pin) != 4:
        print("PIN validation failed.\n")
        return

    account['pin'] = new_pin
    account['history'].append("PIN changed")
    print("PIN updated successfully.\n")


def show_history(account):
    if not account['history']:
        print("No transactions yet.\n")
        return
    print("Transaction History:")
    for h in account['history']:
        print("-", h)
    print()


def main():
    account = {
        'pin': "1234",
        'balance': 5000.0,
        'history': [],
        'password': None
    }

    print("Welcome to Secure Python ATM\n")

    # First time password setup
    if account['password'] is None:
        setup_password(account)

    # Password verification
    if not login_password(account):
        return

    # PIN authentication
    if not authenticate(account):
        return

    while True:
        choice = show_menu()

        if choice == '1':
            check_balance(account)
        elif choice == '2':
            deposit(account)
        elif choice == '3':
            withdraw(account)
        elif choice == '4':
            change_pin(account)
        elif choice == '5':
            show_history(account)
        elif choice == '6':
            print("Thank you for using Python ATM.")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
