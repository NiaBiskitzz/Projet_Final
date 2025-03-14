# Fonction aléatoire

liste_jeux=[1,2,3,4,5,6]
bool(Jeu1_joué)=False
bool(Jeu2_joué)=False
bool(Jeu3_joué)=False
bool(Jeu4_joué)=False
bool(Jeu5_joué)=False
bool(Jeu6_joué)=False
if bool(Jeu1_joué)==True:
    liste_jeux.remove(1)
if bool(Jeu2_joué)==True:
    liste_jeux.remove(2)
if bool(Jeu3_joué)==True:
    liste_jeux.remove(3)
if bool(Jeu4_joué)==True:
    liste_jeux.remove(4)
if bool(Jeu5_joué)==True:
    liste_jeux.remove(5)
if bool(Jeu6_joué)==True:
    liste_jeux.remove(6)

import Jeu1
import Jeu2
import Jeu3
import Jeu4
import Jeu5
import Jeu6

def aléatoire():
    """
    Choisir un jeu aléatoire 1 à 6.

    Paramètres
    ----------

    """
    
    joué=False
    import random
    Random_game=random.choice(liste_jeux)
    if Random_game==1:
        bool(Jeu1_joué)=True
        print("Jeu 1")
        return 1
    elif Random_game==2:
        bool(Jeu2_joué)=True
        print("Jeu 2")
        return 2
    elif Random_game==3:
        bool(Jeu3_joué)=True
        print("Jeu 3")
        return 3
    elif Random_game==4:
        bool(Jeu4_joué)=True
        print("Jeu 4")
        return 4
    elif Random_game==5:
        bool(Jeu5_joué)=True
        print("Jeu 5")
        return 5
    elif Random_game==6:
        bool(Jeu6_joué)=True
        print("Jeu 6")
        return 6