# Fonction aléatoire

liste_jeux=[1,2,3,4,5,6]
Jeu1_joué=False
Jeu2_joué=False
Jeu3_joué=False
Jeu4_joué=False
Jeu5_joué=False
Jeu6_joué=False

def aléatoire():
    """
    Choisir un jeu aléatoire 1 à 6.

    Paramètres
    ----------
    import random
    random_game=random

    """
    
    joué=False
    import random
    Random_game=random.choice(liste_jeux)
    if Random_game==1:
        Jeu1_joué=True
        print("Jeu 1")
        liste_jeux.remove(1)
        return 1
    elif Random_game==2:
        Jeu2_joué=True
        print("Jeu 2")
        liste_jeux.remove(2)
        return 2
    elif Random_game==3:
        Jeu3_joué=True
        print("Jeu 3")
        liste_jeux.remove(3)
        return 3
    elif Random_game==4:
        Jeu4_joué=True
        print("Jeu 4")
        liste_jeux.remove(4)
        return 4
    elif Random_game==5:
        Jeu5_joué=True
        print("Jeu 5")
        liste_jeux.remove(5)
        return 5
    elif Random_game==6:
        Jeu6_joué=True
        print("Jeu 6")
        liste_jeux.remove(6)
        return 6

print(aléatoire())
print(aléatoire())
print(aléatoire())
print(aléatoire())
print(aléatoire())
print(aléatoire())
print(aléatoire())
