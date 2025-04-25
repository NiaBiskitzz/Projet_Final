from blackjack.Dealer import deal_card


def player_hits(player_hand, deck):
    """Handles the player hitting and receiving a new card."""
    new_card = deal_card(deck) # Deal a new card from the deck
    player_hand.append(new_card)    # Add the new card to the player's hand
    return new_card # Return the new card for display purposes