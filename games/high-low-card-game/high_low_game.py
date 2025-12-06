import random

def create_deck():
    deck = list(range(2, 15)) * 4
    random.shuffle(deck)
    return deck

def card_name(card_value):
    if card_value == 11:
        return 'Jack'
    elif card_value == 12:
        return 'Queen'
    elif card_value == 13:
        return 'King'
    elif card_value == 14:
        return 'Ace'
    else:
        return str(card_value)

def main():
    print("Welcome to the High-Low Card Game!")
    deck = create_deck()
    score = 0
    current_card = deck.pop()

    while True:
        print(f"\nCurrent card is: {card_name(current_card)}")
        guess = input("Will the next card be higher or lower? (type 'high' or 'low'): ").lower()

        if guess not in ['high', 'low']:
            print("Invalid input. Please type 'high' or 'low'.")
            continue

        next_card = deck.pop()
        print(f"The next card is: {card_name(next_card)}")

        if (guess == 'high' and next_card > current_card) or (guess == 'low' and next_card < current_card):
            score += 1
            print("You are correct! Guess again:)")
            current_card = next_card
            if not deck:
                print("No more cards left in the deck!")
                break
        else:
            print("Sorry, wrong guess! Rerun the game to play again!")
            break

    print(f"Your final score is: {score}")

if __name__ == "__main__":
    main()
