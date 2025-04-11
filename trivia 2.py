from random import random # importation des modules
from random import randint
def trivia_game():
    Films = {#dictionnaire pour les questions
        "Quel est le nom du pere de thor?": "Odin",
        "Quel était le nom de New York entre 1624 et 1664 ?": "New Amsterdam",
        "D'où vien SuperMan?": "Krypton",
        "Qui est réellement Batman?": "Bruce Wayne",
        "Quel est le nom du chien de Mickey Mouse?": "Pluto",
        "Quel est le nom du premier film de Star Wars?": "A New Hope"
    }

    Geographie = {"Quel pays possède le plus grand nombre d’îles dans le monde?": "Suède", "Quel est le plus petit pays du monde?": "Vatican", "Quel est le plus petit pays du monde?": "Vatican", "Quel est la capital du Canada": " Ottawa", "Citez le nom de la plus vaste chaine de montagne": "les Andes", "Citez le nom du plus long fleuve du monde": "le Nil", "Quel est le site naturel le plus bas de la planete terre": "la fosse de Mariannes"}


    kings_and_queens_of_rock = { "Who is known as the 'King of Rock and Roll'?": "Elvis Presley", "Who is known as the 'Queen of Rock and Roll'?": "Tina Turner", "Who is known as the 'Godfather of Soul'?": "James Brown", "Who is known as the 'King of the Blues'?": "B.B. King", "Who is known as the 'Queen of Soul'?": "Aretha Franklin", "Who is known as the 'King of Pop'?": "Michael Jackson", "Who is known as the 'Queen of Pop'?": "Madonna", "Who is known as the 'King of Punk'?": "Iggy Pop", "Who is known as the 'Queen of Punk'?": "Patti Smith", "Who is known as the 'King of Metal'?": "Ozzy Osbourne", "Who is known as the 'Queen of Metal'?": "Lita Ford", "Who is known as the 'King of Rockabilly'?": "Elvis Presley", "Who is known as the 'Queen of Rockabilly'?": "Wanda Jackson", "Who is known as the 'King of Country'?": "George Strait",}

    def switch_player(current_player, player_count):# fonction pour pointage de chaque joeur
        if player_count == 3:
            if current_player < 3:
                new_player = current_player + 1
            else:
                new_player = 1
        if player_count == 2:
            if current_player == 1:
                new_player = 2
        else:
                new_player = 1
        if player_count == 1:
            new_player = 1
    
        return new_player



    game_theme = input("Select 1 pour Films, 2 pour Geographie, 3 pour Kings and Queens of Rock!  ")#entré utilisateur pour le choix de question
    print (game_theme)
    game_data = {}
    if game_theme == "1":
        game_data = Films
    else:
        if game_theme == "2":
            game_data = Geographie
        else:
            if game_theme == "3":
                game_data = kings_and_queens_of_rock
            else:
                print("mauvaise selection, reesayer")

    game_length = len(game_data)# nombre de question
    fixed_game_length = game_length
    counter = 1
    scores = [0, 0, 0]
    questions = list(game_data)

    player_count = input("combien de joueur? (1 , 2, or 3)")# choix du nombre de joeur

    if player_count != "1" and player_count != "2" and player_count !="3": # si quelque chose d'autres est entré, message d'erreur
        print ("entre invalide - reesayer")
        player_count = 0
        counter = 100

    player_num = 1
    while counter <= fixed_game_length:
        print ("Ok " + "player " + str(player_num) + " c'est ton tour.  Answer question " + str(counter) + " of " + str(fixed_game_length))# dit a l'utilisateur combien de question à répondre
        question_num = randint(1, game_length) - 1
        question = questions[question_num]
        answer_question = input (question)
        if answer_question == game_data.get(question):
            scores [player_num-1] += 1
            print ("Correct! " + "vous avez fait un point. " + "tu a " + str(scores[player_num-1]) + " points.")# si bonne réponse+1score
        else: 
            print ("mauvais - la bonne reponse est " + game_data.get(question))
        counter += 1 
        questions.pop(question_num)
    
        game_length = game_length - 1
        new_player = switch_player(player_num, int(player_count))# si mauvaise -1 point
        player_num = new_player

    score_counter = 0#affiche le score après chaque question
    while score_counter < int(player_count):
        print ("Player " + str(score_counter+ 1) + " score: " + str(scores[score_counter]))
        score_counter += 1
