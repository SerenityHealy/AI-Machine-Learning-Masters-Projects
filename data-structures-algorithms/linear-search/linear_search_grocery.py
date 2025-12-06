def linear_search(database, target):
    for index, item in enumerate(database):
        if item.lower() == target.lower():
            return index
    return -1


def main():
    database = [
                   "Apples", "Avocados", "Bananas", "Berries", "Carrots", "Chicken",
                   "Ground Beef", "Hot Dogs", "Fish", "Salmon", "Shrimp", "Tilapia",
                   "Ice Cream", "Pizza", "Potatoes", "Corn", "Rice", "Pasta",
                   "Tomatoes", "Spinach", "Cereal", "Milk", "Butter", "Cheese",
                   "Eggs", "Soda", "Juice", "Coffee", "Tea", "Water", "Sugar",
                   "Flour", "Baking Soda", "Chocolate Chips", "Cake Mix",
                   "Honey", "Peanut Butter", "Jam", "Vinegar", "Soy Sauce",
                   "Salt", "Pepper", "Spices", "Napkins", "Paper Towels",
                   "Toothpaste", "Shampoo", "Conditioner", "Laundry Detergent",
                   "Dish Soap", "Batteries", "Light Bulbs", "Onions", "Brussel Sprouts" "Cucumbers"
        ]

    print("Hello! Welcome to the Online Marketplace Grocery Search Tool!")

    print("Type 'exit' anytime to quit the search.\n")

    while True:
        target_item = input("Enter the grocery item you are looking for: ").strip()

        if target_item.lower() == 'exit':
            print("Thank you for using the Online Marketplace Grocery Search Tool. Bye!")
            break

        result = linear_search(database, target_item)

        if result != -1:
            print(f"'{target_item}' was found in the database at index {result}.")
        else:
            print(f"Sorry, '{target_item}' was not found in the database.")

        print()  # Add a blank line for better readability


if __name__ == "__main__":
    main()
