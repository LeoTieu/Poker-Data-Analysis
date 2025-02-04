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

def has_ace(hand: list):
    return any(rank == "A" for rank, suit in hand)


def has_flush(hand: list):
    suit = hand[0][1]
    for card in hand:
        card_suit = card[1]
        if suit != card_suit:
            return False
    return True

def has_straight(hand: list):
    counter = 0
    for card in hand:
        card_ranking = card[0]
        if any(rank == next_card_dictionary[card_ranking] for rank, suit in hand):
            continue
        counter += 1
    return True if counter == 1 else False


def has_four_of_a_kind(hand: list):
    for index, card in enumerate(hand):
        counter = 1
        print(card)
        current_card_ranking = card[0]
        for index_2, card_2 in enumerate(hand):
            if index == index_2:
                continue
            if current_card_ranking == card_2:
                counter += 1
        
        if counter == 4:
            return True
    return False
        
if __name__ == '__main__':
    poker_hand_examples = {
    "Royal Flush": [
        [('T', 'H'), ('J', 'H'), ('Q', 'H'), ('K', 'H'), ('A', 'H')],
        [('T', 'D'), ('J', 'D'), ('Q', 'D'), ('K', 'D'), ('A', 'D')],
    ],
    "Straight Flush": [
        [('5', 'S'), ('6', 'S'), ('7', 'S'), ('8', 'S'), ('9', 'S')],
        [('2', 'C'), ('3', 'C'), ('4', 'C'), ('5', 'C'), ('6', 'C')],
    ],
    "Four of a Kind": [
        [('A', 'H'), ('A', 'D'), ('A', 'S'), ('A', 'C'), ('K', 'H')],
        [('7', 'S'), ('7', 'D'), ('7', 'C'), ('7', 'H'), ('3', 'D')],
    ],
    "Full House": [
        [('Q', 'H'), ('Q', 'D'), ('Q', 'S'), ('J', 'H'), ('J', 'D')],
        [('8', 'C'), ('8', 'S'), ('8', 'D'), ('2', 'H'), ('2', 'C')],
    ],
    "Flush": [
        [('2', 'H'), ('6', 'H'), ('9', 'H'), ('J', 'H'), ('K', 'H')],
        [('4', 'S'), ('7', 'S'), ('8', 'S'), ('T', 'S'), ('Q', 'S')],
    ],
    "Straight": [
        [('4', 'C'), ('5', 'D'), ('6', 'S'), ('7', 'H'), ('8', 'C')],
        [('T', 'C'), ('J', 'D'), ('Q', 'S'), ('K', 'D'), ('A', 'H')],
    ],
    "Three of a Kind": [
        [('9', 'H'), ('9', 'D'), ('9', 'S'), ('J', 'C'), ('K', 'D')],
        [('5', 'S'), ('5', 'D'), ('5', 'C'), ('8', 'H'), ('Q', 'H')],
    ],
    "Two Pair": [
        [('J', 'H'), ('J', 'C'), ('8', 'S'), ('8', 'D'), ('K', 'H')],
        [('4', 'D'), ('4', 'S'), ('7', 'C'), ('7', 'H'), ('A', 'C')],
    ],
    "Pair": [
        [('6', 'H'), ('6', 'C'), ('9', 'D'), ('J', 'S'), ('A', 'H')],
        [('T', 'S'), ('T', 'D'), ('5', 'H'), ('7', 'C'), ('Q', 'D')],
    ],
    "High Card": [
        [('2', 'H'), ('5', 'D'), ('8', 'S'), ('J', 'C'), ('K', 'H')],
        [('3', 'C'), ('6', 'S'), ('9', 'D'), ('T', 'H'), ('A', 'S')],
    ],
}

