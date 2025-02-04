next_card_dictionary = {
    "A" : "2",
    "2" : "3",
    "3" : "4",
    "4" : "5",
    "5" : "6",
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

def has_four_of_a_kind(hand: list):
    for index, card in enumerate(hand):
        counter = 1
        current_card_ranking = card[0]
        for index_2, card_2 in enumerate(hand):
            if index == index_2:
                continue
            if current_card_ranking == card_2[0]:
                counter += 1
        if counter == 4:
            return True
    return False

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

def has_three_of_a_kind(hand: list):
    for index, card in enumerate(hand):
        counter = 1
        current_card_ranking = card[0]
        for index_2, card_2 in enumerate(hand):
            if index == index_2:
                continue
            if current_card_ranking == card_2[0]:
                counter += 1
        if counter == 3:
            return True
    return False

def has_two_pair(hand: list):
    for index, card in enumerate(hand):
        current_pairs = set()
        counter = 1
        current_card_ranking = card[0]
        for index_2, card_2 in enumerate(hand):
            if index == index_2:
                continue
            if current_card_ranking == card_2[0]:
                counter += 1
        if counter == 2:
            current_pairs.add(current_card_ranking)
    return True if len(current_pairs) == 2 else False


def has_pair(hand: list):
    for index, card in enumerate(hand):
        counter = 1
        current_card_ranking = card[0]
        for index_2, card_2 in enumerate(hand):
            if index == index_2:
                continue
            if current_card_ranking == card_2[0]:
                counter += 1
        if counter == 2:
            return True
    return False
