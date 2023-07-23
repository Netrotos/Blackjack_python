#Blackjack by Netrotos  7/23

import random

balance=int(input("Input balance: "))
if  balance<=0:
    balance=int(input("Input valid balance: "))
        
def card_value(card):
    if card.startswith(("J", "Q", "K")):
        return 10
    elif card.startswith("A"):
        return int(input("Input ace value: 1 or 11: "))
    else:
        return int(card.split()[0])

def dealercard_value(card):
    if card.startswith(("J", "Q", "K")):
        return 10
    elif card.startswith("A"):
        return 11
    else:
        return int(card.split()[0])


while balance > 0:
    print(" \n \nYour balance is: " , balance)
    bet = int(input("Input bet: "))
    if  (bet > balance) or (bet <= 0):
        bet=int(input("Input valid bet: "))


    cards=["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    kdc=random.choice(cards)
    udc=random.choice(cards)
    pc1=random.choice(cards)
    pc2=random.choice(cards)

    print("Dealer known card: "+ kdc)
    print("Your cards: ", pc1+" & "+pc2)

    vpc1 = card_value(pc1)
    vpc2 = card_value(pc2)
    vkdc = dealercard_value(kdc)
    vudc = dealercard_value(udc)
        
    pv = vpc1+vpc2
    dv = vkdc+vudc


    if kdc=="A":
        surrender=int(input("Do you want to surrender and lose 1/2 your bet?\n0 - no, 1 - yes\n"))
        while surrender != 0 and surrender != 1:
            print("Input valid answer")
            surrender=int(input("Do you want to surrender and lose 1/2 your bet?\n0 - no, 1 - yes\n"))
        if surrender==1:
            balance-= (.5 * bet)
            break

    elif (vpc1+vpc2)==21 and (vkdc+vudc)!=21:
        print ("Blackjack!")
        balance += 0.5 * bet
        break
    
    elif (vpc1+vpc2) == (vkdc+vudc)==21:
        print ("Tie!")
        break
    
    elif (vpc1+vpc2)!=21 and (vkdc+vudc)==21:
        print ("Player lost!")
        balance -= 0.5 * bet
        break


    while True:
        play = int(input("Possible actions:\n1 - Hit\n2 - Double Down\n3 - Stand\n"))
    
        if play ==1:
            npc=random.choice(cards)
            print("New card: " , npc)
            pv+=card_value(npc)
            continue
        
        while play==2 and (balance < (2 * bet)):
            print("Balance not enough to Double Down!")
            break

        if play == 2 and (balance>= (2 * bet)):
            npc2=random.choice(cards)
            print("Doubled your bet!")
            print("New card: " , npc2)
            pv+=card_value(npc2)
            bet+=bet
            print("Dealer card revealed: " , udc)
            while dv <= 16:
                dpc=random.choice(cards)
                print("New dealer card: " , dpc)
                dv+=dealercard_value(dpc)
            if dv>21 and pv>21:
                print("Tie!")
            elif pv > 21:
                print ("Player Bust!")
                balance-= 2 * bet
            elif (dv>pv and pv <= 21 and dv <= 21):
                print("Player lost!")
                balance-= 2 * bet
            elif pv == dv:
                print("Tie!")
            elif (dv<pv and pv <= 21 and dv <= 21):
                print("Player won!")
                balance+= 2 * bet
            elif dv>21:
                print ("Dealer Bust!")
                balance+= 2 * bet
            break

        elif play == 3:
            print("Dealer card revealed: " , udc)
            while dv <= 16:
                dpc=random.choice(cards)
                print("New dealer card: " , dpc)
                dv+=dealercard_value(dpc)
            if dv>21 and pv>21:
                print("Tie!")
            elif pv > 21:
                print ("Player Bust!")
                balance-=bet
            elif pv == dv:
                print("Tie!")
            elif (dv>pv and pv <= 21 and dv <= 21):
                print("Player lost!")
                balance-=bet
            elif (dv<pv and pv <= 21 and dv <= 21):
                print("Player won!")
                balance+= bet
            elif dv>21:
                print ("Dealer Bust!")
                balance+= bet
            break

        else:
            print("Invalid action. Please choose a valid action.")
