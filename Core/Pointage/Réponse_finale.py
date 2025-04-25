#si le joueur 1 gagne = vrai et joueur 2 gagne = faux
#player1 = True
#player2 = False
from test_main import point_joueur1, point_joueur2 

def reponsefinale(pointage_joueur1, pointage_joueur2):
    #Si le joueur 1 a un resultats plus grand que le joueur 2, le joueur 1 gagne
    if pointage_joueur1 > pointage_joueur2:
        resultat_mini_jeux = True
    #Si le joueur 2 a un resulat plsu grand que le joueur 1, le joueur 2 gagne
    elif pointage_joueur1 < pointage_joueur2:
        resultat_mini_jeux = False

    #Si le joueur 1 a gagné, il recois un point    
    if resultat_mini_jeux == True:
        point_joueur1 = point_joueur1 + 1
    #Si le joueur 2 a gagné, il recois un point
    elif resultat_mini_jeux == False:
        point_joueur2 = point_joueur2 + 1
    return point_joueur1, point_joueur2