#si le joueur 1 gagne = vrai et joueur 2 gagne = faux
joueur1 = input()
joueur2 = input()
pointage_joueur1 = 0
pointage_joueur2 = 0
#player1 = True
#player2 = False
def banque(pointage_joueur1, pointage_joueur2, resultat_mini_jeux):
    #Si le joueur 1 a un resultats plus grand que le joueur 2, le joueur 1 gagne
    if pointage_joueur1 > pointage_joueur2:
        resultat_mini_jeux = True
    if resultat_mini_jeux == True:
        pointage_joueur1 += 1
    #Si le joueur 2 a un resultats plus grand que le joueur 1, le joueur 2 gagne
    elif pointage_joueur1 < pointage_joueur2:
        resultat_mini_jeux = False
    elif resultat_mini_jeux == False:
        pointage_joueur2 += 1
    return pointage_joueur1, pointage_joueur2