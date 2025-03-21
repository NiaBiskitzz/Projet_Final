#écrit un max de commentaire
import fonction_aléatoire #donne un chiffre de façcon aléatoire entre 1 et 6.De plus lorsqu'un chiffre est selectionné celui si ne peut être reselectionée à moin de redémarer la fonction
import Banque #fonction qui enregistre le nombre de point
import réponce_finale 
import début_Jeu #cette fonction permet que lorsque l'espace est actonner lejeu peux commencer
import point #Afichage des point total
import jeu_1 #fonction du jeu 1
import jeu_2  #fonction du jeu 2
import jeu_3  #fonction du jeu 3
import jeu_4   #fonction du jeu 4
import jeu_5   #fonction du jeu 5
import jeu_6   #fonction du jeu 6

#démarage du programe des jeux
début_Jeu()
#Séléction du jeu de façon aléatoire
choix_de_jeu = fonction_aléatoire()
choix_de_jeu = int(choix_de_jeu)
if choix_de_jeu == 1:
    
    jeu_1()
    réponce_finale()
    Banque()
    point()
elif choix_de_jeu == 2:
    jeu_2()
    réponce_finale()
    Banque()
    point()
elif choix_de_jeu == 3:
    jeu_3()
    réponce_finale()
    Banque()
    point()
elif choix_de_jeu == 4:
    jeu_4()
    réponce_finale()
    Banque()
    point()
elif choix_de_jeu == 5:
    jeu_5()
    réponce_finale()
    Banque()
    point()
else 
    jeu_6()
    réponce_finale()
    Banque()
    point()



