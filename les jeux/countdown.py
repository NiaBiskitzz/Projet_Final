import time
import datetime
 
# Crée une fonction
def countdown(h, m, s):
 
    # Calcule le nombre total de secondes
    total_seconds = h * 3600 + m * 60 + s
 
    # While loop qui regarde si le tempes est 0
    # si pas a 0 -1 seconde 
    while total_seconds > 0:
 
        # Timer represente le temps restant
        timer = datetime.timedelta(seconds = total_seconds)
        
        # affiche le temps restant
        print(timer, end="\r")
 
        # pause de une seconde
        time.sleep(1)
 
        # Reduit le temps d'une seconde tans que la boucle roule
        total_seconds -= 1
 
    print("Bzzzt! The countdown is at zero seconds!")
 
# Entré utilisateur pour les heures, minutes et secondes
h = input("Enter the time in hours: ")
m = input("Enter the time in minutes: ")
s = input("Enter the time in seconds: ")
countdown(int(h), int(m), int(s))

#quand temps = 0 termine le jeu