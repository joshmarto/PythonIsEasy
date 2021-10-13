#BLACKJACK
from random import shuffle


def createDeck():
    Deck = []

    faceValues = ["A", "J", "Q", "K"]
    for i in range(4): #There are 4 different suits
        for card in range(2, 11): #Adding the numbers 2 - 10
            Deck.append(card)
        for card in faceValues:
            Deck.append(card)
    shuffle(Deck)
    return Deck

class Player:
    def __init__(self, hand=[], money=100):
        self.hand = hand
        self.score = self.setScore()
        self.money = money
        self.bet = 0

    def __str__(self):
        currentHand = "hand: "
        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus = currentHand + " score: " + str(self.score)
        return finalStatus

    def setScore(self):
        self.score = 0
        faceCardsDict = {"A": 11, "J": 10, "Q": 10, "K": 10,
                         2: 2, 3: 3, 4: 4, 5: 5, 6: 6,
                         7: 7, 8: 8, 9: 9, 10:10}
        aceCounter = 0
        for card in self.hand:
            self.score += faceCardsDict[card]
            if card == "A":
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1
        return self.score

    def hit(self, card):
        self.hand.append(card)
        self.score = self.setScore()

    def play(self, newHand):
        self.hand = newHand
        self.score = self.setScore()

    def betMoney(self, amount):
        self.money -= amount
        self.bet += amount

    def draw(self):
        self.money += self.bet
        self.bet = 0

    def win(self, result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += int(2.5 * self.bet)
            else:
                self.money += 2 * self.bet
            self.bet = 0
        else:
            self.bet = 0

    def hasBlackjack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False

def printHouse(house):
    print("House hand", end=" ")
    for card in range(len(house.hand)):
        if card == 0:
            print("X", end=" ")
        elif card == len(house.hand) - 1:
            print(f"{house.hand[card]}")
        else:
            print(house.hand[card], end=" ")

""" TESTS
player1 = Player([3, 7, 5])
print(player1)
player1.hit("A")
print(player1)
player1.betMoney(20)
print(player1.money, player1.bet)
player1.win(True)
print(player1.money, player1.bet)
player1.play(["A", "K"])
print(player1)
player1.betMoney(20)
player1.win(True)
print(player1.money, player1.bet) """

cardDeck = createDeck()
#print(cardDeck)
firstHand = [cardDeck.pop(), cardDeck.pop()]
secondHand = [cardDeck.pop(), cardDeck.pop()]
player1 = Player(firstHand)
house = Player(secondHand)
cardDeck = createDeck()

while (True):
    if len(cardDeck) < 20:
        cardDeck = createDeck()
    firstHand = [cardDeck.pop(), cardDeck.pop()]
    secondHand = [cardDeck.pop(), cardDeck.pop()]
    player1.play(firstHand)
    house.play(secondHand)
    Bet = int(input("Please enter your bet: "))
    player1.betMoney(Bet)
    print(f"Player {player1}")
    printHouse(house)
    if player1.hasBlackjack():
        if house.hasBlackjack():
            player1.draw()
        else:
            player1.win(True)
    else:
        while (player1.score < 21):
            action = input("Do you want another card?(y/n): ")
            if action == "y":
                player1.hit(cardDeck.pop())
                print(f"Player {player1}")
                printHouse(house)
            else:
                break
        while (house.score < 16):
            printHouse(house)
            house.hit(cardDeck.pop())
        if player1.score > 21:
            if house.score > 21:
                player1.draw()
            else:
                player1.win(False)
        elif player1.score > house.score:
            player1.win(True)
        elif player1.score == house.score:
            player1.draw()
        else:
            if house.score > 21:
                player1.win(True)
            else:
                house.win(True)
    print(f"Player {player1}")
    print(f"House {house}")
    print(f"Player's money {player1.money}")
