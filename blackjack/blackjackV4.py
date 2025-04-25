import random
import os

import poker
import HandTotal
import Dealer
import player_hit



#def black_jack():

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

print("les cartes de player 1 sont: ", Player1_hand)  # Display player 1's hand
Player1_total = HandTotal.calculate_hand_total(Player1_hand)  # Calculate the total value of player 1's hand
print("la valeur des cartes de player 1 est: ", Player1_total)  # Display player 1's total value

if Player1_total == 21:  # Check if player 1 has a blackjack
    print("Player 1 a un blackjack!")  # Display a message if player 1 has a blackjack
        ###return joueur1_gagne = True  # Set the variable to indicate that player 1 has won

elif Player1_total > 21:  # Check if player 1 has busted
    print("Player 1 a busté!")
    ###return joueur1_gagne = False  # Set the variable to indicate that player 1 has lost

input("Donnez l'ordi à l'autre joueur")  # Wait for the player to pass the turn to
os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen

# Player 2's turn
Player2_hand = []
for _ in range(2):  # Deal 2 cards to player 2
    card = random.choice(deck)  # Randomly select a card from the deck
    Player2_hand.append(card)  # Add the card to player 1's hand
    deck.remove(card)  # Remove the card from the deck

print("les cartes de player 2 sont: ", Player2_hand)  # Display player 2's hand
Player2_hand = list(Player2_hand)  # Convert player 2's hand to a list
Player2_total = HandTotal.calculate_hand_total(Player2_hand)  # Calculate the total value of player 2's hand
print("la valeur des cartes de player 2 est: ", Player2_total)  # Display player 2's total value

if Player2_total == 21:  # Check if player 2 has a blackjack
    print("Player 2 a un blackjack!")  # Display a message if player 2 has a blackjack
    ###return joueur2_gagne = True  # Set the variable to indicate that player 1 has won

elif Player2_total > 21:  # Check if player 2 has busted
    print("Player 2 a busté!")  # Display a message if player 2 has busted
    ###return joueur2_gagne = False  # Set the variable to indicate that player 1 has won

input("Donnez l'ordi à l'autre joueur")  # Wait for the player to pass the turn to
os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen

answer_player1 = ""
answer_player2 = ""
while (len(Player1_hand) < 11 and Player1_total < 21):  # Loop until player 1 or player 2 has 11 cards or reaches/ exceed a total of 21 or both players stand
    # Player 1's turn
    if len(Player1_hand) < 11 and Player1_total < 21:
        print("Player 1, hit ou stand?")  # Ask if player 1 wants to hit or stand
        answer_player1 = input()  # Get the player's response
        if answer_player1 == "hit":  # If the player hits
            new_card = player_hit.player_hit(Player1_hand, deck)  # Deal a new card to player 1
            Player1_total = HandTotal.calculate_hand_total(Player1_hand)  # Calculate the new total value of player 1's hand
            print("la nouvelle carte est: ", new_card)  # Display the new card
            print("Vos cartes sont: ", Player1_hand)    # Display player 1's hand
            print("la valeur de vos cartes est: ", Player1_total)  # Display the total value of player 1's hand
            if Player1_total == 21:  # Check if player 1 has a blackjack
                print("Player 1 a un blackjack!")
            elif Player1_total > 21:  # Check if player 1 has busted
                print("Player 1 a busté!")
                break
        else:
            if answer_player1 == "stand":
                continue  # Do nothing if the player does not want another card
    input("Donnez l'ordi à l'autre joueur")  # Wait for the player to pass the turn to
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
    
    # Player 2's turn
    if len(Player2_hand) < 11 and Player2_total < 21:
        print("Player 2, hit ou stand?")  # Ask if player 2 wants to hit or stand 
        answer_player2 = input()  # Get the player's response
        if answer_player2 == "hit":  # If the player hits
            new_card = player_hit.player_hit(Player2_hand, deck)  # Deal a new card to player 2
            Player2_total = HandTotal.calculate_hand_total(Player2_hand)  # Calculate the new total value of player 2's hand
            print("la nouvelle carte est: ", new_card)  # Display the new card
            print("Vos cartes sont: ", Player2_hand)    # Display player 2's hand
            print("la valeur de vos cartes est: ", Player2_total)  # Display the total value of player 2's hand
            if Player2_total == 21:  # Check if player 2 has a blackjack
                print("Player 2 a un blackjack!")
            elif Player2_total > 21:  # Check if player 2 has busted
                print("Player 2 a busté!")
                break
        else:
            if answer_player2 == "stand":
                continue  # Do nothing if the player does not want another card
    input("Donnez l'ordi à l'autre joueur")  # Wait for the player to pass the turn to
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
    if answer_player1 == "stand" and answer_player2 == "stand":
        pass  # Exit the loop if both players do not want another card
    print("Player 1, your total is: ", Player1_total)  # Display player 1's total value
    print("Player 2, your total is: ", Player2_total)  # Display player 2's total value
    if Player1_total > Player2_total and Player1_total <= 21:
        print("Player 1 wins!")
        break
        
    elif Player2_total > Player1_total and Player2_total <= 21:
        print("Player 2 wins!")
        break