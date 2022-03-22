# https://www.codewars.com/kata/5810ad962b321bac8f000178
# Level 6 kyu

# Directions:
# A normal deck of 52 playing cards contains suits 'H', 'C', 'D', 'S' - Hearts, Clubs, Diamonds, Spades respectively - and cards with values from Ace (1) to King (13): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
# Your Task
# Complete the function that returns a shuffled deck of 52 playing cards without repeats.
# Each card should have format "{suit} {value}", e.g. the Queen of Hearts is "H 12" and the Ace of Spades is "S 1". 
# The order of the cards must be different each time the function is called.


# Function
def shuffled_deck():
    # Import random to use the shuffle() function.
    import random
    
    # Create lists containing the suit and card number.
    suits: list = ['H', 'C', 'D', 'S']
    cards: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    # Create a deck of cards that is a list with each card containing the suit a space then the card number ['H 1', 'H 2', ...].
    deck: dict = [f'{suit} {str(card)}' for suit in suits for card in cards]
    
    # Shuffle the deck using the random module.
    random.shuffle(deck)
    
    return deck


# Test Cases
import codewars_test as test
from solution import *

@test.describe("Sample test")
def tests():
    @test.describe("Some examples")
    def tests():
        deck1, deck2 = shuffled_deck(), shuffled_deck()
        test.assert_equals(len(set(deck1)), 52, "deck #1 should consist of 52 cards")
        test.assert_equals(len(set(deck2)), 52, "deck #2 should consist of 52 cards")
        test.assert_equals(sorted(deck1), sorted(deck2), "decks should contain the same cards")
        test.assert_not_equals(deck1, deck2, "decks should be shuffled")