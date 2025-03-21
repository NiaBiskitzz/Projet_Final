#Le jeux de la roulette du casino a 2 joueurs 
print("Bienvenue au jeux de la roulette du casino!")
#Le joueur 1 choisi un nombre entre 0 et 36
print("Joueur 1, choisissez un nombre entre 0 et 36")
#Le joueur 2 choisi un nombre entre 0 et 36
print("Joueur 2, choisissez un nombre entre 0 et 36")
#La roulette choisi un nombre alléatoire entre 0 et 36
import random
nombre_roulette = random.randint(0, 36)
#Affiches le nombre de la roulette et les chiffres paires sont noirs et les chiffres impaires sont rouges 
print("Le nombre de la roulette est:", nombre_roulette)
if nombre_roulette % 2 == 0:
    print("Le nombre est noir")
else:
    print("Le nombre est rouge")
#Si le joueur 1 choisi le meme nombre que la roulette, le joueur 1 gagne 5 ponits
#Si le joueur 2 choisi le meme nombre que la roulette, le joueur 2 gagne 5 points
#Si le joueurs 1 a la meme couleur que la roulette, le joueur 1 gagne 1 point
#Si le joueurs 2 a la meme couleur que la roulette, le joueur 2 gagne 1 point
if nombre_roulette == joueur1:
    print("Joueur 1 gagne 5 points")
elif nombre_roulette == joueur2:
    print("Joueur 2 gagne 5 points")
if nombre_roulette % 2 == 0 and joueur1 % 2 == 0:
    print("Joueur 1 gagne 1 point")
elif nombre_roulette % 2 == 0 and joueur2 % 2 == 0:
    print("Joueur 2 gagne 1 point")
