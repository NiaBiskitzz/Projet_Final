from HandTotal import calculate_hand_total
from Dealer import deal_card



def player_turn(deck, player_hand):
    while True:
        print("Player's hand:", player_hand, "Total:", calculate_hand_total(player_hand))
        action = input("Vous voulez hit ou stand? ").lower()
        
        if action == "hit":
            player_hand.append(deal_card(deck))
            if calculate_hand_total(player_hand) > 21:
                print("Busté!", player_hand, "Total:", calculate_hand_total(player_hand))
                return False
        else:
            return True
