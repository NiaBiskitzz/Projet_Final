import time

class Timer: # regroupe trois fonctions pour calculer le temps que prend le code a s'executer
    def __init__(self):
        self.start = time.perf_counter()
 #demare le timer au debut du code
    def restart(self):
        self.start = time.perf_counter()
#permet de reinitialiser l'heure de depart
    def get_time(self):
        return time.perf_counter() - self.start
    # retourne le temps que le code a pris pour s'executer