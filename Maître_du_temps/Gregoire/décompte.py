from time import sleep

def decompte():
    countdown = 5
    while countdown > 0:
        print(countdown)
        sleep(1)
        countdown -= 1