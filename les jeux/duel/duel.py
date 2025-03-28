import keyboard
import time

def duel():
    
    
    
    print("1ère manche")
    passer_règle_1m= input("voulez vous avoir avoir les réglement de la manche? (yes or no)")
    if passer_règle_1m == "yes":
        print("Bienvenue dans le jeu de duel")
        time.sleep(3)
        print("ce jeux ce compose de 3 round et celle si est la première.Vous devez tirer sur l'autre joueur le plus rapidement possible après le temp donner")
        time.sleep(5)
        print("devez attendre que le décompte soit terminer pour tirer.Si un joeur tire avant que le décompte soi terminer le joeur qui a tiré à un pénalité")
    