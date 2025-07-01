# Python-project
# Casino Blackjack
#### Video Demo:  <(https://youtu.be/XmD-zMiMXgg)>
## Description

This project is based on the popular card game 'Blackjack'. Instead of writing code just for the game, I decided to add a twist in order to resemble playing at a casino. This just means that the player will have the option to bet money before each game. For Blackjack, the odds multiplier is 2.00, meaning that if a player bets $1.00 and wins, they will get back $2.00 (This includes their original $1 bet + $1 profit).

The rules of Blackjack are simple: the player and dealer both try to get a score as close to 21 as possible, without exceeding it. More specifically, the dealer will start by distributing two cards to the player and two cards to themselves (with one being facedown). The player will then have the option to 'hit' or 'stand'. When they choose 'hit' the dealer will give them another card, when they choose 'stand' it is the dealers job to draw cards in order to get a greater score than the player, without exceeding 21. In this scenario, the dealer will continue to draw cards for themselves until thay have exceeded the players score and reached a score of at least 17. A 'draw' occurs when both the player and dealer have a score greater than 21 or they both have a score equal to 21. The player wins if their score is greater than the dealer's score and at most 21 or if the dealer's score exceeds 21 and their score doesn't. The player loses if the dealers score is greater than their score and at most 21 or if their score exceeds 21 and the dealer's score doesnt. When the player gets a score of 21 it is called a 'Blackjack' because the worst case scenario is a draw. All cards are taken at face value except for Kings, Queens and Jacks which are worth 10 points and Ace's which are worth 1 point or 11 points depending on whether or not the Ace will cause a 'bust' (i.e., a score greater than 21). Those more familiar with Blackjack will recall the choice to "split" or "double down"; I did not include these options to make the game more beginner friendly.

Note that in the test_project.py file I utilize "monkeypatch" from pytest to test functions that call the built in input function.

### Functions

The program utilizes 5 functions, not including the main function. These functions are: game, hand_counter, option, deposit_money and bet.

