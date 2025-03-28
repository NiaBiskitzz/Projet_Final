from Maître_du_temps.Amé import Input_Temps_Reel
from Core.Chargement import Debut_Jeu
from Core.Pointage import Banque
from Maître_du_temps.Gregoire import countdown

def Taper():
    """
    Le gagnant est la personne qui tape le plus grand nombre de fois sur sa touche.
    """
    print("Le but du jeu est d'appuyer le plus grand nombre de fois sur votre touche. La touche du joueur 1 est s et celle du joueur 2 est k.")

    total_seconds = countdown.countdown()

    while countdown.countdown() and total_seconds != 0:
        #Apporter les variables score1 et score2 de Input_Temps_Reel
        score1, score2 = Input_Temps_Reel.InputTempsReel()

        #Apporter les variables pointage_joueur1 et pointage_joueur2 de Banque
        pointage_joueur1, pointage_joueur2 = Banque.banque()

        #Il faut appuyer sur la touche espace pour débuter le jeu
        Debut_Jeu.DebutJeu()
        #Le nombre de fois que les joueurs appuient sur leur touche (s et k) est compté
        Input_Temps_Reel.InputTempsReel()
        #Les scores (variables du jeu) sont égaux aux pointages (variables qui déterminent le gagnant)
        pointage_joueur1 = score1
        pointage_joueur2 = score2
        #Retourner les scores aux codes de pointage pour déterminer le gagnant
    return pointage_joueur1, pointage_joueur2 