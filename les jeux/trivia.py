"""trivia questions
deux joueurs
chaque joueur doit repondre a 5 questions
chaque bonne reponse = 1 point
le joueur avec le plus de point gagne 
si egalite, roche papier ciseaux"""

import time
import datetime
import random
import countdown

print(countdown.countdown(0, 10, 0))





input("Voulez vous savoir comment jouer?")
if input == "oui":
    print("Le but du jeu est de repondre correctement au plus de question possible")
else:
    print("D'accord, commencons le jeu")




Questions = {
    "Quel est le nom du pere de thor?": "Odin",
    "Quel était le nom de New York entre 1624 et 1664 ?:" : "New Amsterdam",
    "D'où vien SuperMan?": "Krypton",
    "Qui est réellement Batman?": "Bruce Wayne",
    "Quel est le nom du chien de Mickey Mouse?": "Pluto",
    "Quel est le nom du premier film de Star Wars?": "A New Hope",
}

def ask_questionJ1(Question):
    print(Question)
    reponse = input("Reponse: ")
    return reponse

