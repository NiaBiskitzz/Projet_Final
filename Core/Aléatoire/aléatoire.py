# Fonction aléatoire

liste_jeux=[1,2,3,4,5,6]

def aléatoire():
    """
    Choisir un jeu aléatoire 1 à 6.

    Paramètres
    ----------
    import random
    random_game=random.choice(liste_jeux)à
    if random_game==1:
        liste_jeux.remove(1)
        print("Jeu 1")
        return 1
    elif random_game==2:
        liste_jeux.remove(2)
        print("Jeu 2")
        return 2
    elif random_game==3:
        liste_jeux.remove(3)
        print("Jeu 3")
        return 3
    elif random_game==4:
        liste_jeux.remove(4)
        print("Jeu 4")
        return 4
    elif random_game==5:
        liste_jeux.remove(5)
        print("Jeu 5")
        return 5
    elif random_game==6:
        liste_jeux.remove(6)
        print("Jeu 6")
        return 6
    """

    import random   # Import random library.
    Random_game=random.choice(liste_jeux)   # Choose a random game from the list.
    # conditions and returns while making sure the option is removed from the list.
    if Random_game==1:
        liste_jeux.remove(1)
        print("Jeu 1")  # Temporary print for testing, change to name of the game when testing the completed programme, also optionnal.
        return 1
    elif Random_game==2:
        liste_jeux.remove(2)
        print("Jeu 2")
        return 2
    elif Random_game==3:
        liste_jeux.remove(3)
        print("Jeu 3")
        return 3
    elif Random_game==4:
        liste_jeux.remove(4)
        print("Jeu 4")
        return 4
    elif Random_game==5:
        liste_jeux.remove(5)
        print("Jeu 5")
        return 5
    elif Random_game==6:
        liste_jeux.remove(6)
        print("Jeu 6")
        return 6

# Tests (optionnal), Remove when done.
print(aléatoire())
print(aléatoire())
print(aléatoire())
print(aléatoire())
print(aléatoire())
print(aléatoire())