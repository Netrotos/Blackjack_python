#Blackjack by Netrotos & ChatGPT  7/23
#green computing concepts by ChatGPT

import random

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

def play_blackjack(balance):
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    while balance > 0:
        print("\n\nYour balance is:", balance)
        bet = int(input("Input bet: "))

        if bet <= 0 or bet > balance:
            print("Input valid bet.")
            continue

        kdc = random.choice(cards)
        udc = random.choice(cards)
        pc1 = random.choice(cards)
        pc2 = random.choice(cards)

        print("Dealer known card:", kdc)
        print("Your cards:", pc1, "&", pc2)

        vpc1 = card_value(pc1)
        vpc2 = card_value(pc2)
        vkdc = dealercard_value(kdc)
        vudc = dealercard_value(udc)

        pv = vpc1 + vpc2
        dv = vkdc + vudc

        if kdc == "A":
            surrender = int(input("Do you want to surrender and lose 1/2 your bet?\n0 - no, 1 - yes\n"))
            if surrender == 1:
                balance -= 0.5 * bet
                break

        elif (vpc1 + vpc2) == 21 and (vkdc + vudc) != 21:
            print("Blackjack!")
            balance += 0.5 * bet
            break

        elif (vpc1 + vpc2) == (vkdc + vudc) == 21:
            print("Tie!")
            break

        elif (vpc1 + vpc2) != 21 and (vkdc + vudc) == 21:
            print("Player lost!")
            balance -= 0.5 * bet
            break

        while True:
            play = int(input("Possible actions:\n1 - Hit\n2 - Double Down\n3 - Stand\n"))

            if play == 1:
                npc = random.choice(cards)
                print("New card:", npc)
                pv += card_value(npc)
                if pv > 21:
                    print("Player Bust!")
                    balance -= bet
                    break

            elif play == 2:
                if balance < (2 * bet):
                    print("Balance not enough to Double Down!")
                else:
                    npc2 = random.choice(cards)
                    print("Doubled your bet!")
                    print("New card:", npc2)
                    pv += card_value(npc2)
                    print("Dealer card revealed:", udc)
                    while dv <= 16:
                        dpc = random.choice(cards)
                        print("New dealer card:", dpc)
                        dv += dealercard_value(dpc)

                    if dv > 21:
                        print("Dealer Bust!")
                        balance += 2 * bet
                    elif pv > 21:
                        print("Player Bust!")
                        balance -= 2 * bet
                    elif dv > pv:
                        print("Player lost!")
                        balance -= 2 * bet
                    elif dv < pv:
                        print("Player won!")
                        balance += 2 * bet
                    elif dv == pv:
                        print("Tie!")
                    break

            elif play == 3:
                print("Dealer card revealed:", udc)
                while dv <= 16:
                    dpc = random.choice(cards)
                    print("New dealer card:", dpc)
                    dv += dealercard_value(dpc)

                if dv > 21:
                    print("Dealer Bust!")
                    balance += bet
                elif pv > 21:
                    print("Player Bust!")
                    balance -= bet
                elif dv > pv:
                    print("Player lost!")
                    balance -= bet
                elif dv < pv:
                    print("Player won!")
                    balance += bet
                elif dv == pv:
                    print("Tie!")
                break

            else:
                print("Invalid action. Please choose a valid action.")


if __name__ == "__main__":
    balance = int(input("Input balance: "))
    while balance <= 0:
        balance = int(input("Input valid balance: "))

    play_blackjack(balance)
