### This is TRASH CODE, please do not use it in production ###



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
    import random
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

    # List of the cards
    deck = [ace_of_hearts, king_of_hearts, queen_of_hearts, jack_of_hearts, ten_of_hearts, nine_of_hearts, eight_of_hearts, seven_of_hearts, six_of_hearts, five_of_hearts, four_of_hearts, three_of_hearts, two_of_hearts, ace_of_diamonds, king_of_diamonds, queen_of_diamonds, jack_of_diamonds, ten_of_diamonds, nine_of_diamonds, eight_of_diamonds, seven_of_diamonds, six_of_diamonds, five_of_diamonds, four_of_diamonds, three_of_diamonds, two_of_diamonds, ace_of_clubs, king_of_clubs, queen_of_clubs, jack_of_clubs, ten_of_clubs, nine_of_clubs, eight_of_clubs, seven_of_clubs, six_of_clubs, five_of_clubs, four_of_clubs, three_of_clubs, two_of_clubs, ace_of_spades, king_of_spades, queen_of_spades, jack_of_spades, ten_of_spades, nine_of_spades, eight_of_spades, seven_of_spades, six_of_spades, five_of_spades, four_of_spades, three_of_spades, two_of_spades]

    Player1_stand = False
    Player2_stand = False

    import random
    while Player1_stand and Player2_stand == False:
        input("appuyer sur entrer pour commencez")
        Player1_card1 = random.choice(deck)
        deck.remove(Player1_card1)
        Player1_card2 = random.choice(deck)
        deck.remove(Player1_card2)
        print(Player1_card1, Player1_card2)
        Player2_card1 = random.choice(deck)
        Player2_card2 = random.choice(deck)
        print(Player2_card1, Player2_card2)
        if Player1_card1['value'] + Player1_card2['value'] == 21:
            print("Player1 a gagné")
        elif Player2_card1['value'] + Player2_card2['value'] == 21:
            print("Player2 a gagné")
        Player1_continue = input("player1 hit ou stand")
        if Player1_continue == "hit":
            Player1_card3 = random.choice(deck)
            deck.remove(Player1_card3)
            print(Player1_card1, Player1_card2, Player1_card3)
            if Player1_card1['value'] + Player1_card2['value'] + Player1_card3['value'] > 21:
                print("Player1 a busté")
                break
            elif Player1_card1['value'] + Player1_card2['value'] + Player1_card3['value'] == 21:
                print("Player1 a gagné")
                break
        elif Player1_continue == "stand":
            Player1_stand = True
        player2_continue = input("player2 hit ou stand")
        if player2_continue == "hit":
            Player2_card3 = random.choice(deck)
            deck.remove(Player2_card3)
            print(Player2_card1, Player2_card2, Player2_card3)
            if Player2_card1['value'] + Player2_card2['value'] + Player2_card3['value'] > 21:
                print("Player2 a busté")
                break
            elif Player2_card1['value'] + Player2_card2['value'] + Player2_card3['value'] == 21:
                print("Player2 a gagné")
                break
        elif player2_continue == "stand":
            Player2_stand = True
    
    if Player1_card1['value'] + Player1_card2['value'] + Player1_card3['value'] > Player2_card1['value'] + Player2_card2['value'] + Player2_card3['value']<= 21:
        print("Player2 a buster, Player1 a gagné")
    elif Player1_card1['value'] + Player1_card2['value'] + Player1_card3['value'] < Player2_card1['value'] + Player2_card2['value'] + Player2_card3['value']<= 21:
        print("Player1 a buster, Player2 a gagné")


print(black_jack)
print(black_jack)
print(black_jack)