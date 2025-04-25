import random
#faire le case du jeu
list_joueur1 = ["▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢"]
list_joueur2 = ["▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢"]

#fonction du premier joueur
def battle_canoe_1():
    print("Joueur 1")
    for i in range(4):
        print(list_joueur1[i*4 +0],list_joueur1[i*4 +1],list_joueur1[i*4 +2],list_joueur1[i*4 +3])

#fonction du deuxieme joueur
def battle_canoe_2():
    print("Joueur 2")
    for i in range(4):
        print(list_joueur2[i*4 +0],list_joueur2[i*4 +1],list_joueur2[i*4 +2],list_joueur2[i*4 +3])
     
#Faire print les case du jeu afin de former un carré 
#Ensuite mettre les bateaux aleatoirement dasn la grille
#fonction random
def battle_canoe():
    #joueur 1   
    battle_canoe_1()
    bateau_joueur1 = (random.randint(0,15), random.randint(0,15))
    bateau_joueur1 = (1,1)
    list_joueur1[bateau_joueur1[0]*4+bateau_joueur1[1]]

    #joueur 2
    battle_canoe_2()
    bateau_joueur2 = (random.randint(0,15), random.randint(0,15))
    bateau_joueur2 = (3,1)
    list_joueur2[bateau_joueur2[0]*4+bateau_joueur2[1]]

    #les varriable de w et x joueur 1
    w = 0
    x = 1

    #les varriable de y et z joueur 2 
    y = 0
    z = 1

    while bateau_joueur1 != (w,x) and bateau_joueur2 != (y,z):
        #mettre 🛇 dans dans la case lorsque na pas la bonne case
        w = int(input())
        x = int(input())
        list_joueur1[x*4+w] = "🛇"

        y = int(input())
        z = int(input())
        list_joueur2[z*4+y] = "🛇"
        
        
        #print reussi et le bateau si sa donne la bonne combinaison et réessayer si pas la bonne combinaison
        if bateau_joueur1 == (w,x):
            list_joueur1[x*4+w] = "🛶" 
            battle_canoe_1()
            print("Bravo!!!")
        else:
            battle_canoe_1()
            print("Réessayer")

        if bateau_joueur2 == (y,z):
            list_joueur2[z*4+y] = "🛶" 
            battle_canoe_2()
            print("Bravo!!!")
        else:
            battle_canoe_2()
            print("Réessayer") 
            
        