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

    def __init__(self,name):
        self.name = name
        self.all_cards =[]

    def remove_one(self):
        return self.all_cards.pop(0) # remove the first/ top card

    def add_cards(self,new_cards):
        if type(new_cards) == type([]): # list of multiple cards obj
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards) # for single card

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."


new_player = Player("Atsuki")
print(new_player) # this is the test for player class


