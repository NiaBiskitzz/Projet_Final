#Joueur 1 = vrai et joueur 2 = faux. Quand un joeur gagne un jeux il recois 1 point selon le vrai ou faux.
def banque (pointage_joueur1, pointage_joueur2, resultat_mini_jeux):
    if resultat_mini_jeux == True:
        pointage_joueur1 += 1
    elif resultat_mini_jeux == False:
        pointage_joueur2 += 1
    return pointage_joueur1, pointage_joueur2