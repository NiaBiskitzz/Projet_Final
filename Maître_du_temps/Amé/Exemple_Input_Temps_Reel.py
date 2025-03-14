import keyboard

score1 = 0
score1 = int(score1)

score2 = 0
score2 = int(score2)

a = True

while (a == True):
    event1 = keyboard.read_event()
    if event1.event_type == keyboard.KEY_DOWN and event1.name == 's' :
        score1 = score1 + 1
        print(f"score du joueur 1: {score1}", f"score du joueur 2: {score2}", sep='\n')
    if event1.event_type == keyboard.KEY_DOWN and event1.name == 'k' :
        score2 = score2 + 1
        print(f"score du joueur 1: {score1}", f"score du joueur 2: {score2}", sep='\n')