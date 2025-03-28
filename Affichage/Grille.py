import random
list = ["▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢","▢"]
#mettre 🛇 dans (x,y)
x = 2
y = 2
list[y*4+x] = "🛇"
#for i in range(4):
    #print(list[i*4 +0],list[i*4 +1],list[i*4 +2],list[i*4 +3])

def battle_canoe():
    #Ensuite mettre les bateaux aleatoirement dasn la grille
    #fonction random
    bateau = random.randint(0,15)
    list[bateau] = "🛶"

battle_canoe()
for i in range(4):
    print(list[i*4 +0],list[i*4 +1],list[i*4 +2],list[i*4 +3])