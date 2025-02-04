import random 
from card_ranking_checks import *

# ("Card", "Suit")
deck = [('2', 'H'), ('3', 'H'), ('4', 'H'), ('5', 'H'), ('6', 'H'), ('7', 'H'), ('8', 'H'), ('9', 'H'), ('T', 'H'), ('J', 'H'), ('Q', 'H'), ('K', 'H'), ('A', 'H'), 
        ('2', 'D'), ('3', 'D'), ('4', 'D'), ('5', 'D'), ('6', 'D'), ('7', 'D'), ('8', 'D'), ('9', 'D'), ('T', 'D'), ('J', 'D'), ('Q', 'D'), ('K', 'D'), ('A', 'D'), 
        ('2', 'S'), ('3', 'S'), ('4', 'S'), ('5', 'S'), ('6', 'S'), ('7', 'S'), ('8', 'S'), ('9', 'S'), ('T', 'S'), ('J', 'S'), ('Q', 'S'), ('K', 'S'), ('A', 'S'), 
        ('2', 'C'), ('3', 'C'), ('4', 'C'), ('5', 'C'), ('6', 'C'), ('7', 'C'), ('8', 'C'), ('9', 'C'), ('T', 'C'), ('J', 'C'), ('Q', 'C'), ('K', 'C'), ('A', 'C')]



hands = {
    # First 2 chars are card ranking
    # S means suited, O means offsuit

    "23S": {
        "Royal Flush" : 0,

        "Straight Flush" : {
            "Highest Card" : {}
        },

        "Four of a kind" : {
            "Highest card" : {}
        },

        "Full House" : {
            "Highest Card" : {} 
        },
        
        "Flush" : {
            "Highest Card" : {}
        },

        "Straight" :  {
            "Highest Card" : {}
        },
        
        "Three of a kind" : {
            "Highest Card" : {}
        },

        "Two pair" : {
            "Highest Card" : {}
        },
        
        "Pair" : {
            "Highest Card" : {}
        },

        "High Card" : {
            "Highest Card" : {}
        },

        "Highest kicker card" : 0   # Used if cards in hand  did not influence the hand ranking. 
    }
}


next_card_dictionary = {
    "A" : "2",
    "2" : "3",
    "3" : "4",
    "4" : "5",
    "6" : "7",
    "7" : "8",
    "8" : "9",
    "9" : "T",
    "T" : "J",
    "J" : "Q",
    "Q" : "K",
    "K" : "A"
}





if __name__ == '__main__':
    royal_flush = ('T', 'H'), ('J', 'H'), ('D', 'H'), ('K', 'H'), ('A', 'H')
    royal_flush = sorted(royal_flush)
    print(royal_flush)
    print(has_four_of_a_kind(royal_flush))