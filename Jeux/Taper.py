import sys
sys.path.insert(1,'/../Maître_du_temps/Amé')
sys.path.append('../../Core/Chargement')
from Input_Temps_Reel import InputTempsReel 
from Debut_jeu import DebutJeu

def Taper():
    """
    Le gagnant est la personne qui tape le plus grand nombre de fois suer sa touche.
    """
    print("Le but du jeu est d'appuyer le plus grand nombre de fois sur votre touche. La touche du joueur 1 est s et celle du joueur 2 est k.")

    DebutJeu()
    InputTempsReel()
    pointage_joueur1 = score1
    pointage_joueur2 = score2
    return pointage_joueur1, pointage_joueur2 