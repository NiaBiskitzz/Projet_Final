import random
import os

import poker
import HandTotal
import Dealer
import Player_turn
from Core.Pointage import Réponse_finale #Importer pour les pointages



def black_jack():
    #Importer les pointages
    pointage_joueur1, pointage_joueur2 = Réponse_finale.reponsefinale()

    # Create a deck of cards
    deck = poker.create_blackjack_deck()

    #start of the game
    print("Bienvenue dans le jeu de Black Jack!")  # Welcome message
    input("Appuyer sur entrer pour recevoir les cartes")  # Wait for the player to press enter

    # Player 1's turn
    Player1_hand = [Dealer.deal_card(deck), Dealer.deal_card(deck)]  # Deal 2 cards to player 1
    print("les cartes de player 1 sont: ", Player1_hand)  # Display player 1's hand
    Player1_total = HandTotal.calculate_hand_total(Player1_hand)  # Calculate the total value of player 1's hand
    print("la valeur des cartes de player 1 est: ", Player1_total)  # Display player 1's total value

    input("Donnez l'ordi à l'autre joueur")  # Wait for the player to pass the turn to
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen

    # Player 2's turn
    Player2_hand = [Dealer.deal_card(deck), Dealer.deal_card(deck)]  # Deal 2 cards to player 2
    print("les cartes de player 2 sont: ", Player2_hand)  # Display player 2's hand
    Player2_total = HandTotal.calculate_hand_total(Player2_hand)  # Calculate the total value of player 2's hand
    print("la valeur des cartes de player 2 est: ", Player2_total)  # Display player 2's total value

    input("Donnez l'ordi à l'autre joueur")  # Wait for the player to pass the turn to
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen


    # Hit or stand
    #Player 1's turn
    Player1_standing = Player_turn.player_turn(deck, Player1_hand)  # Player 1's turn to hit or stand
    Player1_total = HandTotal.calculate_hand_total(Player1_hand)  # Calculate the total value of player 1's hand
    print("la valeur des cartes de player 1 est: ", Player1_total)  # Display player 1's total value
    if Player1_total > 21:
        print("Player 1 a busté! Player 2 gagne!")  # Player 1 busted, Player 2 wins
        return
    input("Donnez l'ordi à l'autre joueur")  # Wait for the player to pass the turn to
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen

    # Player 2's turn
    Player2_standing = Player_turn.player_turn(deck, Player2_hand)  # Player 2's turn to hit or stand
    Player2_total = HandTotal.calculate_hand_total(Player2_hand)  # Calculate the total value of player 2's hand
    print("la valeur des cartes de player 2 est: ", Player2_total)  # Display player 2's total value
    if Player2_total > 21:
        print("Player 2 a busté! Player 1 gagne!")  # Player 2 busted, Player 1 wins
        return

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen

    # Determine the winner
    print("Player 1 total:", Player1_total)  # Display player 1's total value
    print("Player 2 total:", Player2_total)  # Display player 2's total value   
    if Player1_standing and Player2_standing:
        if Player1_total > Player2_total:
            print("Player 1 gagne!")  # Player 1 wins
            #Pointages des joueurs
            pointage_joueur1 = 1
            pointage_joueur2 = 0 
        elif Player2_total > Player1_total:
            print("Player 2 gagne!")  # Player 2 wins
            #Pointages des joueurs
            pointage_joueur1 = 0
            pointage_joueur2 = 1
        else:
            print("Égalité!!!")  # Tie game
            #Pointages des joueurs
            pointage_joueur1 = 0
            pointage_joueur2 = 0
    return pointage_joueur1, pointage_joueur2



black_jack()