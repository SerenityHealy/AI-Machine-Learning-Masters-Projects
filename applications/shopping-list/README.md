# Shopping List Application

A comprehensive grocery shopping application with list management, price comparison, and multi-screen navigation.

## Overview

This application provides a complete grocery shopping experience with user authentication, list creation/editing, saved lists management, and price comparison across multiple stores.

## Features

- **Welcome/Login Screen**: Login, password recovery, or guest access
- **List Management**: Create, view, and edit grocery lists
- **Saved Lists**: Store multiple lists with custom names
- **Price Comparison**: Compare total costs across 5 major stores
- **Category Organization**: Organize items by type (Fruits, Meat, Dairy, etc.)
- **Multi-Screen Navigation**: Intuitive menu system

## Usage

```bash
python shopping_list_app.py
```

### Navigation Flow

```
Welcome Screen
    ├─→ Log In → Options Screen
    ├─→ Forgot Password (email reset)
    └─→ Guest Access → Options Screen

Options Screen
    ├─→ Create New List
    ├─→ View Saved Lists
    ├─→ Edit Previous Lists
    ├─→ Price Comparison
    └─→ Exit
```

## Features Breakdown

### 1. Welcome/Login Screen
**Options**:
- Log In (proceeds to options)
- Forgot Password (shows email instructions)
- Guest Access (proceeds to options)

### 2. Create New Grocery List
- Add items one by one
- Type 'done' when finished
- Displays numbered list
- Returns to options screen

### 3. Saved Lists
**Pre-loaded Lists**:
- "The Cookout BBQ"
- "Birthday Party 8/3/25"
- "12/20/24 Grocery List"
- "11/10/24 Grocery List"
- "Halloween Party"

### 4. Price Comparison
Compares prices across stores:
- **Aldi**: $204.48 (lowest)
- **Costco**: $223.99
- **Walmart**: $244.29
- **Target**: $247.88
- **Whole Foods**: $250.73 (highest)

### 5. Edit Mode
- Select saved list to modify
- View details
- Return to options

## Example Session

```
--- Welcome/Login Screen ---
1. Log In
2. Forgot Password
3. Create / Guest Access
Select an option (1-3): 3
Accessing as Guest... Redirecting to Options Screen...

--- Options Screen ---
1. Create New List
2. View Saved Lists
3. Edit Previous Lists
4. Go to Price Comparison Screen
5. Exit
Select an option (1-5): 1

--- New Grocery List ---
Organize your list by categories (Fruits, Meat, Dairy, etc.)
Type 'done' when finished.
Add an item to your list: Apples
Add an item to your list: Milk
Add an item to your list: Chicken
Add an item to your list: done

Your Grocery List:
1. Apples
2. Milk
3. Chicken
```

## Technical Details

**Language**: Python 3
**Architecture**: Function-based with recursive navigation
**Concepts**:
- Function recursion for screen navigation
- Menu-driven interface
- List management
- Data structures (lists, dictionaries)
- Input validation

## Code Structure

### Functions
- `welcome_screen()`: Entry point with authentication
- `options_screen()`: Main menu hub
- `new_grocery_list()`: List creation interface
- `saved_lists_screen(edit_mode=False)`: View/edit saved lists
- `price_comparison_screen()`: Store price display

## Learning Outcomes

- Multi-screen application design
- Navigation state management
- User interface patterns
- List manipulation
- Menu-driven programming
- User experience flow

## Possible Enhancements

1. **Persistent Storage**: Save lists to JSON/database
2. **Real Price API**: Connect to actual store APIs
3. **Item Categories**: Auto-categorize items
4. **Coupons**: Apply discounts and coupons
5. **Shopping History**: Track past purchases
6. **Quantity & Units**: Add quantities to items
7. **Budget Tracking**: Set and monitor budgets
8. **Nutrition Info**: Add nutritional data
9. **Recipe Integration**: Generate lists from recipes
10. **Mobile App**: Convert to mobile interface
