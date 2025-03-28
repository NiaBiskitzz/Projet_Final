#si le joueur 1 gagne = vrai et joueur 2 gagne = faux

#player1 = True
#player2 = False
joueur1 = input()
joueur2 = input()
pointage_joueur1 = 0
pointage_joueur2 = 0
if joueur1:
    resultat_mini_jeux = True
elif joueur2:
    resultat_mini_jeux = False
#Si le joueur 1 a un resultats plus grand que le joueur 2, le joueur 1 gagne
if pointage_joueur1 > pointage_joueur2:
    resultat_mini_jeux = True
    #Si le joueur 2 a un resultats plus grand que le joueur 1, le joueur 2 gagne
elif pointage_joueur1 < pointage_joueur2:
    resultat_mini_jeux = False