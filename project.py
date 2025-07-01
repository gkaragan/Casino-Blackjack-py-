from card_deck import *
import sys
import re


def main():
    print("\nWELCOME TO CASINO BLACKJACK!\n")
    while True:
        balance = 0
        start = option()
        if start == "play":
            balance = deposit_money()
            while balance > 0:
                while True:
                    confirmation = input(
                        "\nType 'p' to keep playing or type 'w' to withdraw your money: "
                    ).strip().lower()
                    if confirmation == "p":
                        stake = bet(balance)
                        print(f"\nBalance: $ {balance}\nStake: $ {stake}\n")
                        result = game()
                        if result == "WIN":
                            balance += stake
                            print(f"\nYou Win!\n\nBalance: $ {balance}")
                        elif result == "LOSS":
                            balance -= stake
                            print(f"\nYou Lose!\n\nBalance: $ {balance}")
                        else:
                            print(f"\nDraw!\n\nBalance: $ {balance}")
                        if balance == 0:
                            print("\nInsufficient funds")
                            break
                    elif confirmation == "w":
                        sys.exit(
                            f"\nYour withdrawal of $ {balance} has been approved. Goodbye!"
                        )
                    else:
                        continue
        continue


def game():
    deck = Deck()
    deck.shuffle()
    player_hand = [f"|{deck[0]}|", f"|{deck[2]}|"]
    dealer_hand = [f"|{deck[1]}|", f"|{deck[3]}|"]
    dealer_count = hand_counter(dealer_hand)
    player_count = hand_counter(player_hand)
    print(f"Dealer: |{deck[1]}| |?|\nPlayer:", *player_hand)
    i = 4
    while True:
        print()
        if player_count == 21:
            print("BLACKJACK!")
            if dealer_count == 21:
                print("\nDealer: ", *dealer_hand)
                print("Player: ", *player_hand)
                return "DRAW"
            else:
                print("\nDealer: ", *dealer_hand)
                print("Player: ", *player_hand)
                while dealer_count < player_count:
                    dealer_hand.append(f"|{deck[i]}|")
                    i += 1
                    dealer_count = hand_counter(dealer_hand)
                    print("\nDealer: ", *dealer_hand)
                    print("Player: ", *player_hand)
                if dealer_count == 21:
                    return "DRAW"
                else:
                    return "WIN"
        decision = input("Select an option: hit/stand ").strip().lower()
        if decision == "hit":
            player_hand.append(f"|{deck[i]}|")
            print(f"\nDealer: |{deck[1]}| |?|\nPlayer:", *player_hand)
            player_count = hand_counter(player_hand)
            i += 1
            if player_count == 21:
                print("\nBLACKJACK")
                print(f"\nDealer: |{deck[1]}| |{deck[3]}|\nPlayer:", *player_hand)
                while dealer_count < player_count:
                    dealer_hand.append(f"|{deck[i]}|")
                    print("\nDealer:", *dealer_hand)
                    print("Player:", *player_hand)
                    i += 1
                    dealer_count = hand_counter(dealer_hand)
                if dealer_count == 21:
                    return "DRAW"
                else:
                    return "WIN"
            elif player_count > 21:
                print("\nBUST")
                print(f"\nDealer: |{deck[1]}| |{deck[3]}|\nPlayer:", *player_hand)
                while dealer_count < 17:
                    dealer_hand.append(f"|{deck[i]}|")
                    print(f"\nDealer: ", *dealer_hand)
                    print(f"Player: ", *player_hand)
                    i += 1
                    dealer_count = hand_counter(dealer_hand)
                if 17 <= dealer_count <= 21:
                    return "LOSS"
                else:
                    return "DRAW"
        if decision == "stand":
            print(f"\nDealer: |{deck[1]}| |{deck[3]}|\nPlayer:", *player_hand)
            if dealer_count <= player_count:
                while dealer_count <= player_count:
                    dealer_hand.append(f"|{deck[i]}|")
                    i += 1
                    dealer_count = hand_counter(dealer_hand)
                    print(f"\nDealer:", *dealer_hand)
                    print(f"Player:", *player_hand)
                    print()
                    if player_count < dealer_count <= 21:
                        return "LOSS"
                    elif dealer_count > 21:
                        return "WIN"
                break
            elif dealer_count > player_count:
                return "LOSS"


def hand_counter(list):
    count = 0
    raw_values = [i.lower() for i in list]
    for i in raw_values:
        if i[1] in ["k", "q", "j"] or i[1:3] == "10":
            i = 10
            count += 10
        elif i[1] == "a":
            if count + 11 > 21:
                count += 1
            elif count + 11 == 21:
                count += 11
            else:
                count += 11
        else:
            count += int(i[1])
    return count


def option():
    while True:
        start = input("\nSelect an option: play/exit ").strip().lower()
        if start == "play":
            return "play"
        elif start == "exit":
            sys.exit("\nGoodbye!")


def deposit_money():
    while True:
        deposit = input(
            "\nEnter deposit amount (minimum $1, maximum $1000000): $ "
        ).strip()
        if re.search(r"^[0-9]+\.?[0-9]*$", deposit):
            if deposit[0] == "0" and "." not in deposit:
                print("\nDeposit should not include any leading zeros")
                continue
            elif float(deposit) < 1:
                print("\nDeposit amount must be at least $1")
                continue
            elif float(deposit) > 1000000:
                print("\nDeposit exceeds maximum allowable amount")
                continue
            else:
                return round(float(deposit), 2)
        #This line of code for commas is new
        elif "," in deposit:
            return round(float(deposit.replace(",","")), 2)
        else:
            print("\nInvalid deposit amount: only digits and decimals allowed")
            continue


def bet(n):
    while True:
        stake = input("\nEnter stake amount: $ ")
        if re.search(r"^[0-9]+\.?[0-9]*$", stake):
            if stake[0] == "0" and "." not in stake:
                print("\nStake should not include any leading zeros")
                continue
            elif float(stake) <= n:
                return round(float(stake), 2)
            else:
                print("\nStake exceeds available balance")
                continue
         #This line of code for commas is new
        elif "," in stake:
            return round(float(stake.replace(",","")), 2)
        else:
            print("\nInvalid stake amount")
            continue


if __name__ == "__main__":
    main()

