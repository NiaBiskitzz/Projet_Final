import os

def effacer():
    """
    Cette fonction efface ce qui est écrit dans le terminal après ou avant un jeu
    """
    #La commande est égale à clear
    command = 'cls'

    #Mettre la commande dans le terminal
    os.system(command)
