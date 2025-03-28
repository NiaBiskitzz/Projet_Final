
from Core.Aléatoire.aléatoire import aléatoire #donne un chiffre de façcon aléatoire entre 1 et 6 afin de choisir le jeu. De plus, lorsqu'un chiffre est selectionné celui-ci ne peut être reselectionnée à moins de redémarer la fonction.
from Core.Pointage.Banque import banque #Enregistre le nombre de points
from Core.Pointage.Réponse_finale import reponsefinale #Traduit la réponse du minijeu en vrai ou faux
from Core.Chargement.Debut_Jeu import DebutJeu #Lorsque l'espace est actonné le jeu peut commencer
from Affichage.Effacer import effacer #Permet d'effacer le jeu précédent
from Affichage.Erreur import game_over #Affichage du gagnant et perdant ainsi que les points gagnés entre les jeux
from Affichage.point import add #Affiche le nombre de points entre les jeux
import  #Battleship
import  #Quiz
from Taper import Taper  #Tape la taupe
from black_jack import black_jack #Black jack
from duel import duel #Duel
import RouletteCasino #Roulette

#démarage du programme des jeux
DebutJeu()
#Séléction du jeu de façon aléatoire
choix_de_jeu = aléatoire()
choix_de_jeu = int(choix_de_jeu)
if choix_de_jeu == 1:
    battleship()
    reponsefinale()
    banque()
    game_over()
    add()
    effacer()
elif choix_de_jeu == 2:
    trivia()
    reponsefinale()
    banque()
    game_over()
    add()
    effacer()
elif choix_de_jeu == 3:
    tape_taupe()
    reponsefinale()
    banque()
    game_over()
    add()
    effacer()
elif choix_de_jeu == 4:
    black_jack()
    reponsefinale()
    banque()
    game_over()
    add()
    effacer()
elif choix_de_jeu == 5:
    duel()
    reponsefinale()
    banque()
    game_over()
    add()
    effacer()
else:
    roulette()
    reponsefinale()
    banque()
    game_over()
    add()
    effacer()




