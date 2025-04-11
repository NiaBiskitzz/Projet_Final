from Maître_du_temps.Amé import Input_Temps_Reel #Compte le nombre de fois que les touches s et k sont appuyées
from Core.Chargement import Debut_Jeu #Appuyer sur la touche espace pour débuter le jeu
from Core.Pointage import Réponse_finale #Apporter les variables pour calculer les points des joueurs
from décompte import decompte #Décompte de 5 secondes

def Taper():
    """
    Le gagnant est la personne qui tape le plus grand nombre de fois sur sa touche.

    Cette fonction retourne les pointages des joueurs 1 et 2.
    """
    print("Le but du jeu est d'appuyer le plus grand nombre de fois sur votre touche. La touche du joueur 1 est s et celle du joueur 2 est k.")

    #Apporter les variables score1 et score2 de Input_Temps_Reel
    score1, score2 = Input_Temps_Reel.InputTempsReel()

    #Apporter les variables pointage_joueur1 et pointage_joueur2 de Banque
    pointage_joueur1, pointage_joueur2 = Réponse_finale.reponsefinale()

    #Il faut appuyer sur la touche espace pour débuter le jeu
    Debut_Jeu.DebutJeu()

    #Apporter la variable countdown de décompte
    countdown = décompte.decompte()

    #Appel de la fonction pour avoir un décompte de 5 secondes
    decompte()

    #Pendant que countdown n'est pas équivalent à 0
    while countdown != 0:
        #Le nombre de fois que les joueurs appuient sur leur touche (s et k) est compté
        Input_Temps_Reel.InputTempsReel()
        #Les scores (variables du jeu) sont égaux aux pointages (variables qui déterminent le gagnant)
        pointage_joueur1 = score1
        pointage_joueur2 = score2
        #Retourner les scores aux codes de pointage pour déterminer le gagnant
    return pointage_joueur1, pointage_joueur2 

#Appel de la fonction
Taper() 