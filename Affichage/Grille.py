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
list[bateau[0]*4+bateau[1]]
#list[bateau] = "🛶"

#les varriable de x et y
x = 0
y = 1

while bateau != (x,y):
#mettre 🛇 dans dans la case lorsque na pas la bonne case
    x = int(input())
    y = int(input())
    list[y*4+x] = "🛇"
#rappler la fonction pour que la grille reappparait avec le signe qui veut dire quon ne la pas eu 
    battle_canoe()
    
    #print reussi et le bateau si sa donne la bonne combinaison et réessayer si pas la bonne combinaison
    if bateau == (x,y):
      list[y*4+x] = "🛶" 
      battle_canoe()
      print("Bravo!!!")
    else:
        print("Réessayer")

     
    



