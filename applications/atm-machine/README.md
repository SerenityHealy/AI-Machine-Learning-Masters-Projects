# ATM Machine Simulator

A command-line ATM machine simulator with PIN authentication, balance management, and transaction handling.

## Overview

This project simulates basic ATM functionality including card insertion, PIN verification with attempt limits, withdrawals, deposits, and balance tracking.

## Features

- **Card Insertion Simulation**: Prompts for card insertion
- **PIN Authentication**: 3-attempt limit with card retention on failure
- **Withdrawal**: Deduct funds with insufficient balance checking
- **Deposit**: Add funds to account
- **Balance Display**: Shows current balance before each transaction
- **Auto-Close on Zero Balance**: Closes account when balance reaches zero
- **Input Validation**: Handles invalid amounts and menu choices

## Usage

```bash
python atm_machine.py
```

### Example Session

```
Hello, Welcome to the ATM! Please Insert Your Card to Start.
Insert Card? (y/n): y
Enter your PIN: 1234
PIN accepted.

Current balance: $100.00
What would you like to do?
1) Withdraw
2) Deposit
3) Exit
Choose an option (1/2/3): 1
Enter withdrawal amount: $50
Withdrew $50.00. New balance: $50.00
```

## Configuration

Default settings (can be modified in code):
- **Initial Balance**: $100.00
- **Correct PIN**: 1234
- **Max PIN Attempts**: 3

## Features Breakdown

### PIN Verification
- Allows 3 attempts to enter correct PIN
- Retains card and exits after max attempts
- Case-sensitive comparison

### Transaction Types

**Withdrawal**:
- Validates amount > 0
- Checks for sufficient funds
- Updates balance on success

**Deposit**:
- Validates amount > 0
- Adds to balance immediately

### Error Handling
- Invalid PIN handling
- Insufficient funds notification
- Invalid amount (non-numeric, zero, negative)
- Invalid menu selection

## Technical Details

**Language**: Python 3
**Concepts Demonstrated**:
- While loops for menu systems
- Conditional logic
- Exception handling (ValueError)
- Input validation
- State management (balance, attempts)

## Learning Outcomes

- Building interactive CLI applications
- Implementing authentication systems
- Managing financial transactions
- Input validation and error handling
- State management in programs
- User experience design for terminal apps

## Possible Enhancements

1. **Multiple Accounts**: Support checking/savings
2. **Transaction History**: Log all transactions
3. **Persistent Storage**: Save balance to file
4. **Receipt Printing**: Generate transaction receipts
5. **Transfer Money**: Between accounts
6. **Bill Payment**: Add bill pay functionality
