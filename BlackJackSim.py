#An attempt to make a blackjack simulator

import random
import time

Cash = 20.00

Start = str(input("Play Blackjack | Y or N - "))

while True:
    if Start.upper() == "N":
        break
    elif Start.upper() != "Y":
        print("Enter a reasonable answer")
    else:

        while True:
            print("You have $", Cash, "0", sep="")
            Bet = float(input("Betting amount - "))
            if Bet > Cash or Bet < 0:
                print("Enter a reasonable amount")
            else:
                break

        AllCards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]*4
        random.shuffle(AllCards)
        first = AllCards.pop(random.randint(0,len(AllCards)-1))
        second = AllCards.pop(random.randint(0,len(AllCards)-1))

        dealerfirst = AllCards.pop(random.randint(0,len(AllCards)-1))
        dealersecond = AllCards.pop(random.randint(0,len(AllCards)-1))

        Acount = 0
        dAcount = 0

        insurance = "nil"
        Binsurance = 0
        win = False
        done = False
        breaker = False

        print("Your cards: ", first, second)
        print("Dealers cards: ", dealerfirst, "[?]")

        if first in ["J", "Q", "K"]:
            firstvalue = 10
        elif first == "A":
            firstvalue = 11
            Acount += 1
        else:
            firstvalue = first

        if second in ["J", "Q", "K"]:
            secondvalue = 10
        elif second == "A":
            secondvalue = 11
            Acount += 1
        else:
            secondvalue = second

        if dealerfirst in ["J", "Q", "K"]:
            dealerfirstvalue = 10
        elif dealerfirst == "A":
            dealerfirstvalue = 11
            dAcount += 1
        else:
            dealerfirstvalue = dealerfirst

        if dealersecond in ["J", "Q", "K"]:
            dealersecondvalue = 10
        elif dealersecond == "A":
            dealersecondvalue = 11
            dAcount += 1
        else:
            dealersecondvalue = dealersecond

        FSsum = firstvalue + secondvalue
        Dsum = dealerfirstvalue + dealersecondvalue

        time.sleep(0.2)

        if FSsum == 22:
            FSsum -= 10
            Acount - 1

        if FSsum == 21 and dealerfirstvalue < 10:
            print("Blackjack | You win")
            win = True
            Cash += Bet
            print("$", Cash, sep="")
        elif dealerfirstvalue >= 10:
            if Dsum == 21 and FSsum == 21:
                done = True
                win = True
                print(dealerfirst, dealersecond)
                print("Both sides have blackjacks")
            elif Dsum < 21 and FSsum == 21:
                done = True
                win = True
                print("Dealer's hand - ", dealerfirst, dealersecond)
                print("Blackjack | You Win")
                Cash += Bet
                print("$", Cash, sep="")
            while not done and Cash - Bet >= 3:
                insurance = str(input("Do you want to buy insurance for $3.00? | Y or N - "))
                if insurance.upper() == "Y":
                    Cash -= 3
                    time.sleep(0.2)
                    Binsurance = True
                    done = True
                elif insurance.upper() == "N":
                    time.sleep(0.2)
                    Binsurance = False
                    done = True
                else:
                    print("Try again")
                    time.sleep(0.2)

        done = False
        nextCards = [first, second]
        dealCards = [dealerfirst, dealersecond]
        while not done and win == False:
            Hit = str(input("Hit or Stand | H or S - "))
            if Hit.upper() == "H":
                temp = AllCards.pop(random.randint(0,len(AllCards)-1))
                nextCards.append(temp)
                print(nextCards)
                if temp in ["J", "Q", "K"]:
                    tempvalue = 10
                elif temp == "A":
                    tempvalue = 11
                    Acount += 1
                else:
                    tempvalue = temp
                FSsum += tempvalue
                if FSsum > 21 and Acount > 0:
                    FSsum -= 10
                    Acount -= 1
                elif FSsum > 21:
                    print("Busted")
                    win = True
                    done = True
                    Cash -= Bet
                    print("$", Cash, sep="")
                elif FSsum == 21:
                    done = True
                    time.sleep(0.2)
            elif Hit.upper() == "S":
                done = True
                time.sleep(0.2)
            else:
                print("Try again")
                time.sleep(0.2)

        if win == False:
            print(dealCards)
            if Dsum == 22:
                Dsum -= 10
                dAcount -= 1
            if Dsum >= 17:
                if Dsum == 21 and Binsurance == True:
                    print("Insurance saves the day")
                elif Dsum > FSsum:
                    win = True
                    print("You lose")
                    Cash -= Bet
                    print("$", Cash, sep="")
                elif Dsum < FSsum:
                    win = True
                    print("You win")
                    Cash += Bet
                    print("$", Cash, sep="")
                else:
                    print("Tie")
            else:
                done = False
                while not done:
                    temp = AllCards.pop(random.randint(0,len(AllCards)-1))
                    dealCards.append(temp)
                    print(dealCards)
                    if temp in ["J", "Q", "K"]:
                        tempvalue = 10
                    elif temp == "A":
                        tempvalue = 11
                        Acount += 1
                    else:
                        tempvalue = temp
                    Dsum += tempvalue
                    if Dsum > 21 and dAcount > 1:
                        Dsum -= 10
                        dAcount -= 1
                        done = True
                    elif Dsum > 21:
                        print("Dealer busted")
                        Cash += Bet
                        print("$", Cash, sep="")
                        done = True
                    elif Dsum >= 17:
                        done = True
                        if Dsum > FSsum:
                            win = True
                            print("You loose")
                            Cash -= Bet
                            print("$", Cash, sep="")
                        elif Dsum < FSsum:
                            win = True
                            print("You win")
                            Cash += Bet
                            print("$", Cash, sep="")
                        else:
                            print("Tie")

        if Cash > 0:
            while True:
                Start = str(input("Play Blackjack | Y or N - "))
                if Start.upper() == "Y":
                    break
                elif Start.upper() != "N":
                    print("Enter a reasonable answer")
                else:
                    breaker = True
                    break
            if breaker == True:
                break
        if Cash <= 0:
            text = "You're broke"
