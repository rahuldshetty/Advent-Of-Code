'''Day 7 Problem'''
from collections import defaultdict
from enum import Enum

class HandType(Enum):
    '''
    Type of card in hand
    '''
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7

CARD_RANK = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "J": 4,
    "T": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13,
}

EXAMPLE_FILE = "example.txt"
INPUT_FILE = "input.txt"

def read_input(file):
    '''read input from file'''
    with open(file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
        cards = []
        for line in lines:
            hand, bid = line.split()
            cards.append({
                "bid": int(bid),
                "hand": hand
            })
        return cards

def check_type(hand):
    '''
    Find what type of card is it
    '''
    count_elements = defaultdict(int)
    for symbol in hand:
        count_elements[symbol] += 1

    values = tuple(sorted(count_elements.values()))

    if values == (5,):
        # here all five cards have the same label: AAAAA
        return HandType.FIVE_OF_A_KIND

    elif values == (1, 4):
        # where four cards have the same label and one card has a different label: AA8AA
        return HandType.FOUR_OF_A_KIND

    elif values == (2, 3):
        # where three cards have the same label, and the 
        # remaining two cards share a different label: 23332
        return HandType.FULL_HOUSE

    elif values == (1, 1, 3):
        # where three cards have the same label, and the remaining two cards are 
        # each different from any other card in the hand: TTT98
        return HandType.THREE_OF_A_KIND

    elif values == (1, 2, 2):
        # where two cards share one label, two other cards share a second label, 
        # and the remaining card has a third label: 23432
        return HandType.TWO_PAIR

    elif values == (1, 1, 1, 2):
        # where two cards share one label, and the other three cards 
        # have a different label from the pair and each other: A23A4
        return HandType.ONE_PAIR

    # where all cards' labels are distinct: 23456
    return HandType.HIGH_CARD

def sort_by_rank_and_order(card):
    '''
    Logic to sort hand cards array
    '''
    hand_type = check_type(card['hand'])
    rank_order = [hand_type.value, ]

    # Add number values from card
    for c in card['hand']:
        rank_order.append(CARD_RANK[c])

    return tuple(rank_order)

def part1(file):
    '''Solution for part 1 of the problem'''
    cards = read_input(file)
    sorted_cards = sorted(cards, key=sort_by_rank_and_order, reverse=True)
    ans = 0
    for i in range(len(cards)):
        ans += sorted_cards[i]['bid'] * (i + 1)
    return ans

################################################################
################################################################
MODIFIED_CARD_RANK = {
    "A": 1,
    "K": 2,
    "Q": 3,
    "T": 5,
    "9": 6,
    "8": 7,
    "7": 8,
    "6": 9,
    "5": 10,
    "4": 11,
    "3": 12,
    "2": 13,
    "J": 14,
}

def modified_check_type(hand):
    '''
    Find what type of card is it
    '''
    no_of_j = 0

    count_elements = defaultdict(int)
    for symbol in hand:
        if symbol == 'J':
            no_of_j += 1
        else:
            count_elements[symbol] += 1

    values = sorted(count_elements.values())
    if len(values) == 0:
        values.append(no_of_j)
    else:
        values[-1] += no_of_j
    
    values = tuple(values)

    if values == (5,):
        # here all five cards have the same label: AAAAA
        return HandType.FIVE_OF_A_KIND

    elif values == (1, 4):
        # where four cards have the same label and one card has a different label: AA8AA
        return HandType.FOUR_OF_A_KIND

    elif values == (2, 3):
        # where three cards have the same label, and the 
        # remaining two cards share a different label: 23332
        return HandType.FULL_HOUSE

    elif values == (1, 1, 3):
        # where three cards have the same label, and the remaining two cards are 
        # each different from any other card in the hand: TTT98
        return HandType.THREE_OF_A_KIND

    elif values == (1, 2, 2):
        # where two cards share one label, two other cards share a second label, 
        # and the remaining card has a third label: 23432
        return HandType.TWO_PAIR

    elif values == (1, 1, 1, 2):
        # where two cards share one label, and the other three cards 
        # have a different label from the pair and each other: A23A4
        return HandType.ONE_PAIR

    # where all cards' labels are distinct: 23456
    return HandType.HIGH_CARD

def sort_by_rank_and_order_joker_modified(card):
    '''
    Logic to sort hand cards array
    '''
    hand_type = modified_check_type(card['hand'])
    rank_order = [hand_type.value, ]

    # Add number values from card
    for c in card['hand']:
        rank_order.append(MODIFIED_CARD_RANK[c])

    return tuple(rank_order)

def part2(file):
    '''Solution for part 2 of the problem'''
    cards = read_input(file)
    sorted_cards = sorted(cards, key=sort_by_rank_and_order_joker_modified, reverse=True)
    ans = 0
    for i in range(len(cards)):
        ans += sorted_cards[i]['bid'] * (i + 1)
    return ans

def main():
    '''Program Start Execution'''
    assert part1(EXAMPLE_FILE) == 6440
    print("Part 1 Result:", part1(INPUT_FILE))

    assert part2(EXAMPLE_FILE) == 5905
    print("Part 2 Result:", part2(INPUT_FILE))

if __name__ == "__main__":
    main()
