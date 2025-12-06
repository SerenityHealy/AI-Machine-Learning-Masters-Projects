def welcome_screen():
    print("\n--- Welcome/Login Screen ---")
    print("1. Log In")
    print("2. Forgot Password")
    print("3. Create / Guest Access")
    while True:
        choice = input("Select an option (1-3): ")
        if choice == "1":
            print("\nLog In successful! Redirecting to Options Screen...")
            options_screen()
            break
        elif choice == "2":
            print("\nForgot Password selected. Please check your email for reset instructions.")
        elif choice == "3":
            print("\nAccessing as Guest... Redirecting to Options Screen...")
            options_screen()
            break
        else:
            print("Invalid choice. Please select a valid option (1-3).")

def options_screen():
    print("\n--- Options Screen ---")
    print("1. Create New List")
    print("2. View Saved Lists")
    print("3. Edit Previous Lists")
    print("4. Go to Price Comparison Screen")
    print("5. Exit")
    while True:
        choice = input("Select an option (1-5): ")
        if choice == "1":
            new_grocery_list()
            break
        elif choice == "2":
            saved_lists_screen()
            break
        elif choice == "3":
            saved_lists_screen(edit_mode=True)
            break
        elif choice == "4":
            price_comparison_screen()
            break
        elif choice == "5":
            print("Exiting the app. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

def new_grocery_list():
    print("\n--- New Grocery List ---")
    print("Organize your list by categories (Fruits, Meat, Dairy, etc.)")
    print("Type 'done' when finished.")
    grocery_list = []
    while True:
        item = input("Add an item to your list: ")
        if item.lower() == 'done':
            break
        grocery_list.append(item)
    print("\nYour Grocery List:")
    for idx, item in enumerate(grocery_list, start=1):
        print(f"{idx}. {item}")
    print("\nReturning to Options Screen...\n")
    options_screen()

def saved_lists_screen(edit_mode=False):
    print("\n--- Saved Grocery Lists ---")
    saved_lists = [
        "The Cookout BBQ",
        "Birthday Party 8/3/25",
        "12/20/24 Grocery List",
        "11/10/24 Grocery List",
        "Halloween Party"
    ]
    for idx, lst in enumerate(saved_lists, start=1):
        print(f"{idx}. {lst}")
    if edit_mode:
        print("\nEdit mode active: Select a list to edit.")
    else:
        print("\nSelect a list to view its details.")
    input("Press Enter to return to the Options Screen.")
    options_screen()

def price_comparison_screen():
    print("\n--- Price Comparison Screen ---")
    stores = [
        {"name": "Aldi", "price": "$204.48"},
        {"name": "Costco", "price": "$223.99"},
        {"name": "Walmart", "price": "$244.29"},
        {"name": "Target", "price": "$247.88"},
        {"name": "Whole Foods", "price": "$250.73"}
    ]
    for idx, store in enumerate(stores, start=1):
        print(f"{idx}. {store['name']} = {store['price']}")
    print("\nSelect a store number for more details or press Enter to return to the Options Screen.")
    input("Press Enter to return to the Options Screen.")
    options_screen()

welcome_screen()
