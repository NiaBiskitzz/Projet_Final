import random
#import countdown# marche pas, il faut que le code roule pendant le countdown

def trivia_game1():
    questions1 = [
        {"question": "Quelle est la capitale de la France ?", "reponse": "Paris"},
        {"question": "Combien de continents y a-t-il ?", "reponse": "7"},
        {"question": "Quelle planète est connue comme la planète rouge ?", "reponse": "Mars"},
        {"question": "Quelle est la racine carrée de 81 ?", "reponse": "9"},
        {"question": "Quel est le plus grand océan sur Terre ?", "reponse": "Pacifique"}
    ]

def ask_questions1(player):
        print(f"\n{player}, c'est ton tour !")
        score = 0
        for q in questions1:
            user_reponse = input(q["question"] + " ")
            if user_reponse.lower() == q["reponse"].lower():
                print("Bonne réponse !")
                score += 1
            else:
                print(f"Mauvaise réponse ! La bonne réponse était : {q['reponse']}")
        return score


def trivia_game2():
    questions2 = [
        {"question": "Quel est le nom du pere de thor?", "reponse": "Odin"},
        {"question": "Quel était le nom de New York entre 1624 et 1664 ?", "reponse": "New Amsterdam"},
        {"question": "D'où vien SuperMan?", "reponse": "Krypton"},
        {"question": "Qui est réellement Batman?", "reponse": "Bruce Wayne"},
        {"question": "Quel est le nom du chien de Mickey Mouse?", "reponse": "Pluto"},
        {"question": "Quel est le nom du premier film de Star Wars?", "reponse": "A New Hope"}
    ]

    def ask_questions2(player):
        print(f"\n{player}, c'est ton tour !")
        score = 0
        for q in questions2:
            user_reponse = input(q["question"] + " ")
            if user_reponse.lower() == q["reponse"].lower():
                print("Bonne réponse !")
                score += 1
            else:
                print(f"Mauvaise réponse ! La bonne réponse était : {q['reponse']}")
        return score

    player1 = input("Nom du joueur 1 : ")
    player2 = input("Nom du joueur 2 : ")

    score1 = ask_questions1(player1)
    score2 = ask_questions2(player2)

    print(f"\nRésultats : {player1} a {score1} points, {player2} a {score2} points.")

    if score1 > score2:
        print(f"{player1} gagne !")
    elif score2 > score1:
        print(f"{player2} gagne !")
    else:
        print("Égalité ! C'est l'heure de Roche-Papier-Ciseaux.")

        def roche_papier_ciseaux():
            choices = ["Roche", "Papier", "Ciseaux"]
            print("Choisissez : Roche, Papier ou Ciseaux.")
            p1_choice = input(f"{player1}, fais ton choix : ")
            p2_choice = input(f"{player2}, fais ton choix : ")
            if p1_choice == p2_choice:
                print("Égalité, rejouez !")
                roche_papier_ciseaux()
            elif (p1_choice == "Roche" and p2_choice == "Ciseaux") or \
                 (p1_choice == "Papier" and p2_choice == "Roche") or \
                 (p1_choice == "Ciseaux" and p2_choice == "Papier"):
                print(f"{player1} gagne avec {p1_choice} contre {p2_choice} !")
            else:
                print(f"{player2} gagne avec {p2_choice} contre {p1_choice} !")

        roche_papier_ciseaux()

# Démarrer le jeu
trivia_game1()