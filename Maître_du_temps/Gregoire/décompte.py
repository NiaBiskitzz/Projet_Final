from time import sleep

def decompte():# création de la fonction
    countdown = 5 # notre temps dans ce cas si
    while countdown >= 0: # si le temps n'est pas a 0 le boucle continue
        print(countdown)# affiche le temps restant
        sleep(1)# pause de 1 seconde entre chiffre pour rendre sa smooth
        countdown -= 1 # -1 seconde après chaque boucle