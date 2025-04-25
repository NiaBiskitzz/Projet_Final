"""
Le jeu black jack utilise 52 cartes de poker(excluant les jokers). 
Chaque carte a une valeur entre 1 et 11. 
Le donneur distribue deux cartes visible au joueur. 
Le joueur peut demander des cartes supplémentaires (« hit ») 
jusqu’à ce que le total de ses cartes soit supérieur à 21 (auquel cas il perd) ou jusqu’à 
ce qu’il décide de s’arrêter (« stand »). 

la valeur de Ace est par default 11, si le valeur total est supérieur à 21,
il sera 1.
"""



#Body of the game/fonction
def black_jack():
    """
    definir le gagnant du jeu de black jack

    Paramètres
    ----------
    """



    # Dictionnary for the card values
    ace_of_hearts = {'suit': 'Hearts', 'value': 11}
    king_of_hearts = {'suit': 'Hearts', 'value': 10}
    queen_of_hearts = {'suit': 'Hearts', 'value': 10}
    jack_of_hearts = {'suit': 'Hearts', 'value': 10}
    ten_of_hearts = {'suit': 'Hearts', 'value': 10}
    nine_of_hearts = {'suit': 'Hearts', 'value': 9}
    eight_of_hearts = {'suit': 'Hearts', 'value': 8}
    seven_of_hearts = {'suit': 'Hearts', 'value': 7}
    six_of_hearts = {'suit': 'Hearts', 'value': 6}
    five_of_hearts = {'suit': 'Hearts', 'value': 5}
    four_of_hearts = {'suit': 'Hearts', 'value': 4}
    three_of_hearts = {'suit': 'Hearts', 'value': 3}
    two_of_hearts = {'suit': 'Hearts', 'value': 2}

    ace_of_diamonds = {'suit': 'Diamonds', 'value': 11}
    king_of_diamonds = {'suit': 'Diamonds', 'value': 10}
    queen_of_diamonds = {'suit': 'Diamonds', 'value': 10}
    jack_of_diamonds = {'suit': 'Diamonds', 'value': 10}
    ten_of_diamonds = {'suit': 'Diamonds', 'value': 10}
    nine_of_diamonds = {'suit': 'Diamonds', 'value': 9}
    eight_of_diamonds = {'suit': 'Diamonds', 'value': 8}
    seven_of_diamonds = {'suit': 'Diamonds', 'value': 7}
    six_of_diamonds = {'suit': 'Diamonds', 'value': 6}
    five_of_diamonds = {'suit': 'Diamonds', 'value': 5}
    four_of_diamonds = {'suit': 'Diamonds', 'value': 4}
    three_of_diamonds = {'suit': 'Diamonds', 'value': 3}
    two_of_diamonds = {'suit': 'Diamonds', 'value': 2}

    ace_of_clubs = {'suit': 'Clubs', 'value': 11}
    king_of_clubs = {'suit': 'Clubs', 'value': 10}
    queen_of_clubs = {'suit': 'Clubs', 'value': 10}
    jack_of_clubs = {'suit': 'Clubs', 'value': 10}
    ten_of_clubs = {'suit': 'Clubs', 'value': 10}
    nine_of_clubs = {'suit': 'Clubs', 'value': 9}
    eight_of_clubs = {'suit': 'Clubs', 'value': 8}
    seven_of_clubs = {'suit': 'Clubs', 'value': 7}
    six_of_clubs = {'suit': 'Clubs', 'value': 6}
    five_of_clubs = {'suit': 'Clubs', 'value': 5}
    four_of_clubs = {'suit': 'Clubs', 'value': 4}
    three_of_clubs = {'suit': 'Clubs', 'value': 3}
    two_of_clubs = {'suit': 'Clubs', 'value': 2}

    ace_of_spades = {'suit': 'Spades', 'value': 11}
    king_of_spades = {'suit': 'Spades', 'value': 10}
    queen_of_spades = {'suit': 'Spades', 'value': 10}
    jack_of_spades = {'suit': 'Spades', 'value': 10}
    ten_of_spades = {'suit': 'Spades', 'value': 10}
    nine_of_spades = {'suit': 'Spades', 'value': 9}
    eight_of_spades = {'suit': 'Spades', 'value': 8}
    seven_of_spades = {'suit': 'Spades', 'value': 7}
    six_of_spades = {'suit': 'Spades', 'value': 6}
    five_of_spades = {'suit': 'Spades', 'value': 5}
    four_of_spades = {'suit': 'Spades', 'value': 4}
    three_of_spades = {'suit': 'Spades', 'value': 3}
    two_of_spades = {'suit': 'Spades', 'value': 2}



    # Create a deck of cards
    deck = [ace_of_hearts, king_of_hearts, queen_of_hearts, jack_of_hearts, ten_of_hearts, nine_of_hearts, eight_of_hearts, seven_of_hearts, six_of_hearts, five_of_hearts, four_of_hearts, three_of_hearts, two_of_hearts, ace_of_diamonds, king_of_diamonds, queen_of_diamonds, jack_of_diamonds, ten_of_diamonds, nine_of_diamonds, eight_of_diamonds, seven_of_diamonds, six_of_diamonds, five_of_diamonds, four_of_diamonds, three_of_diamonds, two_of_diamonds, ace_of_clubs, king_of_clubs, queen_of_clubs, jack_of_clubs, ten_of_clubs, nine_of_clubs, eight_of_clubs, seven_of_clubs, six_of_clubs, five_of_clubs, four_of_clubs, three_of_clubs, two_of_clubs, ace_of_spades, king_of_spades, queen_of_spades, jack_of_spades, ten_of_spades, nine_of_spades, eight_of_spades, seven_of_spades, six_of_spades, five_of_spades, four_of_spades, three_of_spades, two_of_spades]



    #start of the game
    print("Bienvenue dans le jeu de Black Jack!")  # Welcome message
    input("Appuyer sur entrer pour recevoir les cartes")  # Wait for the player to press enter
    import random  # Import random library.


    #Player 1's turn
    Player1_hand = []  # Create a list for player 1's hand
    player1_card1 = random.choice(deck)  # Choose a random card from the deck
    deck.remove(player1_card1)  # Remove the card from the deck
    Player1_hand.append(player1_card1)  # Add the first card to player 1's hand
    player1_card2 = random.choice(deck)  # Choose a random card from the deck
    deck.remove(player1_card2)  # Remove the card from the deck
    Player1_hand.append(player1_card2)  # Add the second card to player 1's hand
    print(player1_card1, player1_card2)  # Print the cards
    player1_total = player1_card1['value'] + player1_card2['value']  # Calculate the total value of the cards
    print("Total:", player1_total)  # Print the total value of the cards

    # Player 2's turn
    Player2_hand = []  # Create a list for player 2's hand
    player2_card1 = random.choice(deck)  # Choose a random card from the deck
    deck.remove(player2_card1)  # Remove the card from the deck
    Player2_hand.append(player2_card1)  # Add the first card to player 2's hand
    player2_card2 = random.choice(deck)  # Choose a random card from the deck
    deck.remove(player2_card2)  # Remove the card from the deck
    Player2_hand.append(player2_card2)  # Add the second card to player 2's hand
    print(player2_card1, player2_card2)  # Print the cards
    player2_total = player2_card1['value'] + player2_card2['value']  # Calculate the total value of the cards
    print("Total:", player2_total)  # Print the total value of the cards



    #conditions for the game to continue
    if player1_total == 21:  # Check if player 1's total is 21
        print("Player 1 Black Jack!")  # Print a message if the player has a Black Jack
    elif player2_total == 21:  # Check if player 2's total is 21
        print("Player 2 Black Jack!")  # Print a message if the player has a Black Jack
    elif player1_total > 21:  # Check if player 1's total is greater than 21
        if ace_of_hearts or ace_of_diamonds or ace_of_clubs or ace_of_spades in Player1_hand:  # Check if player 1 has an Ace in their hand
            player1_total -= 10  # Subtract 10 from the total value of the cards
            print("Player 1, you have an Ace, your total is now:", player1_total)  # Print the new total value of the cards
        else:  # If player 1 does not have an Ace in their hand
            print("Player 1 busts!")  # Print a message if player 1 busts
    elif player2_total > 21:  # Check if player 2's total is greater than 21
        if ace_of_hearts or ace_of_diamonds or ace_of_clubs or ace_of_spades in Player2_hand:
            player2_total -= 10  # Subtract 10 from the total value of the cards
            print("Player 2, you have an Ace, your total is now:", player2_total)  # Print the new total value of the cards
        else:  # If player 2 does not have an Ace in their hand
            print("Player 2 busts!")  # Print a message if player 2 busts
    elif player1_total < 21 and player2_total < 21:  # Check if both players' totals are less than 21
        print("Player 1 and Player 2, hit ou stand?")
        player1_continue = input("Player 1? ")
        player2_continue = input("Player 2? ")  # Ask both players if they want to hit or stand
    while player1_continue == "hit" or player2_continue == "hit":  # While the player wants to hit
        if player1_continue == "hit":  # Check if the player wants to hit
            player1_card3 = random.choice(deck) # Choose a random card from the deck
            deck.remove(player1_card3)  # Choose a random card from the deck
            Player1_hand.append(player1_card3)  # Add the card to player 1's hand

"""Check if theres a way to add more cards to the player hand without having to write the same code over and over again"""
"""make a list with player_hand for cards and use apend"""