#si le joueur 1 gagne = vrai et joueur 2 gagne = faux
#player1 = True
#player2 = False
def reponsefinale(pointage_joueur1, pointage_joueur2, resultat_mini_jeux):
    #Si le joueur 1 a un resultats plus grand que le joueur 2, le joueur 1 gagne
    if pointage_joueur1 > pointage_joueur2:
        resultat_mini_jeux = True
    elif pointage_joueur1 < pointage_joueur2:
        resultat_mini_jeux = False
    if resultat_mini_jeux == True:
        point_joueur1 += 1
    if resultat_mini_jeux == False:
        point_joueur2 += 1
    #Si le joueur 2 a un resultats plus grand que le joueur 1, le joueur 2 gagne
    return point_joueur1, point_joueur2