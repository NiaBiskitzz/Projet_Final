def game_over(pointage_joueur1):
    pointage_joueur1:playeur1

    if  pointage_joueur1 == True: #si la donnée du joueur 1 est vrai sa veut dire qu'il obtient 1 point supplementaire et le joueur 2
        #perd cepandent il ne perd pas de point.
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
       

game_over(False)



        