- game

    The game function contains the bulk of the code for the program. The code for the actual game of blackjack is contained in this function. The function utilizes the online library 'card_deck' in order to instantiate and shuffle a deck using the libraries Deck class. The deck is a standard deck of 52 cards and saves us the time of writing a long list or dictionary. the deck itself is a list of 52 "cards"; each card contains a rank (i.e., value) and a suit (i.e., heart, club, spade or clover).
    > deck = Deck()

    > deck.shuffle()

    These lines of code instantiate and shuffle the deck object. Shuffling is important so the order of the cards is randomized, and follows no predicatble pattern.

    > player_hand = [f"|{deck[0]}|", f"|{deck[2]}|"]

    > dealer_hand = [f"|{deck[1]}|", f"|{deck[3]}|"]

    player_hand and dealer_hand are lists representing the cards that the dealer and player have. One can imagine the first card in the shuffled deck (0th index) being dealt to the player, the second being dealt to the dealer, the third to the player, and fourth to the dealer. I decided to use index along the deck for a sense of realism. In real Blackjack, cards are dealt from the front of the deck, they are not randomly chosen from the deck. However, the random module could have been used to achieve similar results.
    > deck[i]

    The above line of code thus represents the ith card in the shuffled deck. In player_hand and dealer_hand, cards can be added since they are lists. However, I chose to structure elements in this list using "| |" as borders to simulate the look of a real card.
    > dealer_count = hand_counter(dealer_hand)

    > player_count = hand_counter(player_hand)

    dealer_count and player_count represent the current score of the dealer/player. They utilize the hand_counter function which will be explained in more detail later.
    The game function starts by printing the dealers hand with their second card face down (as is done in Blackjack), as well as the players hand.
    > i = 4

    Setting i equal to 4 is important, because i represents the next card in the deck that is to be drawn after the dealer and player both receive their initial two cards.

    > decision = input("Select an option: hit/stand ").strip().lower()

    After the player see's their printed hand, they are prompted to hit or stand. Hitting adds the ith card to their hand which by default is the 5th card in the deck (not 4th - recall that lists are 0 indexed). After each decision to hit or stand, the player and dealers current hands are both printed. This simulates drawing cards in real life. However, the dealers facedown card is only revealed when it is their turn to begin drawing cards; that is, if the player stands, has a blackjack, or busts. Whenever a card is drawn from the deck the value of i is increased by one using i += 1. This ensures that cards are always drawn in order, and that there are no duplicates. The decision to hit is followed by multiple conditionals that describe certain scenarios that may occur, with each scenario resulting in a win, loss or draw for the player. These scenarios are based upon the rules previously described. The function returns either "WIN", "LOSS", or "DRAW", the only possible outcomes for any scenario within the game. The infinite loop started within the function ensures that the player can keep hitting until a result is achieved. This process must terminate since each card has a value of at least one. The player also has the option to stand, which will then lead the dealer to draw cards until they have won or until they bust. I decided to make the dealer "greedy" in the sense that they keep drawing cards until they win, not stopping at a draw.
    > dealer_hand.append(f"|{deck[i]}|")

    > i += 1

    > dealer_count = hand_counter(dealer_hand)

    Notice that these 3 lines of code are always executed together (the same is true for player_hand and player_count). The first line adds the ith card to the dealer_hand list which then allows it to be printed after every draw of a card. The second line uodates the value if i. The third line keeps track of the dealers score so that the program knows when to stop drawing cards (e.g., if the dealer beat the players score then they can stop drawing). I print many blank lines throughout this function and the code in general just because of stylistic taste, and to make the program output more visually appealing. The reader will notice that I constantly print the dealers hand and the players hand after any one of them draws a card. Those familiar with Blackjack will see this as the "pause" between the dealer drawing a card. Doing this as opposed to just printing the final hands takes alot more lines of code however, I prefer it stylistically.

- hand_counter

    The hand_counter function is self explanatory. It takes in a list; in particular, the players or dealers hand, and outputs their score. This is done by iterating through each element in the list and adding the card value to the variable "count". All cards with the exception of the 10s are strings of length 4; the 10s are strings of length 5 (e.g., '|10♣|'), which explains the notation:
    > i[1:3] == "10"

- option

    This function allows the user to make a decision to either start playing or to exit the program based on their input. This is a simple function that could have been excluded, but, I included it so that the main function could be as concise as possible.

- deposit_money

    In order for a player to acutally play, they must first deposit money, that is what this function is for (remember, this project is inspired by casino Blackjack). I decided to use regular expressions for this function instead of exceptions because I knew exactly how i wanted the user input to look, and I included an infinite loop to ensure that the user enters correctly. If the user gets to this function in main, but then decides they dont want to deposit anything anymore, they must still enter an amount, but, they can withdraw is right away soon after. I also included upper and lower bounds on the deposit amount, which is a common feature at most casinos.

- bet

    The bet function is similar to deposit_money as it too uses regular expressions. It takes in a parameter n, which is the account balance in the main function. Then it prompts the user to input a bet amount, ensuring that it doesnt exceed n.

- main

    > while True:

    >    balance = 0

    >   start = option()

    >  if start == "play":

    > balance = deposit_money()

    > while balance > 0:

    > while True:

    The reader will notice the main function begin with the above lines of code. The second loop ensures that once a player deposits money, they will be able to continue playing until their funds are gone. Of course, after each game, the player has the option to stop and withdraw their money, or keep playing. If the players balance drops to 0, then they will break out of the second loop and back into the first one, which will lead the program to prompt them to either play (i.e., deposit money again) or exit. I chose to structure the program this way with loops to get a more realistic experience, as opposed to just programming a single game. The frequent use of "\n" is a stylistic choice to make reading the output easier for the player.
