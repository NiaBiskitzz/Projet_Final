
from Core.Aléatoire.aléatoire import aléatoire #Donne un chiffre de façon aléatoire entre 1 et 6 afin de choisir le jeu. De plus, lorsqu'un chiffre est selectionné celui-ci ne peut être reselectionnée à moins de redémarer la fonction.
from Core.Pointage.Banque import banque #Enregistre le nombre de points
from Core.Pointage.Réponse_finale import reponsefinale #Traduit la réponse du minijeu en vrai ou faux
from Core.Chargement.Debut_Jeu import DebutJeu #Lorsque l'espace est actonné le jeu peut commencer
from Affichage.Effacer import effacer #Permet d'effacer le jeu précédent
from Affichage.Erreur import game_over #Affichage du gagnant et perdant ainsi que les points gagnés entre les jeux
from Affichage.point import add #Affiche le nombre de points entre les jeux
import  #Battleship
import jouer_trivia
from Taper import Taper  #Tape la taupe
from black_jack import black_jack #Black jack
from duel import duel #Duel
from RouletteCasino import roulette() #Roulette

#Démarage du programme des jeux
DebutJeu()
#Sélection du jeu de façon aléatoire
choix_de_jeu = aléatoire()
choix_de_jeu = int(choix_de_jeu)
if choix_de_jeu == 1:
    battleship()
    reponsefinale() #Traduit réponse minijeu vrai ou faux
    banque() #Enregistre le nombre de points
    game_over() #Affiche le gagnant et perdant et les points gagnés après le jeu
    add() #Afficher le nombre de points entre les jeux
    effacer() #Effacer ce qui est dans le terminal pour le jeu
elif choix_de_jeu == 2:
    jouer_trivia()
    reponsefinale()
    banque()
    game_over()
    add()
    effacer()
elif choix_de_jeu == 3:
    Taper()
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




