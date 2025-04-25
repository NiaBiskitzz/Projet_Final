import random
#faire le case du jeu
list = ["▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢"]
def battle_canoe():
    for i in range(4):
        print(list[i*4 +0],list[i*4 +1],list[i*4 +2],list[i*4 +3])
    #Faire print les case du jeu afin de former un carré 
battle_canoe()
        #Ensuite mettre les bateaux aleatoirement dasn la grille
        #fonction random

bateau = (random.randint(0,15), random.randint(0,15))
bateau = (1,1)
list[bateau*4+bateau]
#list[bateau] = "🛶"

x = int(input())
y = int(input())

while bateau != (x,y):

    #mettre 🛇 dans (x,y)
    x = int(input())
    y = int(input())
    list[y*4+x] = "🛇"
#print reussi si sa donne la bonne combinaison 
    if bateau == (x,y):
      print("Reussi")
    else:
        print("Raté")

     
    



