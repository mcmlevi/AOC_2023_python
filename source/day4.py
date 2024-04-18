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
    file = open("data/day4.txt", encoding="utf-8")
    sum_of_cards = 0
    for line in file.readlines():
        (winning_numbers, card_numbers) = get_numbers(line)
        number_of_matching_numbers = len([x for x in card_numbers if x in winning_numbers])
        if number_of_matching_numbers > 0:
            sum_of_cards += (1 <<  number_of_matching_numbers - 1)

    return sum_of_cards

print(part1())