# Linear Search - Online Grocery Search Tool

A demonstration of the linear search algorithm applied to a grocery item database.

## Overview

This program implements a linear search algorithm to find grocery items in a database. It provides an interactive search interface for looking up items in an online marketplace.

## Features

- **Linear Search Implementation**: From-scratch algorithm
- **Case-Insensitive Search**: Matches regardless of capitalization
- **Interactive Loop**: Continuous searching until exit
- **Index Display**: Shows position in database
- **User-Friendly**: Clear feedback for found/not found items
- **Exit Option**: Type 'exit' to quit

## Usage

```bash
python linear_search_grocery.py
```

## Example Session

```
Hello! Welcome to the Online Marketplace Grocery Search Tool!
Type 'exit' anytime to quit the search.

Enter the grocery item you are looking for: apples
'apples' was found in the database at index 0.

Enter the grocery item you are looking for: chocolate chips
'chocolate chips' was found in the database at index 33.

Enter the grocery item you are looking for: pizza
'pizza' was found in the database at index 13.

Enter the grocery item you are looking for: lobster
Sorry, 'lobster' was not found in the database.

Enter the grocery item you are looking for: exit
Thank you for using the Online Marketplace Grocery Search Tool. Bye!
```

## Database Contents

**54 Items** including:
- **Produce**: Apples, Avocados, Bananas, Berries, Carrots, Onions, Tomatoes, Spinach, Cucumbers, Potatoes, Corn, Brussel Sprouts
- **Proteins**: Chicken, Ground Beef, Hot Dogs, Fish, Salmon, Shrimp, Tilapia, Eggs
- **Dairy**: Ice Cream, Milk, Butter, Cheese
- **Pantry**: Pizza, Rice, Pasta, Cereal, Sugar, Flour, Baking Soda, Chocolate Chips, Cake Mix, Honey, Peanut Butter, Jam
- **Condiments**: Vinegar, Soy Sauce, Salt, Pepper, Spices
- **Beverages**: Soda, Juice, Coffee, Tea, Water
- **Household**: Napkins, Paper Towels, Toothpaste, Shampoo, Conditioner, Laundry Detergent, Dish Soap, Batteries, Light Bulbs

## Algorithm: Linear Search

### How It Works
```python
def linear_search(database, target):
    for index, item in enumerate(database):
        if item.lower() == target.lower():
            return index
    return -1
```

**Steps**:
1. Start at beginning of list (index 0)
2. Compare each item to target
3. If match found, return index
4. If end reached without match, return -1

### Time Complexity
- **Best Case**: O(1) - Item is first element
- **Worst Case**: O(n) - Item is last or not present
- **Average Case**: O(n/2) ≈ O(n)

### Space Complexity
- **O(1)** - Constant space (no additional data structures)

## Technical Details

**Language**: Python 3
**Algorithm**: Linear Search
**Concepts**:
- Sequential search
- List traversal
- Enumerate function
- String comparison (case-insensitive)

## Code Structure

### Functions

**linear_search(database, target)**
- Iterates through database
- Case-insensitive comparison
- Returns index or -1

**main()**
- Initializes database list
- Game loop for continuous searching
- Handles user input
- Displays results

## When to Use Linear Search

**Advantages**:
- Simple to implement
- Works on unsorted lists
- No preprocessing required
- Good for small datasets

**Disadvantages**:
- Slow for large datasets
- O(n) time complexity
- Better algorithms exist for sorted data

## Comparison with Other Search Algorithms

| Algorithm | Time (Sorted) | Time (Unsorted) | Space | Preprocessing |
|-----------|---------------|-----------------|-------|---------------|
| Linear Search | O(n) | O(n) | O(1) | None |
| Binary Search | O(log n) | N/A | O(1) | Must be sorted |
| Hash Table | O(1) avg | O(1) avg | O(n) | Build hash table |

## Learning Outcomes

- Understanding search algorithms
- Time/space complexity analysis
- Algorithm implementation
- String manipulation
- User interaction design
- When to use different algorithms

## Possible Enhancements

1. **Binary Search**: Sort list and use binary search (O(log n))
2. **Hash Table**: Use dictionary for O(1) lookup
3. **Fuzzy Matching**: Suggest similar items
4. **Category Search**: Search by category
5. **Price Information**: Add prices to items
6. **Inventory Count**: Track quantities
7. **Shopping Cart**: Add items to cart
8. **Search History**: Remember recent searches
9. **Autocomplete**: Suggest items as you type
10. **Performance Metrics**: Show search time
