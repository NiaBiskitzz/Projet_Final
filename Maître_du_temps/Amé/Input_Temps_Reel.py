import keyboard

def InputTempsReel():
    """
    Lorsque les joueurs appuient sur une touche de clavier, il n'est pas nécessaire d'appuyer sur enter et compter le nombre de fois que la touche est activée

    Retour: nombre de fois que chaque joueur a appuyé sur la touche
    
    """
    score1 = 0
    score1 = int(score1)

    score2 = 0
    score2 = int(score2)

    a = True

    while (a == True):
        event1 = keyboard.read_event()
        if event1.event_type == keyboard.KEY_DOWN and event1.name == 's' :
            score1 = score1 + 1
            print(f"score du joueur 1: {score1}", f"score du joueur 2: {score2}", sep='\n')
        if event1.event_type == keyboard.KEY_DOWN and event1.name == 'k' :
            score2 = score2 + 1
            print(f"score du joueur 1: {score1}", f"score du joueur 2: {score2}", sep='\n')
    return f"score du joueur 1: {score1}", f"score du joueur 2: {score2}"

def DebutJeu():
    """
    Lorsque cette touche est appuyée, le jeu commence
    """
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space' :
        return