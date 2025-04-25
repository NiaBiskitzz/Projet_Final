# Jeu de trivia pour deux joueurs
from Core.Pointage import Réponse_finale

def jouer_trivia():
    pointage_joueur1, pointage_joueur2 = Réponse_finale.reponsefinale

    # Questions et réponses
    questions = [
        {"question": "Quelle est la capitale de la France ?", "reponse": "Paris"},
        {"question": "Combien y a-t-il de continents sur Terre ?", "reponse": "7"},
        {"question": "Qui a écrit 'Les Misérables' ?", "reponse": "Victor Hugo"},
        {"question": "Quelle est la planète la plus proche du Soleil ?", "reponse": "Mercure"},
        {"question": "En quelle année a commencé la Révolution française ?", "reponse": "1789"}
    ]

    # Scores
    score_joueur1 = 0
    score_joueur2 = 0

    # Jeu
    for i, q in enumerate(questions):
        print("\nQuestion", i + 1)
        if i % 2 == 0:
            print("-> Joueur 1")
            reponse = input(q["question"] + " ")
            if reponse.strip().lower() == q["reponse"].lower():
                print("Bonne réponse !")
                score_joueur1 += 1
            else:
                print("Mauvaise réponse. La bonne réponse était :", q["reponse"])
        else:
            print("-> Joueur 2")
            reponse = input(q["question"] + " ")
            if reponse.strip().lower() == q["reponse"].lower():
                print("Bonne réponse !")
                score_joueur2 += 1
            else:
                print("Mauvaise réponse. La bonne réponse était :", q["reponse"])

    # Résultats
    print("\n--- Résultats finaux ---")
    print("Joueur 1 :", score_joueur1, "point(s)")
    print("Joueur 2 :", score_joueur2, "point(s)")

    if score_joueur1 > score_joueur2:
        print("Le Joueur 1 gagne !")
    elif score_joueur2 > score_joueur1:
        print("Le Joueur 2 gagne !")
    else:
        print("Égalité parfaite !")

    pointage_joueur1 = score_joueur1
    pointage_joueur2 = score_joueur2
    return pointage_joueur1, pointage_joueur2