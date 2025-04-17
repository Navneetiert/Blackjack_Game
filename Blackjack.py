'''
1.storing all suits of cards inside tuple
2.storing all possible rank inside ranks tuple
3.stroing digit for correct corresponding rank inside values tuple
'''
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card():
    '''
    0.defining Card class to create card obejct with 
    their suit and rank
    1.defing str for print statement
    '''
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return (self.rank + " of "+ self.suit)


class Deck():
    '''
    0.defining Derk class to create all cards and tie them 
    inside list all_cards with their corresponding value
    defining in Card class.
    1.defined method for shuffle all cards in all_cards lst to 
    select a random card.
    2.defined method for removing the single card from list of 
    all cards from last.
    '''
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle_all_cards(self):
        random.shuffle(self.all_cards)


    def deal_one(self):
        return self.all_cards.pop()


class Player():
    '''
    0.defining Player class containing the name and empty list of all_cards intially.
    1.defining the method for removing the first card from the beginning from list.
    2.defining the method for adding the single or mutliple cards to all_cards list.
    3.defing the method for printing the value
    '''
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        self.all_cards.pop(0)

    def add_cards(self,new_cards):
        # if more than one cards to add
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        # only one card to add
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards'
    


#GAME SETUP
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_all_cards()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#Play the Game: 
game_on = True
#while game on 
round_num = 0
while game_on:
    round_num +=1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Player One,out of cards, Player Two wins!!")
        game_on=False
        break

    if len(player_two.all_cards) == 0:
        print("Player Two,out of cards, Player One Wins!!")
        game_on=False
        break

    #START A NEW ROUND
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())    


    #while at_war
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        
        else:
            print("War!!")
            if len(player_one.all_cards0)< 5:
                print("Player One unable to declare war")
                print("Player Two Wins!")
                game_on = False
                break

            elif len(player_one.all_cards0)< 5:
                print("Player Two unable to declare war")
                print("Player One Wins!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one.add_cards.append(player_one.remove_one())
                    player_two.add_cards.append(player_two.remove_one())
