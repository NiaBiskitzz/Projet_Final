import keyboard #Permet d'observer les touches appuyées du clavier
import datetime #Permet d'observer le temps

def InputTempsReel():
    """
    Lorsque les joueurs appuient sur une touche de clavier, il n'est pas nécessaire d'appuyer sur enter et compter le nombre de fois que la touche est activée

    Retour: nombre de fois que chaque joueur a appuyé sur la touche
    
    """
    #Le score du joueur1 au début est de 0
    score1 = 0
    score1 = int(score1)

    #Le score du joueur2 au début est de 0
    score2 = 0
    score2 = int(score2)

    #Observer le temps pour déterminer le temps de début
    TempsDebut = datetime.datetime.now()

    #Regarder le temps
    TempsFin = datetime.datetime.now()

    #Tant qu'il n'y a pas 5 secondes entre le temps de départ et maintenant
    while ((TempsFin - TempsDebut) < 5):
        #Lire les touches de clavier appuyées
        event1 = keyboard.read_event()
        #Si la touche appuyée est s
        if event1.event_type == keyboard.KEY_DOWN and event1.name == 's' :
            #Le score du joueur1 augmente de 1
            score1 = score1 + 1
            #Si la touche appuyée est k
        if event1.event_type == keyboard.KEY_DOWN and event1.name == 'k' :
            #Le score du joueur2 augmente de 1
            score2 = score2 + 1
        #Le score des joueurs est affiché
        print(f"score du joueur 1: {score1}", f"score du joueur 2: {score2}", sep='\n')
        #Revérifier le temps 
        TempsFin = datetime.datetime.now()
    else:
        print("Fin du jeu")
    #Le retour est le score des deux joueurs
    return score1, score2
