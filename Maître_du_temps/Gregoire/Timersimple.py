#permet d'utiliser la classe Timer facilement   
from timeit import default_timer as Timer
timer = Timer()
 
# Votre code se trouve ici
 
print(f"Programme exécuté en : {timer(): .5f} secondes")