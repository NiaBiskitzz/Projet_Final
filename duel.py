import keyboard
import time
import datetime

def duel():
    Player1_point =int(0)
    Player2_point =int(0)

    
    print("1ère manche")#début de la première manche
    passer_règle_1m= input("voulez vous avoir avoir les réglement de la manche? (yes or no)")#içi je créer une fonction qui demande si l'utilisateur veut connaitre les réglements
    if passer_règle_1m == "yes":
        print("Bienvenue dans le jeu de duel")
        time.sleep(3)
        print("ce jeux ce compose de 3 round et celle si est la première.Vous devez tirer sur l'autre joueur le plus rapidement possible après le temp donner")
        time.sleep(5)
        print("devez attendre que le décompte soit terminer pour tirer.Si un joeur tire avant que le décompte soi terminer le joeur qui a tiré à un pénalité")
    round_starting_time = datetime.datetime.now()
    starter_number_1 = ( round_starting_time + datetime.timedelta(seconds=5) )#ici je créer une variable qui va me permettre de savoir quand le décompte est terminer
    if starter_number_1 < datetime.datetime.now():
        print("gooooo tue l'autre!")
    event1 = keyboard.read_event()
    if (event1.event_type == keyboard.KEY_DOWN and event1.name == 's' ) and ( datetime.datetime.now() >= starter_number_1 ):
        Player1_point = Player1_point + 1
        print("Hahahahahahahahahah le jouer 2 à perdue")
    if (event1.event_type == keyboard.KEY_DOWN and event1.name == 'k' ) and ( datetime.datetime.now() >= starter_number_1 ):
        Player2_point = Player2_point + 1
        print("Hahahahahahahahahah le jouer 1 à perdue")
    if (event1.event_type == keyboard.KEY_DOWN and event1.name == 's' ) and ( datetime.datetime.now() < starter_number_1 ):
        Player2_point = Player2_point + 1
        print("Hahahahahahahahahah le jouer 1 à perdue.Tire le bon temp la prochaime fois!")
    if (event1.event_type == keyboard.KEY_DOWN and event1.name == 'k' ) and ( datetime.datetime.now() < starter_number_1 ):
        Player1_point = Player1_point + 1
        print("Hahahahahahahahahah le jouer 2 à perdue.Tire le bon temp la prochaime fois!")
    print("Fin de la manche 1")#fin de la première manche
    print("score du joueur 1: ", Player1_point, "score du joueur 2: ", Player2_point)#affichage du score des deux joueurs
    time.sleep(3)
    print("2ème manche")#début de la deuxième manche
    passer_règle_2m= input("voulez vous avoir avoir les réglement de la manche? (yes or no)")#içi je créer une fonction qui demande si l'utilisateur veut connaitre les réglements
    if passer_règle_2m == "yes":
        print("Bienvenue dans la deuxième manche")
        time.sleep(3)
        print("ce jeux ce compose de 3 round et celle si est la deuxième.Vous devez tirer sur l'autre joueur le plus rapidement possible après 15 secondes")
        time.sleep(5)
        print("dans cette manche il n'aurras pas de décompte.Vous devez utilisée votr instin de cow boy pour tuer l'adverdsaire")
    round_starting_time_2 = datetime.datetime.now()
    starter_number_2 = ( round_starting_time_2 + datetime.timedelta(seconds=15) )#ici je créer une variable qui va me permettre de savoir quand le décompte est terminer
    event2 = keyboard.read_event()
    if (event2.event_type == keyboard.KEY_DOWN and event2.name == 's' ) and ( datetime.datetime.now() >= starter_number_2 ):
        Player1_point = Player1_point + 1
        print("Hahahahahahahahahah le jouer 2 à perdue")
    if (event2.event_type == keyboard.KEY_DOWN and event2.name == 'k' ) and ( datetime.datetime.now() >= starter_number_2 ):
        Player2_point = Player2_point + 1
        print("Hahahahahahahahahah le jouer 1 à perdue")
    if (event2.event_type == keyboard.KEY_DOWN and event2.name == 's' ) and ( datetime.datetime.now() < starter_number_2 ):
        Player2_point = Player2_point + 1
        print("Hahahahahahahahahah le jouer 1 à perdue.Tire le bon temp la prochaime fois!")
    if (event2.event_type == keyboard.KEY_DOWN and event2.name == 'k' ) and ( datetime.datetime.now() < starter_number_2 ):
        Player1_point = Player1_point + 1
        print("Hahahahahahahahahah le jouer 2 à perdue.Tire le bon temp la prochaime fois!")
    print("Fin de la manche 2")#fin de la deuxième manche
    
    print("score du joueur 1: ", Player1_point, "score du joueur 2: ", Player2_point)#affichage du score des deux joueurs
    time.sleep(3)
    print("3ème manche et dernière manche")#début de la troisième manche
    passer_règle_3m= input("voulez vous avoir avoir les réglement de la manche? (yes or no)")#içi je créer une fonction qui demande si l'utilisateur veut connaitre les réglements
    if passer_règle_3m == "yes":
        print("Bienvenue dans la troisième manche")
        time.sleep(3)
        print("ce jeux ce compose de 3 round et celle si est la troisième.Vous devez tirer sur l'autre joueur le plus rapidement possible après 15 secondes.Attention les points sont triplés")
        time.sleep(5)
        print("il a toujous pas de décompte mais les points sont triplés")
    round_starting_time_3 = datetime.datetime.now()
    starter_number_3 = ( round_starting_time_3 + datetime.timedelta(seconds=15) )#ici je créer une variable qui va me permettre de savoir quand le décompte est terminer
    event3 = keyboard.read_event()
    if (event3.event_type == keyboard.KEY_DOWN and event3.name == 's' ) and ( datetime.datetime.now() >= starter_number_3 ):
        Player1_point = Player1_point + 3
        print("Hahahahahahahahahah le jouer 2 à perdue")
    if (event3.event_type == keyboard.KEY_DOWN and event3.name == 'k' ) and ( datetime.datetime.now() >= starter_number_3 ):
        Player2_point = Player2_point + 3
        print("Hahahahahahahahahah le jouer 1 à perdue")
    if (event3.event_type == keyboard.KEY_DOWN and event3.name == 's' ) and ( datetime.datetime.now() < starter_number_3 ):
        Player2_point = Player2_point + 3
        print("Hahahahahahahahahah le jouer 1 à perdue.Tire le bon temp la prochaime fois!")
    if (event3.event_type == keyboard.KEY_DOWN and event3.name == 'k' ) and ( datetime.datetime.now() < starter_number_3 ):
        Player1_point = Player1_point + 3
        print("Hahahahahahahahahah le jouer 2 à perdue.Tire le bon temp la prochaime fois!")
    print("Fin de la manche 3")#fin de la troisième manche
    if Player1_point > Player2_point:
        Win = True
    if Player1_point < Player2_point:
        Win = False
    return Win

    
