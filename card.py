import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
        self.values = values[ranks]

    def __str__(self):
        return self.ranks + ' of ' + self.suits


class Deck:
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)  # remove the first/ top card

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):  # list of multiple cards obj
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)  # for single card

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


# new_player = Player("A")
# print(new_player) # this is the test for player class


# game setup

player1 = Player("1")
player2 = Player("2")

new_deck = Deck()
new_deck.shuffle_deck()

# split cards

for x in range(26):  # 52 / 2
    player1.all_cards(new_deck.deal_one())
    player2.all_cards(new_deck.deal_one())

game_is_on = True

round_num = 0

while game_is_on:
    round_num += 1
    print(f"Round {round_num}")

    # check number of cards player 1 has
    if len(player1.all_cards) == 0:
        print(f"Player1, out of cards! Player 2 Wins.")
        game_is_on = False
        break

    if len(player2.all_cards) == 0:
        print(f"Player2, out of cards! Player 1 Wins.")
        game_is_on = False
        break

    # start new round from here

    player1_one_cards = []
    player1_one_cards.append(player1.remove_one())

    player2_two_cards = []
    player2_two_cards.append(player2.remove_one())

    # loop war condition since it could be happening more than one war in the game

    at_war = True

    # three condition
    # 1. player one > player two
    # 2. add cards to player one
    # 3 at war = False

    # 1. player two > player two
    # 2. add cards to player two
    # 3 at war = False

    # 1. player one == player two
    # 2. check if player has enough card to continue playing
    # 3  draw additinoal cards
    # 4 loop to first step
    while at_war:
        if player1_one_cards[-1].value > player2_two_cards[-1].value:
            # Player One gets the cards
            player1_one_cards.add_cards(player1_one_cards)
            player1_one_cards.add_cards(player2_two_cards)

            # No Longer at "war" , time for next round
            at_war = False

            # Player Two Has higher Card
        elif player1_one_cards[-1].value < player2_two_cards[-1].value:

            # Player Two gets the cards
            player2_two_cards.add_cards(player1_one_cards)
            player2_two_cards.add_cards(player2_two_cards)

            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.

            # First check to see if player has enough cards

            # Check to see if a player is out of cards:
            if len(player1_one_cards.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player1_one_cards.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player1_one_cards.append(player1_one_cards.remove_one())
                    player2_two_cards.append(player2_two_cards.remove_one())
