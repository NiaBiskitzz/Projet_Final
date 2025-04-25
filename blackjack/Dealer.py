import random


def deal_card(deck):
    """Deals one card from the deck using random.choice and removes it."""
    card = random.choice(deck)  # Choose a random card
    deck.remove(card)           # Remove the card from the deck
    return card