


def calculate_hand_total(hand):
    """Calculates the total value of a player's hand while considering the Ace's flexible value."""
    total = sum(card[2] for card in hand) # Sum the values of the cards in hand
    num_aces = sum(1 for card in hand if card[0] == "Ace")   # Count the number of Aces in hand

    # Adjust for Aces if total exceeds 21
    while total > 21 and num_aces > 0:
        # Convert an Ace from 11 to 1   
        total -= 10  # Convert an Ace from 11 to 1
        num_aces -= 1   # Decrease the count of Aces
    
    return total

"""
# To test the function, type in the following lines:
player1_hand = [{"rank": "A", "suit": "Hearts", "value": 11}, {"rank": "8", "suit": "Spades", "value": 8}]
player1_total = calculate_hand_total(player1_hand)
print(player1_total)
"""