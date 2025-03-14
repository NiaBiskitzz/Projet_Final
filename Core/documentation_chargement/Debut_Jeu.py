def DebutJeu():
    """
    Lorsque cette touche est appuyée, le jeu commence
    """
    print("Appuyer sur la touche 'espace' pour débuter.")

    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space' :
        return