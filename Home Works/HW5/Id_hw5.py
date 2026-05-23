from ast import Return
import random

def card_value(card):
    """Return the integer value [1, 9] of card"""
    return card % 9 + 1

def card_suit(card):
    """Return the suit ["Club", "Spade", "Heart", "Diamond"] of card"""
    suits = ["Club", "Spade", "Heart", "Diamond"]
    return suits[card // 9]

def display_card(card):
    """Prints card, both value and suit, in some reasonable report format"""
    val = card_value(card)
    suit = card_suit(card)
    print(f"{val}{suit[0]}")

def init_deck(deck):
    """Assign the elements of deck, such that each element's value is the same as its index."""
    for i in range(36):
        if i < len(deck):
            deck[i] = i
        else:
            deck.append(i)

def shuffle_deck(deck, n):
    """Generate two random numbers j and k in [0, 35] and swap exactly n times"""
    for _ in range(n):
        j = random.randint(0, 35)
        k = random.randint(0, 35)
        
        deck[j], deck[k] = deck[k], deck[j]

def display_deck(deck):
    """Prints the cards in deck"""
    for card in deck:
        display_card(card)

def card_tuple(card):
    """Return a tuple that contains the card value and the card suit"""
    return (card_value(card), card_suit(card))

def unique_suits(deck):
    """Return a set containing all suits found in the deck"""
    return {card_suit(card) for card in deck}

def main():
    
    deck = [0] * 36

    print("After init_deck")
    print("****")
    init_deck(deck)
    display_deck(deck)

    print("\nAfter shuffle_deck")
    print("**************************\n**************")
    
    shuffle_deck(deck, 150)  
    display_deck(deck)

    print("\nCard tuple example:")
    
    print(card_tuple(10))

    print("\nUnique suits:")
    print(unique_suits(deck))

if __name__ == "__main__":
    main()