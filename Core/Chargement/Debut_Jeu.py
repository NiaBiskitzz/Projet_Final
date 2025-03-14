def DebutJeu():
    """
    Lorsque cette touche est appuyée, le jeu commence
    """
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'space' :
        return