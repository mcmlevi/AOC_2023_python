import re

def check_grid(y_pos, x_pos, size, grid, row_count, row_lenght):
    """Loop around the grid and check if any value is an special character

    Args:
        y_pos (_type_): _description_
        x_pos (_type_): _description_
        size (_type_): _description_
        grid (_type_): _description_
        row_count (_type_): _description_
        row_lenght (_type_): _description_

    Returns:
        Bool: returns true if an special character can be found
    """
    for y in range((0 if y_pos - 1 < 0 else y_pos -1 ), (row_count if y_pos + 2 > row_count else y_pos + 2), 1):
        for x in range((0 if x_pos - 1 < 0 else x_pos -1 ), (row_lenght if x_pos + size + 1 > row_lenght else x_pos + size + 1), 1):
            if grid[y][x] != '.':
                return True

def find_gear_indentifiers(grid, row_count, row_lenght, gear_identifier):
    gear_multipliers = []
    for y in range(row_count):
        for x in range(row_lenght):        
            if grid[y][x] == gear_identifier:
                gear_multipliers.append((y,x))
                
    return gear_multipliers

def match_part_numbers(parts, gear_modifier):
    matches = []
    for ((part_info), number) in parts:
        for offset in range(part_info[2]):
            if abs(part_info[0] - gear_modifier[0]) <= 1 and abs(part_info[1] + offset - gear_modifier[1]) <= 1:
                matches.append(((part_info), number))
                break
            
    return matches
            

def find_gear_multipiers(part_numbers, grid, row_count, row_lenght):
    sum = 0
    for modifier in find_gear_indentifiers(grid, row_count, row_lenght, "*"):
        matches = match_part_numbers(part_numbers, modifier)
        if len(matches) == 2:
            sum += matches[0][1] * matches[1][1]
    return sum
            
def part1():
    file = open("data/day3_sample1.txt")
    data_grid = []
    partnumbers = []
    sum = 0
    for (row, line) in enumerate(file.readlines()):
        line = line.rstrip()
        numbers = re.findall("\d+", line)
        
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
            sum += value
            
    return sum     

def part2():
    file = open("data/day3.txt")
    data_grid = []
    partnumbers = []
    sum = 0
    for (row, line) in enumerate(file.readlines()):
        line = line.rstrip()
        numbers = re.findall("\d+", line)
        
        # build coordinate map for all found numbers
        for number in numbers:
            column = line.find(number)
            line = line.replace(number, "." * len(number), 1)
            partnumbers.append(((row, column, len(number)), int(number)))
        
        data_grid.append([x for x in line])
            
    row_lenght = len(data_grid[0])
    row_count = len(data_grid)
    return find_gear_multipiers(partnumbers, data_grid, row_count, row_lenght)
    
print(part1())
print(part2())   
    
    