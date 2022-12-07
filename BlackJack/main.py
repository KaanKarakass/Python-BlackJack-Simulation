
import random
class Card:
    def __init__(self, suits, cards, values):
        #spades...
        self.suits = suits

        # A, K...
        self.cards = cards

        # Score Value A:11
        self.values = values
def print_card(player, player_score, control):
    i = 0
    if control == 0:
        while i != len(player):
            print(player[i].suits, player[i].cards, end=" ,")
            i += 1
        print("      Point :", player_score)
    else:
        print(player[0].suits, player[0].cards, ", Hidden", end=" ,")
        print("      Point : ", "Hidden +", player[0].values)
def create_card():
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    Deck1 = []
    total = 4
    for i in suits:
        for suit in suits:
            for card in cards:
                Deck1.append(Card(suit, card, values[card]))
    return Deck1


def blackjack(Deck):

    control = False  # if there is not card, it will be True


    total_round = 0
    player1_win = 0
    player2_win = 0

    player1 = []
    player2 = []
    dealer = []

    while len(Deck) > 0:

        player1_score = 0
        player2_score = 0
        dealer_score = 0

        # first time
        while len(player1) < 2 and len(player2) < 2:
            # for player 1 card
            try:
                choice = random.choice(Deck)
            except:
                control = True
                break
            player1.append(choice)
            Deck.remove(choice)

            # for player 2 card
            try:
                choice1 = random.choice(Deck)
            except:
                control =True
                break
            player2.append(choice1)
            Deck.remove(choice1)

            # for dealer cards
            try:
                choice2 = random.choice(Deck)
            except:
                control = True
                break
            dealer.append(choice2)
            Deck.remove(choice2)
            #define players and dealer scores
            player1_score += choice.values
            player2_score += choice1.values
            dealer_score += choice2.values

            #if player or dealer has 2 A card, One of the A card equals as 1 point
            if len(player1) == 2 and len(player2) == 2 and len(dealer) == 2:
                if player1[0].values == 11 and player1[1].values == 11: #for player 1
                    player1[1].values = 1
                    player1_score -= 10
                if player2[0].values == 11 and player2[1].values == 11: #for player 2
                    player2[1].values = 1
                    player2_score -= 10
                if dealer[0].values == 11 and dealer[1].values == 11: #for dealer
                    dealer[1].values = 1
                    dealer_score -= 10
        #if there is not any card
        if control == True:
            break
        # print players cards and points
        print("Player1 Cards:", end=" ")
        print_card(player1, player1_score, 0)

        print("Player2 Cards: ", end=" ")
        print_card(player2, player2_score, 0)
        print("Dealer Cards: ", end=" ")
        print_card(dealer, dealer_score, 1)

        #automatic card take
        while player1_score <= 16:
            # player1 takes card
            try:
                choice = random.choice(Deck)
            except:
                control = True
                break
            player1.append(choice)
            Deck.remove(choice)
            # score calculate
            player1_score += choice.values
        if control == True:
            break
        #print cards
        print("Player1 Cards:", end=" ")
        print_card(player1, player1_score, 0)

        while player2_score <= 16:
            # player2 takes card
            try:
                choice1 = random.choice(Deck)
            except:
                control = True
                break
            player2.append(choice1)
            Deck.remove(choice1)
            # score calculate
            player2_score += choice1.values
        if control == True:
            break
        # print cards
        print("Player2 Cards:", end=" ")
        print_card(player2, player2_score, 0)

        # after players don't want to take card, dealer show hidden card and if card score smaller than 17, takes card.
        while dealer_score < 17:
            #dealer takes card
            try:
                choice2 = random.choice(Deck)
            except:
                control = True
                break
            dealer.append(choice2)
            Deck.remove(choice2)
            # score calculate
            dealer_score += choice2.values
        if control == True:
            break
        print("Dealer Cards:", end=" ")
        print_card(dealer, dealer_score, 0)
        print("\t")

        #compare card_scores
        #for player 1
        if player1_score > 21:
            print("Player 1 Lose")
        elif player1_score == 21 or dealer_score > 21 or player1_score > dealer_score:
            print("Player 1 Won")
            player1_win += 1
        elif player1_score < dealer_score and dealer_score < 22:
            print("Player 1 Lose")
        else:
            if len(player1) < len(dealer): #Scoreless, (Tie-Break)
                print("Player 1 Won")
                player1_win += 1
            else:
                print("Player 1 Lose")

        #for player 2
        if player2_score > 21:
            print("Player 2 Lose")
        elif player2_score == 21 or dealer_score > 21 or player2_score > dealer_score:
            print("Player 2 Won")
            player2_win += 1
        elif player2_score < dealer_score and dealer_score < 22:
            print("Player 2 Lose")
        else:
            if len(player2) < len(dealer):  # Scoreless, (Tie-Break)
                print("Player 2 Won")
                player2_win += 1
            else:
                print("Player 2 Lose")

        total_round += 1

        # print current scores and played round
        print("Played Round :", total_round, "    Player1 current score :", player1_win,
                "    Player2 current score :", player2_win)
        print("******************************************************")
        print("\t")

        player1.clear()
        player2.clear()
        dealer.clear()
    print("Game Over Because Dest is empty")
    print("Score Table")
    if player1_win > player2_win:
        print("Player1 :", player1_win)
        print("Player2 :", player2_win)
    else:
        print("Player2 :", player2_win)
        print("Player1 :", player1_win)
if __name__ == '__main__':
    Deck = create_card()
    blackjack(Deck)


