#Blackjack by Netrotos 7/23 for graphic calculator (+compact and error fixed)

import random

balance = int(input("Input balance: "))
if balance <= 0:
    balance = int(input("Input balance: "))
        
def card_value(card):
    if card[0] in ["J", "Q", "K"]:
        return 10
    elif card[0] == "A":
        av = int(input("A value (1/11): "))
        while av!=1 and av!=11:
            av = int(input("A value (1/11): "))
        else:
            return av
    else:
        return int(card.split()[0])

def dealercard_value(card):
    if card[0] in ["J", "Q", "K"]:
        return 10
    elif card[0] == "A":
        return 11
    else:
        return int(card.split()[0])

while balance > 0:
    print("\nYour balance is: ", balance)
    bet = int(input("Input bet: "))
    if bet > balance or bet <= 0:
        bet = int(input("Input bet: "))

    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    kdc = random.choice(cards)
    udc = random.choice(cards)
    pc1 = random.choice(cards)
    pc2 = random.choice(cards)

    print("Dealer known card: " + kdc)
    print("Your cards: ", pc1 + " & " + pc2)

    vpc1 = card_value(pc1)
    vpc2 = card_value(pc2)
    vkdc = dealercard_value(kdc)
    vudc = dealercard_value(udc)
        

    if kdc == "A":
        surrender = int(input("ff and (-1/2) bet?\n0 - no, 1 - yes\n"))
        while surrender != 0 and surrender != 1:
            print("Input valid answer")
            surrender = int(input("ff and -1/2 bet?\n0 - no, 1 - yes\n"))
        if surrender == 1:
            balance -= (0.5 * bet)
            continue

    pv = vpc1 + vpc2
    dv = vkdc + vudc
    
    if (vpc1 + vpc2) == 21 and (vkdc + vudc) != 21:
        print("Blackjack!")
        balance += 0.5 * bet
        continue
    
    elif (vpc1 + vpc2) == (vkdc + vudc) == 21:
        print("Tie!")
        continue
    
    elif (vpc1 + vpc2) != 21 and (vkdc + vudc) == 21:
        print("Player lost!")
        balance -= 0.5 * bet
        continue
        
    while True:
        play = int(input("1 - Hit\n2 - Double Down\n3 - Stand\n"))
    
        if play == 1:
            npc = random.choice(cards)
            print("New card: ", npc)
            pv += card_value(npc)
            continue
        
        elif play == 2:
                if balance < (2 * bet):
                    print("Balance not enough!")
                else:
                    npc2 = random.choice(cards)
                    print("* 2 your bet!")
                    print("New card: ", npc2)
                    pv += card_value(npc2)
                    print("Dealer card: ", udc)
                    while dv <= 16:
                        dpc = random.choice(cards)
                        print("New d card: ", dpc)
                        dv += dealercard_value(dpc)
                    if dv > 21 and pv > 21:
                        print("Tie!")
                    elif pv > 21:
                        print("Player Bust!")
                        balance -= (2 * bet)
                    elif pv == dv:
                        print("Tie!")
                    elif dv > pv and pv <= 21 and dv <= 21:
                        print("Player lost!")
                        balance -= (2 * bet)
                    elif dv < pv and pv <= 21 and dv <= 21:
                        print("Player won!")
                        balance += (2 * bet)
                    elif dv > 21:
                        print("Dealer Bust!")
                        balance += (2 * bet)
                    break

        elif play == 3:
            print("Dealer card: ", udc)
            while dv <= 16:
                dpc = random.choice(cards)
                print("New d card: ", dpc)
                dv += dealercard_value(dpc)
            if dv > 21 and pv > 21:
                print("Tie!")
            elif pv > 21:
                print("Player Bust!")
                balance -= bet
            elif pv == dv:
                print("Tie!")
            elif dv > pv and pv <= 21 and dv <= 21:
                print("Player lost!")
                balance -= bet
            elif dv < pv and pv <= 21 and dv <= 21:
                print("Player won!")
                balance += bet
            elif dv > 21:
                print("Dealer Bust!")
                balance += bet
            break

        else:
            print("Invalid action.")
