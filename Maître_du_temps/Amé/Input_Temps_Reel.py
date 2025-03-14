import keyboard

def InputTempsReel():
    """
    Lorsque les joueurs appuient sur une touche de clavier, il n'est pas nécessaire d'appuyer sur enter et compter le nombre de fois que la touche est activée

    Retour: nombre de fois que chaque joueur a appuyé sur la touche
    
    """
    #Les scores au début sont à 0
    score1 = 0
    score1 = int(score1)

    score2 = 0
    score2 = int(score2)

    a = True

    #Pendant que a est égale à vrai
    while (a == True):
        #Lire les touches de clavier appuyées
        event1 = keyboard.read_event()
        #Si la touche appuyée est s
        if event1.event_type == keyboard.KEY_DOWN and event1.name == 's' :
            #Le score du joueur augmente de 1
            score1 = score1 + 1
            #Le score des joueurs est affiché
            print(f"score du joueur 1: {score1}", f"score du joueur 2: {score2}", sep='\n')
            #Si la touche appuyée est k
        if event1.event_type == keyboard.KEY_DOWN and event1.name == 'k' :
            score2 = score2 + 1
            print(f"score du joueur 1: {score1}", f"score du joueur 2: {score2}", sep='\n')
    #Le retour est le score des deux joueurs
    return f"score du joueur 1: {score1}", f"score du joueur 2: {score2}"
