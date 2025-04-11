from time import sleep

def decompte():# création de la fonction
    countdown = 5
    while countdown > 0:
        print(countdown)
        sleep(1)
        countdown -= 1
