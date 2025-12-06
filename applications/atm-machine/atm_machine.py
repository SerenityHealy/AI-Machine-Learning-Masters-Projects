def run_atm():
    correct_pin = "1234"
    pin_attempts = 0
    max_attempts = 3
    balance = 100.0

    print("Hello, Welcome to the ATM! Please Insert Your Card to Start.")

    insert_card = input("Insert Card? (y/n): ").strip().lower()
    if insert_card != 'y':
        print("No card inserted. Exiting.")
        return

    while True:
        entered_pin = input("Enter your PIN: ").strip()
        if entered_pin == correct_pin:
            print("PIN accepted.")
            break
        else:
            pin_attempts += 1
            print(f"Incorrect PIN. Attempts so far: {pin_attempts}")
            if pin_attempts >= max_attempts:
                print("Maximum PIN attempts exceeded. Card retained. Exiting.")
                return

    while True:
        if balance == 0:
            print("Account balance is zero. Account is now closed.")
            print("Session ended.")
            return

        print(f"\nCurrent balance: ${balance:.2f}")
        print("What would you like to do?")
        print("1) Withdraw")
        print("2) Deposit")
        print("3) Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == '1':
            amount_str = input("Enter withdrawal amount: $").strip()
            try:
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount entered. Transaction canceled.")
                continue

            if amount <= 0:
                print("Cannot withdraw zero or a negative amount.")
            elif amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")

        elif choice == '2':
            amount_str = input("Enter deposit amount: $").strip()
            try:
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount entered. Transaction canceled.")
                continue

            if amount <= 0:
                print("Cannot deposit zero or a negative amount.")
            else:
                balance += amount
                print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")

        elif choice == '3':
            print("Thank you for using the ATM your session has now ended.")
            return

        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    run_atm()

