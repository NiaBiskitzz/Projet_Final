import itertools

def create_blackjack_deck():
    """Creates a standard deck of playing cards for blackjack."""
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]   # List of suits
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]  # List of ranks
    values = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10} # Dictionary for card values

    
    deck = [(rank, suit, values[rank]) for rank, suit in itertools.product(ranks, suits)] # Create a list of dictionaries for each card
    
    return deck

"""
# To test the function, type in the following lines:
deck = create_blackjack_deck()
for card in deck:
    print(card)
"""