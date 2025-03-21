"""
Le jeu black jack utilise 52 cartes de poker(excluant les jokers). 
Chaque carte a une valeur entre 1 et 11. 
Le jeu se joue avec un donneur et un joueur. 
Le donneur distribue une carte cachée et une carte visible au joueur. 
Le joueur peut demander des cartes supplémentaires (« hit ») 
jusqu’à ce que le total de ses cartes soit supérieur à 21 (auquel cas il perd) ou jusqu’à 
ce qu’il décide de s’arrêter (« stand »). 
Dans ce cas, le donneur dévoile sa carte cachée et tire des cartes jusqu’à ce que le total de ses 
cartes soit supérieur à 16. Le joueur gagne si le total de ses cartes est supérieur à celui du donneur. 
Écrivez un programme qui simule plusieurs parties de black jack et affiche le pourcentage de 
parties gagnées par le joueur.
"""