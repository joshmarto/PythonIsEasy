#POKER
from random import shuffle
from os import system

def createDeck():
    Deck = []

    suitsValues = ["Clubs", "Diamonds", "Hearts", "Spades"]
    for suit in suitsValues:
        for value in range(1, 14):
            if value == 1:
                value = 14
                face = "A"
            elif value == 11:
                value = 11
                face = "J"
            elif value == 12:
                value = 12
                face = "Q"
            elif value == 13:
                value = 13
                face = "K"
            else:
                face = value
            card = Card(suit, face, value)
            Deck.append(card)
    shuffle(Deck)
    return Deck

class Player:
    def __init__(self, name, hand, money=100):
        self.name = name
        self.hand = hand
        self.money = money
        self.bet = 0
        self.active = True
    
    def Pass(self, yes):
        if yes == True:
            pass

    def Bet(self, amount):
        self.bet = amount
        self.money -= amount

    def notGo(self):
        self.active = False

    def Equal(self, amount):
        self.bet += amount - self.bet

    def Up(self, amount):
        self.bet = amount

    def Turn(self):
        print(f"It's {self.name}'s turn")

    def __str__(self):
        return (f"{self.name} has {self.score} points and {self.money} money")

class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __str__(self):
        return (f"{self.face} {self.suit}")

def printDeck(deck):
    for i in range(len(deck)):
        if i != len(deck) - 1:
            print(deck[i], end=" ")
        else:
            print(deck[i])

def flush(player):
    suits = [card.suit for card in player.hand]
    if len(set(suits)) == 1:
      return True
    return False

def straight(player):
    values = [card.value for card in player.hand]
    values.sort()
    if not len( set(values)) == 5:
      return False 
    if values[4] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
      return 5
    else:
      if not values[0] + 1 == values[1]: return False 
      if not values[1] + 1 == values[2]: return False
      if not values[2] + 1 == values[3]: return False
      if not values[3] + 1 == values[4]: return False
    return values[4]

def highCard(player):
    values = [card.value for card in player.hand]
    highCard = None
    for card in player.hand:
      if highCard is None:
        highCard = card
      elif highCard.value < card.value: 
        highCard=card
    return highCard

def highestCount(player):
    count = 0
    values = [card.value for card in player.hand]
    for value in values:
      if values.count(value) > count:
        count = values.count(value)
    return count

def pairs(player):
    pairs = []
    values = [card.value for card in player.hand]
    for value in values:
      if values.count(value) == 2 and value not in pairs:
        pairs.append(value)
    return pairs
        
def fourKind(player):
    values = [card.value for card in player.hand]
    for value in values:
      if values.count(value) == 4:
        return True

def fullHouse(player):
    two = False
    three = False
    values = [card.value for card in player.hand]
    if values.count(values) == 2:
      two = True
    elif values.count(values) == 3:
      three = True
    if two and three:
      return True
    return False

def Win(player1, player2):
    if flush(player1) or straight(player1) or highCard(player1) or highestCount(player1) or pairs(player1) or fourKind(player1) or fullHouse(player1):
        print(f"{player1.name} wins!")
    elif flush(player2) or straight(player2) or highCard(player2) or highestCount(player2) or pairs(player2) or fourKind(player2) or fullHouse(player2):
        print(f"{player2.name} wins!")

def playerHand(player):
    print(f"{player.name} this is your hand", end=" ")
    for i in range(len(player.hand)):
        if i != len(player.hand) - 1:
            print(player.hand[i], end=" ")
        else:
            print(player.hand[i])

def Game(player1, player2, deck):
    while (True):
        if len(deck) < 32:
            deck = createDeck()
            firstHand = [deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop()]
            player1 = Player("Bob", firstHand)
            secondHand = [deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop()]
            player2 = Player("Peter", secondHand)            
        playerHand(player1)
        play = input(f"{player1.name} do you want to play or pass \n(Type 'play' or 'pass')\n")
        if play == "play":
            bet1 = int(input(f"Enter your bet {player1.name} "))
            player1.Bet(bet1)
            playerHand(player2)
            op = input(f"{player2.name} do you want to 'equal' or 'up'?")
            if op == "equal":
                player2.Equal(bet1)
                Win(player1, player2)
                break
            elif op == "up":
                bet2 = int(input(f"Enter your bet {player2.name} "))
                player2.Up(bet2)
                Win(player1, player2)
                break
            else:
                print("403: Forbbiden")
        elif play == "pass":
            play = input(f"{player2.name} do you want to play or pass \n(Type 'play' or 'pass')\n")
            if play == "play":
                print(f"Congrats {player2.name}, you win!")
            elif play == "pass":
                Win(player1, player2)
                break
            else:
                print("403: Forbbiden")
        else:
            print("403: Forbidden")


cardDeck = createDeck()
name1 = input("Player 1, enter your name ")
name2 = input("Player 2, enter your name ")
firstHand = [cardDeck.pop(), cardDeck.pop(), cardDeck.pop(), cardDeck.pop(), cardDeck.pop()]
player1 = Player(name1, firstHand)
secondHand = [cardDeck.pop(), cardDeck.pop(), cardDeck.pop(), cardDeck.pop(), cardDeck.pop()]
player2 = Player(name2, secondHand)
Game(player1, player2, cardDeck)
