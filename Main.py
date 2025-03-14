#écrit un max de commentaire
import fonction_aléatoire
import Banque
import réponce_finale
import début_Jeu
import point #Afichage des point total
import jeu_1
import jeu_2
import jeu_3
import jeu_4
import jeu_5
import jeu_6

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



