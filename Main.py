#écrit un max de commentaire
import fonction_aléatoire #donne un chiffre de façcon aléatoire entre 1 et 6.De plus lorsqu'un chiffre est selectionné celui si ne peut être reselectionée à moin de redémarer la fonction
import Banque #fonction qui enregistre le nombre de point
import réponce_finale 
import début_Jeu #cette fonction permet que lorsque l'espace est actonner lejeu peux commencer
import point #Afichage des point total
import battleship #fonction du jeu 1
import trivia #fonction du jeu 2
import tape_taupe  #fonction du jeu 3
import black_jack #fonction jeu4
import duel #fontiont jeu 5
import roulette #fonction jeu 6

#démarage du programe des jeux
début_Jeu()
#Séléction du jeu de façon aléatoire
choix_de_jeu = fonction_aléatoire()
choix_de_jeu = int(choix_de_jeu)
if choix_de_jeu == 1:
    
    battleship()
    réponce_finale()
    Banque()
    point()
elif choix_de_jeu == 2:
    trivia()
    réponce_finale()
    Banque()
    point()
elif choix_de_jeu == 3:
    tape_taupe()
    réponce_finale()
    Banque()
    point()
elif choix_de_jeu == 4:
    black_jack()
    réponce_finale()
    Banque()
    point()
elif choix_de_jeu == 5:
    duel()
    réponce_finale()
    Banque()
    point()
else 
    roulette()
    réponce_finale()
    Banque()
    point()




