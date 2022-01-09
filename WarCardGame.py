from random import shuffle

values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}
suits=["Hearts","Diamonds","Spades","Clubs"]

class Card():
    def __init__(self,suit,rank):
        '''Creates a Card Object and assigns a suit,rank and value from the values dictionary'''
        self.rank=rank
        self.suit=suit
        self.value=values[rank]
    
    def __str__(self):
        return self.rank +" of "+ self.suit

class Deck():

    # DeckList=[] both here and in init work
    def __init__(self):
        '''Creates all 52 cards of a deck and stores it in the DeckList attribute'''
        self.DeckList=[]
        for x in suits:
            for y in values:
                self.DeckList.append(Card(x,y))

    def shuffledeck(self):
        '''Shuffles Decklist using random.shuffle()'''
        shuffle(self.DeckList)
        print("Shuffle Successful.")
    
    def deal(self,n,player_hand):
        '''Deals n cards as a list to the list player_hand'''
        for x in range(n):
            player_hand.append(self.DeckList.pop())

class Player():

    def __init__(self,name,hand=[]):
        '''Name as Player's name and Hand as the dealed list of cards from Deck.deal()'''
        self.hand=hand
        self.name=name
#play,add,add mulitple
    def __str__(self):
        return "Player {} has {} number of cards".format(self.name,len(self.hand))
    
    def play(self):
        '''Playing one card on the table
           Note: The Card is played (popped) from the top of the hand'''
        return self.hand.pop(0)
    
    def add(self,new_card):
        '''Adding a newly acquired card to the Player's hand
           Note: Adds Card to the bottom of the hand'''
        self.hand.append(new_card)
    
    def add_multiple(self,new_cards_list):
        '''Adding a newly acquired set of cards (from a war situation) to the Player's hand'''
        self.hand.extend(new_cards_list)

# Test code
# new_player=Player("John")
# print(new_player)
# testy=Card("Hearts","Ten")
# print(testy,testy.value,testy.suit)
# decktest=Deck()
# print(len(decktest.DeckList))
# decktest.shuffledeck()
# print(len(decktest.DeckList))
# player1deckk=[]
# player2deckk=[]
# decktest.deal(player1deckk,player2deckk)
# print(len(decktest.DeckList))
# print(len(player1deckk))
# print(len(player2deckk))
# print(player1deckk,player2deckk)
# for card_object in decktest.DeckList:
#     print(card_object)


