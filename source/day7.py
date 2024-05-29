"""Solve AOC day 7"""
from enum import Enum

class Type(Enum):
    FIVE_OF_KIND = 6
    FOUR_OF_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

class Hand:
    _card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
               '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    def _generate_type(self) -> Type:
        """generate the card type, This also takes the Joker rule into account

        :return: The card type
        """
        card_count = {}
        joker_count = 0

        # We can play with or without the Joker rule, with this rule we can pretend the joker can help you achieve the best result
        # Due to the fact that having more of one kind of card is the easiest way to score higher we can simplify the logic a lot.
        # we can simply add the amount of jokers we have to the most common card and we can completely ignore FULL_HOUSE as an option
        # For example if you have three of an kind + 1J + 1 you can either promote to an FULL_HOUSE or FOUR_OF_KIND where FOUR_OF_KIND will always win.
        # This logic remains the same for all other lower options.
        # If we do not play with the Joker rule we simply add the count back to the sorted_counts list and sort it again as the J counts as an normal card.

        for card in self.cards:
            if self.joker_rule and card == 'J':
                joker_count += 1
                continue

            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        sorted_counts = sorted(card_count.values(), reverse= True)

        if self.joker_rule:
            # it's possible all cards are jokers
            if len(sorted_counts) == 0:
                return Type.FIVE_OF_KIND
            else:
                sorted_counts[0] += joker_count
        elif joker_count != 0:
            sorted_counts.append(joker_count)
            sorted_counts.sort(reverse= True)

        if len(sorted_counts) == 1:
            return Type.FIVE_OF_KIND
        elif len(sorted_counts) == 2:
            if sorted_counts[0] == 4:
                return Type.FOUR_OF_KIND
            else:
                return Type.FULL_HOUSE
        elif len(sorted_counts) == 3:
            if sorted_counts[0] == 3:
                return Type.THREE_OF_KIND
            else:
                return  Type.TWO_PAIR
        elif len(sorted_counts) == 4:
            return Type.ONE_PAIR
        else:
            return Type.HIGH_CARD

    def __init__(self, cards: str, bid: int, joker_rule = False) -> None:
            self.cards = [card for card in cards]
            self.bid = bid

            self.joker_rule = joker_rule
            if joker_rule:
                self._card_values['J'] = 1

            self.type = self._generate_type()

    def __lt__(self, other) -> bool:
        """comparison operator for the hand based on type and card value

        :param other: the other hand to compare
        :return: if the left is smaller then the right hand
        """
        if self.type is not other.type:
            return self.type.value < other.type.value
        else:
            for (card, other_card) in zip(self.cards, other.cards):
                if card == other_card:
                    pass
                else:
                    return self._card_values[card] < other._card_values[other_card]

def main():
    with open("data/day7.txt", encoding="utf8") as file:

        hands = []
        for line in file.readlines():
            (cards, bid) = line.split(' ')
            hands.append(Hand(cards, int(bid), True))

    hands.sort()
    total_value = 0
    for (rank, hand) in enumerate(hands):
        total_value += (rank + 1) * hand.bid
    print(total_value)


if __name__ == '__main__':
    main()