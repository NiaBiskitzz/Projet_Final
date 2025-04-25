import poker
import HandTotal
import random
import Dealer

### def create_blackjack_deck():

# Create a deck of cards
deck = poker.create_blackjack_deck()



#start of the game
print("Bienvenue dans le jeu de Black Jack!")  # Welcome message
input("Appuyer sur entrer pour recevoir les cartes")  # Wait for the player to press enter

# Player 1's turn
Player1_hand = []
for _ in range(2):  # Deal 2 cards to player 1
    card = random.choice(deck)  # Randomly select a card from the deck
    Player1_hand.append(card)  # Add the card to player 1's hand
    deck.remove(card)  # Remove the card from the deck
print("les carts de player 1 sont: ", Player1_hand)  # Display player 1's hand
Player1_hand = list(Player1_hand)  # Convert player 1's hand to a list
Player1_total = HandTotal.calculate_hand_total(Player1_hand)  # Calculate the total value of player 1's hand
print("la valeur des cartes de player 1 est: ", Player1_total)  # Display player 1's total value

# Player 2's turn
Player2_hand = []
for _ in range(2):  # Deal 2 cards to player 2
    card = random.choice(deck)  # Randomly select a card from the deck
    Player2_hand.append(card)  # Add the card to player 1's hand
    deck.remove(card)  # Remove the card from the deck
print("les carts de player 2 sont: ", Player2_hand)  # Display player 2's hand
Player2_hand = list(Player2_hand)  # Convert player 2's hand to a list
Player2_total = HandTotal.calculate_hand_total(Player2_hand)  # Calculate the total value of player 2's hand
print("la valeur des cartes de player 2 est: ", Player2_total)  # Display player 2's total value

