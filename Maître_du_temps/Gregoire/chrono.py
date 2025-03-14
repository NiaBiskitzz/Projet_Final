import time
# permet de travailler avec une valeur de temps 
start_time = time.perf_counter() # prend une mesure de temps au début
 
#  code d'une jeu se trouve ici
 
end_time = time.perf_counter() # prend une mesure du temps à la fin
execution_time = end_time - start_time # calcule le temps d'exécution
 
print(f"Programme exécuté en : {execution_time: .5f} secondes") # affiche à l'utilisateur le temps d'exécution

