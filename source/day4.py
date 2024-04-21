"""This module solves day 4 of AOC 2023"""

def get_numbers(line: str):
    """Get all numbers from an given line

    Args:
        line (str): the line to parse

    Returns:
        (list: int, list: int): 2 lists containing the winning numbers and the numbers on the card
    """
    line = line[line.find(":") + 1:]
    sections = line.split("|")
    winning_numbers = [value.strip() for value in sections[0].split(" ") if len(value) > 0]
    card_numbers = [value.strip() for value in sections[1].split(" ") if len(value) > 0]
    return (winning_numbers, card_numbers)

def part1():
    """Solve part 1 of day 4"""
    file = open("data/day4.txt", encoding="utf-8")
    sum_of_cards = 0
    for line in file.readlines():
        (winning_numbers, card_numbers) = get_numbers(line)
        number_of_matching_numbers = len([x for x in card_numbers if x in winning_numbers])
        if number_of_matching_numbers > 0:
            sum_of_cards += (1 <<  number_of_matching_numbers - 1)

    return sum_of_cards

class ScratchCard:
    """container representing the scratch card
    """
    winning_cards = []
    card_numbers = []

    def __init__(self, line: str) -> None:
        (self.winning_cards, self.card_numbers) = get_numbers(line)

    def get_number_of_matches(self):
        """ Get the number of matches from the winning and contained cards"""
        return len([x for x in self.card_numbers if x in self.winning_cards])

def part2():
    """Solve part 2 of day 4 of AOC"""
    file = open("data/day4.txt", encoding="utf-8")
    cards = [(ScratchCard(line), 1) for line in file.readlines()]
    for (index, (card, count)) in enumerate(cards):
        for i in range(1, card.get_number_of_matches() + 1):
            (next_card, next_card_count) = cards[index + i]
            cards[index + i] = (next_card, next_card_count + count)

    return sum(count for (_, count) in cards)


print(part1())
print(part2())
