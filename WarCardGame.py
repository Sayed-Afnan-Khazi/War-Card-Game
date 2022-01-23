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
    
    def deal(self,n):
        '''Deals and returns n cards as a list'''
        player_hand=[]
        for x in range(n):
            player_hand.append(self.DeckList.pop())
        return player_hand

class Player():

    def __init__(self,name,hand=[]):
        '''Name as Player's name and Hand as the dealed list of cards from Deck.deal()'''
        self.hand=hand
        self.name=name

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

# -Game-Logic-

# Creating and Shuffling the deck

new_deck=Deck()
new_deck.shuffledeck()

# Creating the players and dealing cards to them

Player1=Player(input("Enter Player 1's name:"),new_deck.deal(26))
Player2=Player(input("Enter Player 2's name:"),new_deck.deal(26))

# -Game - Start-

game_on=True
round_number=0

while game_on:
    
    # Status Update on the game

    # print(f"{Player1.name} has {len(Player1.hand)} number of cards.")
    # print(f"{Player2.name} has {len(Player2.hand)} number of cards.")

    # Checking if either player has lost
    
    if len(Player1.hand)==0:
        print(f"{Player2.name} wins!")
        break
    elif len(Player2.hand)==0:
        print(f"{Player1.name} wins!")
        break

    round_number+=1
    print(f"Round number: {round_number}")

    # Players play cards

    played_cards=[Player1.play(),Player2.play()]
    # print(f"{Player1.name} played:")
    # print(played_cards[0])
    # print(f"\n {Player2.name} played:")
    # print(played_cards[1])
    # input("Press Enter to continue...")
    
    # Checking for War condition

    if played_cards[0].value == played_cards[1].value:

        print("Tie! War has begun.")
        # input("Press Enter to continue...")

        # Checking if players have enough cards to start a war

        if len(Player1.hand)<=7:
            print(f"{Player1.name} Didn't have enough cards to start a war. \n {Player2.name} wins!")
            break
        if len(Player2.hand)<=7:
            print(f"{Player2.name} Didn't have enough cards to start a war. \n {Player1.name} wins!")
            break
        at_war=True
        adding_cards=[]
        adding_cards.extend(played_cards)

        while at_war: 

            # Players play cards

            player1_played_cards=[]
            player2_played_cards=[]
            for x in range(5):
                player1_played_cards.append(Player1.play())
                player2_played_cards.append(Player2.play())

            # print(f"{Player1.name} played:")
            # print(played_cards[0])
            # print(f"\n {Player2.name} played:")
            # print(played_cards[1])

            # Checking for Repeated War Condition

            if player1_played_cards[-1].value == player2_played_cards[-1].value:
                # print("Tie again. Play another set of cards.")
                continue
            elif player1_played_cards[-1].value > player2_played_cards[-1].value:
                # print(adding_cards) #Debugging
                Player1.add_multiple(adding_cards)
                # print(f"{Player1.name} won this war! \n A total of {len(adding_cards)} cards have been added to their deck.")
                # input("Press Enter to continue...")
                break
            elif played_cards[0].value < played_cards[1].value:
                # print(adding_cards) #Debugging
                Player2.add_multiple(adding_cards)
                # print(f"{Player2.name} won this war! \n A total of {len(adding_cards)} cards have been added to their deck.")
                # input("Press Enter to continue...")
                break

    elif played_cards[0].value > played_cards[1].value:
        # print(played_cards) #Debugging
        Player1.add_multiple(played_cards)
        # print(f"{Player1.name} won this round! \n The",played_cards[1], "have been added to their deck.")
        # input("Press Enter to continue...")
        continue

    elif played_cards[0].value < played_cards[1].value:
        # print(played_cards) #Debugging
        Player2.add_multiple(played_cards)
        # print(f"{Player2.name} won this round! \n The", played_cards[0], "have been added to their deck.")
        # input("Press Enter to continue...")
        continue


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


