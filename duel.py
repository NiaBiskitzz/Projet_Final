import keyboard
import time

def duel():
   

    
    print("1ère manche")#début de la première manche
    passer_règle_1m= input("voulez vous avoir avoir les réglement de la manche? (yes or no)")#içi je créer une fonction qui demande si l'utilisateur veut connaitre les réglements
    if passer_règle_1m == "yes":
        print("Bienvenue dans le jeu de duel")
        time.sleep(3)
        print("ce jeux ce compose de 3 round et celle si est la première.Vous devez tirer sur l'autre joueur le plus rapidement possible après le temp donner")
        time.sleep(5)
        print("devez attendre que le décompte soit terminer pour tirer.Si un joeur tire avant que le décompte soi terminer le joeur qui a tiré à un pénalité")
    round_starting_time = time.now()

    event1 = keyboard.read_event()
    if (event1.event_type == keyboard.KEY_DOWN and event1.name == 's' ) and ( round_starting_time ):
    
    if (event1.event_type == keyboard.KEY_DOWN and event1.name == 'k' ) and ( round_starting_time ):
