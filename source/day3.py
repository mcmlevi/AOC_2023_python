"""Regex is used to find numbers input"""
import re

def check_grid(y_pos, x_pos, size, grid, row_count, row_lenght):
    """Loop around the grid and check if any value is an special character

    Args:
        y_pos (int): x poistion in grid
        x_pos (int): y position in grid
        size (int): number of elements the number takes up
        grid ([[int]]): 2d grid containing symbols
        row_count (int): number of rows in the grid
        row_lenght (int): lenght of an single row in the grid

    Returns:
        Bool: returns true if an special character can be found
    """
    for y in range((0 if y_pos - 1 < 0 else y_pos -1 ),
                   (row_count if y_pos + 2 > row_count else y_pos + 2), 1):
        for x in range((0 if x_pos - 1 < 0 else x_pos -1 ),
                       (row_lenght if x_pos + size + 1 > row_lenght else x_pos + size + 1), 1):
            if grid[y][x] != '.':
                return True

def find_in_grid(grid, row_count, row_lenght, identifier):
    """Generate an list of positions given an indentifier

    Args:
        grid ([[int]]): 2d grid containing symbols
        row_count (int): number of rows in the grid
        row_lenght (int): lenght of an single row in the grid
        identifier (char): the indentifier to find

    Returns:
        [(int,int)]: list of tupple containing the positions
    """
    gear_multipliers = []
    for y in range(row_count):
        for x in range(row_lenght):
            if grid[y][x] == identifier:
                gear_multipliers.append((y,x))

    return gear_multipliers

def find_parts_around_position(parts, position):
    """check if any parts are around an given position

    Args:
        parts list: ((y,x,size), number)): list of parts to search in
        gear_modifier (y,x): 2d position to search around

    Returns:
        list: ((y,x,size), number)): list of parts that surround the provided coordinates
    """
    matches = []
    for ((part_info), number) in parts:
        for offset in range(part_info[2]):
            if abs(part_info[0] - position[0]) <= 1 and abs(
                part_info[1] + offset - position[1]) <= 1:
                matches.append(((part_info), number))
                break

    return matches


def get_sum_of_gear_ratios(part_numbers, grid, row_count, row_lenght):
    """Find the total sum of all gear ratios

    Gear ratios are defines as any 2 parts connected by an "*",
    it's only an valid gear ratio if the "*" is only connected to ONLY 2 parts

    Args:
        part_numbers ((y: int, x: int size: int), number: int): list of part numbers
        found in the input data
        grid (list: [[char]]): grid of symbols
        row_count (int): total row count
        row_lenght (int): lenght of an single row

    Returns:
        int: total count of all gear ratios
    """
    sum_of_gear_ratios = 0
    for modifier in find_in_grid(grid, row_count, row_lenght, "*"):
        matches = find_parts_around_position(part_numbers, modifier)
        if len(matches) == 2:
            sum_of_gear_ratios += matches[0][1] * matches[1][1]
    return sum_of_gear_ratios

def part1():
    """Solve part 1 of day 3

    Returns:
        int: the value needed for P1 day 3
    """
    file = open("data/day3_sample1.txt", encoding="utf-8")
    data_grid = []
    partnumbers = []
    sum_of_parts = 0
    for (row, line) in enumerate(file.readlines()):
        line = line.rstrip()
        numbers = re.findall(R"\d+", line)

        # build coordinate map for all found numbers
        for number in numbers:
            column = line.find(number)
            line = line.replace(number, "." * len(number), 1)
            partnumbers.append(((row, column, len(number)), int(number)))

        data_grid.append([x for x in line])

    row_lenght = len(data_grid[0])
    row_count = len(data_grid)
    for ((y_pos, x_pos, size), value) in partnumbers:
        if check_grid(y_pos, x_pos, size, data_grid, row_count, row_lenght):
            sum_of_parts += value

    return sum_of_parts

def part2():
    """Solve part 2 of day 3

    Returns:
        int: the value needed for part 2 day 3
    """
    file = open("data/day3.txt", encoding="utf-8")
    data_grid = []
    partnumbers = []
    for (row, line) in enumerate(file.readlines()):
        line = line.rstrip()
        numbers = re.findall(R"\d+", line)

        # build coordinate map for all found numbers
        for number in numbers:
            column = line.find(number)
            line = line.replace(number, "." * len(number), 1)
            partnumbers.append(((row, column, len(number)), int(number)))

        data_grid.append([x for x in line])

    row_lenght = len(data_grid[0])
    row_count = len(data_grid)
    return get_sum_of_gear_ratios(partnumbers, data_grid, row_count, row_lenght)

print(part1())
print(part2())
