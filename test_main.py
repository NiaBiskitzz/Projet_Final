from Core.Aléatoire.aléatoire import aléatoire #Donne un chiffre de façon aléatoire entre 1 et 6 afin de choisir le jeu. De plus, lorsqu'un chiffre est selectionné celui-ci ne peut être reselectionnée à moins de redémarer la fonction.
from Core.Pointage import Réponse_finale #Traduit la réponse du minijeu en vrai ou faux
from Core.Chargement.Debut_Jeu import DebutJeu #Lorsque l'espace est actonné le jeu peut commencer
from Affichage.Effacer import effacer #Permet d'effacer le jeu précédent
from Affichage.Erreur import game_over #Affichage du gagnant et perdant ainsi que les points gagnés entre les jeux
from Affichage.point import add #Affiche le nombre de points entre les jeux
from Maître_du_temps.Gregoire.countdown import countdown
#from Taper import Taper  #Tape la taupe
#from black_jack import black_jack #Black jack
#from duel import duel #Duel
#from RouletteCasino import roulette #Roulette
 

pointage_joueur1 = int(1)
pointage_joueur2 = int(2) 

#Démarage du programme des jeux  
DebutJeu()
#Sélection du jeu de façon aléatoire
choix_de_jeu = aléatoire()
choix_de_jeu = int(choix_de_jeu)
if choix_de_jeu == 1:
    print("Battleship") 
    Réponse_finale.reponsefinale(pointage_joueur1, pointage_joueur2)
    game_over(Réponse_finale.resultat_mini_jeux)
    add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2)
    countdown()
    effacer()
elif choix_de_jeu == 2:
    print("trivia")
    Réponse_finale.reponsefinale(pointage_joueur1, pointage_joueur2)
    game_over(Réponse_finale.resultat_mini_jeux)
    add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2)
    countdown()
    effacer()
elif choix_de_jeu == 3:
    print("Taper")
    Réponse_finale.reponsefinale(pointage_joueur1, pointage_joueur2)
    game_over(Réponse_finale.resultat_mini_jeux)
    add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2)
    countdown()
    effacer()
elif choix_de_jeu == 4:
    print ("black_jack")
    Réponse_finale.reponsefinale(pointage_joueur1, pointage_joueur2)
    game_over(Réponse_finale.resultat_mini_jeux)
    add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2)
    countdown()
    effacer()
elif choix_de_jeu == 5:
    print("duel")
    Réponse_finale.reponsefinale(pointage_joueur1, pointage_joueur2)
    game_over(Réponse_finale.resultat_mini_jeux)
    add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2)
    countdown()
    effacer()
else:
    print("roulette")
    Réponse_finale.reponsefinale(pointage_joueur1, pointage_joueur2) 
    game_over(Réponse_finale.resultat_mini_jeux)
    add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2)
    countdown()
    effacer()