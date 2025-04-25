import time
import datetime

# Crée une fonction
def countdown():

    # Entré utilisateur pour les heures, minutes et secondes
    h = int(0)
    m = int(0)
    s = int(15)

    #quand temps = 0 termine le jeu

    # Calcule le nombre total de secondes
    total_seconds = h * 3600 + m * 60 + s
 
    # While loop qui regarde si le tempes est 0
    # si pas a 0 -1 seconde 
    while total_seconds > 0:
 
        # Timer represente le temps restant
        timer = datetime.timedelta(seconds = total_seconds)
 
        # pause de une seconde
        time.sleep(1)
 
        # Reduit le temps d'une seconde tans que la boucle roule
        total_seconds -= 1

