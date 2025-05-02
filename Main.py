from Core.Aléatoire.aléatoire import aléatoire #Donne un chiffre de façon aléatoire entre 1 et 6 afin de choisir le jeu. De plus, lorsqu'un chiffre est selectionné celui-ci ne peut être reselectionnée à moins de redémarer la fonction.
from Core.Pointage import Réponse_finale #Traduit la réponse du minijeu en vrai ou faux
from Core.Chargement.Debut_Jeu import DebutJeu #Lorsque l'espace est actonné le jeu peut commencer
from Affichage.Effacer import effacer #Permet d'effacer le jeu précédent
from Affichage.Erreur import game_over #Affichage du gagnant et perdant ainsi que les points gagnés entre les jeux
from Affichage.point import add #Affiche le nombre de points entre les jeux
from Maître_du_temps.Gregoire.countdown import countdown
from Affichage.Battle_canoe import battle_canoe #Battleship
from trivia_game import jouer_trivia #Quiz
from Taper import Taper  #Tape la taupe
from blackjack.blackjackV4 import black_jack #Black jack
from RouletteCasino import roulette #Roulette
 

pointage_joueur1 = int(0)
pointage_joueur2 = int(0)

#Démarage du programme des jeux  
DebutJeu()
#Tant que les deux jeux n'ont pas été joués
while (Réponse_finale.point_joueur1 + Réponse_finale.point_joueur2) != 6:
    choix_de_jeu = aléatoire() #Choix aléatoire du jeu
    choix_de_jeu = int(choix_de_jeu)
    if choix_de_jeu == 1: #Si le choix de jeu est 1
        battle_canoe() #Le jeu est joué
        Réponse_finale.reponsefinale(pointage_joueur1, pointage_joueur2) #Les pointages sont calculés en dehors les jeux
        game_over(Réponse_finale.resultat_mini_jeux) #Afficher quel joueur a gagné et les points gagnés
        add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2) #Afficher le nombre de points
        countdown() #Attendre 15 secondes pour voir l'affichage des points
        effacer() #Effacer l'affichage des points du jeu
        Réponse_finale.point_joueur1 = int(0) #Remettre les points à 0
        Réponse_finale.point_joueur2 = int(0)
    elif choix_de_jeu == 2:
        jouer_trivia()
        Réponse_finale.reponsefinale(pointage_joueur1, pointage_joueur2)
        game_over(Réponse_finale.resultat_mini_jeux)
        add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2)
        countdown()
        effacer()
        Réponse_finale.point_joueur1 = int(0)
        Réponse_finale.point_joueur2 = int(0)
    elif choix_de_jeu == 3:
        Taper()
        Réponse_finale.reponsefinale(pointage_joueur1, pointage_joueur2)
        game_over(Réponse_finale.resultat_mini_jeux)
        add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2)
        countdown()
        effacer()
        Réponse_finale.point_joueur1 = int(0)
        Réponse_finale.point_joueur2 = int(0)
    elif choix_de_jeu == 4:
        black_jack()
        Réponse_finale.reponsefinale(pointage_joueur1, pointage_joueur2)
        game_over(Réponse_finale.resultat_mini_jeux)
        add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2)
        countdown()
        effacer()
        Réponse_finale.point_joueur1 = int(0)
        Réponse_finale.point_joueur2 = int(0)
    elif choix_de_jeu == 5:
        print("duel") #Le code du jeu n'a pas réussi à fonctionner à temps
        add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2)
        countdown()
        effacer()
        Réponse_finale.point_joueur1 = int(0)
        Réponse_finale.point_joueur2 = int(0)
    else:
        roulette()
        Réponse_finale.reponsefinale(pointage_joueur1, pointage_joueur2) 
        game_over(Réponse_finale.resultat_mini_jeux)
        add(Réponse_finale.point_joueur1, Réponse_finale.point_joueur2)
        countdown()
        effacer()
        Réponse_finale.point_joueur1 = int(0)
        Réponse_finale.point_joueur2 = int(0)
else: #Lorsque tous les jeux ont été joués
    print("fin") 
    
    