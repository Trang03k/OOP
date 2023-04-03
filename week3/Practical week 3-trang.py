
# Please use the following starting code.
# TODO complete the following classes...

import random
class Card:
    def __init__(self, suit, value_str):
        self.__suit = suit
        self.__value_str = value_str

    
    def get_suit(self):
        return self.__suit
    
    def getValueStr(self):
        return self.__value_str
    
    def getValue(self):
        if self.__value_str =='ace':
            return 1
        elif self.__value_str in ['jack','queen','king']:
            return 10
        else:
            return int(self.__value_str)
        

    def toString(self):
        return f'{self.__value_str} of {self.__suit}'




class Deck:
    

    def __init__(self):
        self.__cards = []
        self.reset()

    def reset(self):
        self.__cards =[]
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        values = ['ace', '2', '3', '4', '5', '6', '7', '8', 
                    '9', '10', 'jack', 'queen', 'king']
        
        for suit in suits:
            for value in values:
                self.__cards.append(Card(suit,value))
        
    def shuffle(self):
        random.shuffle(self.__cards)

    def drawCard(self):
        if not self.__cards:
            return None
        else:
            return self.__cards.pop(0)
    
class Hand:
    def __init__(self):
        self.__cards =[]
    
    def addToHand(self,Card):
        if len(self.__cards) < 5:
            self.__cards.append(Card)
        else:
            print('Error')
        
    def getHandValue(self):
        value = 0
        for card in self.__cards:
            value += card.getValue()
        return value
    
    def emptyHand(self):
        self.__cards = []

    def showCards(self):
        for num, card in enumerate(self.__cards):
            print(card.toString(), end='')
            if num < len(self.__cards) - 1:
                print(', ', end='')
        print()

        




# Test/Create objects
c1 = Card('hearts', 'ace')
print(c1.toString(), 'is worth', c1.getValue())
c2 = Card('spades', 'jack')
print(c2.toString(), 'is worth', c2.getValue())


deck = Deck()
print(deck.drawCard().toString())
deck.shuffle()
c3 = deck.drawCard()
print(c3.toString(), 'is worth', c3.getValue())
deck.reset()



myCards = Hand()
myCards.addToHand(deck.drawCard())
myCards.addToHand(deck.drawCard())
myCards.showCards()
print(myCards.getHandValue())
myCards.emptyHand()
print(myCards.getHandValue())