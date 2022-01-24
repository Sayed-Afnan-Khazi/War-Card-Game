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
    
    def add(self,new_cards_list):
        '''Adding a newly acquired (set of) card(s) to the Player's hand
           Works for both a single card or a set of cards'''
        if type(new_cards_list)==type([]):
            self.hand.extend(new_cards_list)
        else:
            self.hand.append(new_cards_list)

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
    
    # Checking if either player has lost
    
    if len(Player1.hand)==0:
        print(f"{Player2.name} wins!")
        break
    elif len(Player2.hand)==0:
        print(f"{Player1.name} wins!")
        break

    round_number+=1
    print(f"Round number: {round_number}")

    player1_played_cards=[]
    player2_played_cards=[]

    player1_played_cards.append(Player1.play())
    player2_played_cards.append(Player2.play())
    
    # Considering War has already occurred, if it hasn't then we break

    at_war=True

    while at_war:


        if player1_played_cards[-1].value > player2_played_cards[-1].value: 
            Player1.add(player1_played_cards)
            Player1.add(player2_played_cards)

            # War didn't happen
            break

        elif player1_played_cards[-1].value < player2_played_cards[-1].value:
            Player2.add(player1_played_cards)
            Player2.add(player2_played_cards) 

            # War didn't happen
            break

        else:
            print("WAR!")

            if len(Player1.hand)<5:
                print(f"{Player1.name} unable to start a war, {Player2.name} wins!")
                game_on=False
                break
            elif len(Player2.hand)<5:
                print(f"{Player2.name} unable to start a war, {Player1.name} wins!")
                game_on=False
                break
            else:
                for x in range(5):
                    player1_played_cards.append(Player1.play())
                    player2_played_cards.append(Player2.play())
                continue # Not needed

# -Game - End -

