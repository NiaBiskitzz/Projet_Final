def game_over(game):
    pointage_joueur1:playeur1
    pointage_joueur2:playeur2

    if  pointage_joueur1 == True:
        pointage_joueur2 = not(pointage_joueur1)
        print("    Playeur 1   ")
        print("________________")
        print("|              |")
        print("|   +1 point   |")
        print("|______________|")
        print("   Playeur 2    ")
        print("________________")
        print("|              |")
        print("|    PERDU!    |")
        print("|______________|")
    if  pointage_joueur1 == False:
        pointage_joueur2 = not(pointage_joueur1)
        print("    Playeur 1   ")
        print("________________")
        print("|              |")
        print("|    PERDU!    |")
        print("|______________|")
        print("   Playeur 2    ")
        print("________________")
        print("|              |")
        print("|   +1 point   |")
        print("|______________|")
       

game_over(True, False)



        