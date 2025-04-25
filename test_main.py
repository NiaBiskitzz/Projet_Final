from Core.Aléatoire.aléatoire import aléatoire #Donne un chiffre de façon aléatoire entre 1 et 6 afin de choisir le jeu. De plus, lorsqu'un chiffre est selectionné celui-ci ne peut être reselectionnée à moins de redémarer la fonction.
from Core.Pointage.Réponse_finale import reponsefinale #Traduit la réponse du minijeu en vrai ou faux
from Core.chargement.Debut_Jeu import DebutJeu #Lorsque l'espace est actonné le jeu peut commencer
from Affichage.Effacer import effacer #Permet d'effacer le jeu précédent
from Affichage.Erreur import game_over #Affichage du gagnant et perdant ainsi que les points gagnés entre les jeux
from Affichage.point import add #Affiche le nombre de points entre les jeux
#from Taper import Taper  #Tape la taupe
#from black_jack import black_jack #Black jack
#from duel import duel #Duel
from RouletteCasino import roulette #Roulette
from Core.Pointage import Réponse_finale
 

pointage_joueur1 = int(1)
pointage_joueur2 = int(2)  
point_joueur1 = int(0)
point_joueur2 = int(0)

#Démarage du programme des jeux  
DebutJeu()
#Sélection du jeu de façon aléatoire
choix_de_jeu = aléatoire()
choix_de_jeu = int(choix_de_jeu)
if choix_de_jeu == 1:
    print("Battleship") 
    reponsefinale(pointage_joueur1, pointage_joueur2)
    game_over(pointage_joueur1)
    add()
    effacer()
elif choix_de_jeu == 2:
    print("trivia")
    reponsefinale(pointage_joueur1, pointage_joueur2)
    game_over(pointage_joueur1)
    add(point_joueur1, point_joueur2)
    effacer()
elif choix_de_jeu == 3:
    print("Taper")
    reponsefinale(pointage_joueur1, pointage_joueur2)
    game_over(pointage_joueur1)
    add(point_joueur1, point_joueur2)
    effacer()
elif choix_de_jeu == 4:
    print ("black_jack")
    reponsefinale(pointage_joueur1, pointage_joueur2)
    game_over(pointage_joueur1)
    add(point_joueur1, point_joueur2)
    effacer()
elif choix_de_jeu == 5:
    print("duel")
    reponsefinale(pointage_joueur1, pointage_joueur2)
    game_over(pointage_joueur1)
    add(point_joueur1, point_joueur2)
    effacer()
else:
    print("roulette")
    reponsefinale(pointage_joueur1, pointage_joueur2) 
    game_over(point_joueur1)
    add(point_joueur1, point_joueur2)
    effacer()