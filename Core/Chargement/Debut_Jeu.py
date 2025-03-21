import keyboard

def DebutJeu():
    """
    Lorsque cette touche est appuyée, le jeu commence
    """
    print("Appuyer sur la touche 'espace' pour débuter.")

    #Lire les touches du clavier appuyées
    event = keyboard.read_event()
    #Si la touche espace est appuyée
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space' :
        #Sortir de la fonction
        return