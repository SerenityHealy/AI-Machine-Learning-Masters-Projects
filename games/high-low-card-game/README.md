# High-Low Card Game

A command-line card guessing game where players predict whether the next card will be higher or lower than the current card.

## Overview

This interactive game simulates a deck of cards and challenges players to correctly guess whether each successive card will be higher or lower. The game continues until the player guesses incorrectly or runs out of cards.

## Features

- **52-Card Deck**: Full deck with values 2-14 (Ace high)
- **Random Shuffling**: Deck randomized each game
- **Score Tracking**: Counts consecutive correct guesses
- **Face Card Display**: Jack, Queen, King, Ace names
- **Input Validation**: Ensures valid guesses
- **Game End Conditions**: Wrong guess or deck exhaustion

## Usage

```bash
python high_low_game.py
```

## How to Play

1. Game displays current card
2. Guess if next card will be 'high' or 'low'
3. Game reveals the next card
4. If correct, score increases and game continues
5. If incorrect, game ends
6. Rerun program to play again

## Example Session

```
Welcome to the High-Low Card Game!

Current card is: 7
Will the next card be higher or lower? (type 'high' or 'low'): high
The next card is: Jack
You are correct! Guess again:)

Current card is: Jack
Will the next card be higher or lower? (type 'high' or 'low'): low
The next card is: 5
You are correct! Guess again:)

Current card is: 5
Will the next card be higher or lower? (type 'high' or 'low'): high
The next card is: 3
Sorry, wrong guess! Rerun the game to play again!
Your final score is: 2
```

## Game Mechanics

### Card Values
- **2-10**: Numeric values
- **11**: Jack
- **12**: Queen
- **13**: King
- **14**: Ace (highest)

### Winning a Round
- Guess "high" and next card > current card
- Guess "low" and next card < current card

### Losing
- Guess "high" and next card ≤ current card
- Guess "low" and next card ≥ current card

### Ties
Currently, ties (same value) count as incorrect. This can be modified.

## Technical Details

**Language**: Python 3
**Libraries**: `random` (for shuffling)
**Concepts**:
- List manipulation
- Random shuffling
- Game loop logic
- Conditional logic
- Input validation

## Code Structure

### Functions

**create_deck()**
- Creates list with values 2-14, repeated 4 times (suits)
- Shuffles the deck
- Returns shuffled deck

**card_name(card_value)**
- Converts numeric values to card names
- Maps 11→Jack, 12→Queen, 13→King, 14→Ace
- Returns string representation

**main()**
- Game loop and logic
- Input handling
- Score tracking
- Win/lose conditions

## Strategy Tips

- **Probability**: Low cards (2-7) more likely to go up
- **High cards** (10-Ace) more likely to go down
- **Middle cards** (7-9) are trickiest
- **Deck counting**: Remember what's been played

## Learning Outcomes

- Game loop implementation
- Random number generation
- List operations (pop, shuffle)
- User input validation
- Control flow (while loops, conditionals)
- Function design and modularity

## Possible Enhancements

1. **Tie Handling**: Let player guess again on ties
2. **Deck Counting**: Show remaining cards
3. **Difficulty Levels**: Different deck sizes
4. **Streak Bonuses**: Bonus points for long streaks
5. **Leaderboard**: Save high scores
6. **Multiplayer**: Take turns guessing
7. **Suit Display**: Show actual suits (♠ ♥ ♦ ♣)
8. **Statistics**: Track win/loss ratio
9. **Betting System**: Add virtual currency
10. **Visual Display**: ASCII card graphics
