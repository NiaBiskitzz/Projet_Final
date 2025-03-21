# Fonction aléatoire

liste_jeux=[1,2,3,4,5,6]

def aléatoire():
    """
    Choisir un jeu aléatoire 1 à 6.

    Paramètres
    ----------
    import random

    """

    joué=False
    import random
    Random_game=random.choice(liste_jeux)
    if Random_game==1:
        liste_jeux.remove(1)
        print("Jeu 1")
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

print(aléatoire())
print(aléatoire())
print(aléatoire())
print(aléatoire())
print(aléatoire())
print(aléatoire())