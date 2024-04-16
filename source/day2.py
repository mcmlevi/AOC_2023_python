from collections import defaultdict
import math

def part1(cubes: dict):
    file = open("data\day2.txt")
    sum = 0
    
    for (gameID, line) in enumerate(file.readlines()):
        line = line[line.find(": "):].rstrip()
        shown_cubes = [entries.strip().split(" ") for game in line.split(";") for entries in game.split(",")]
        possible = True
        for (value, key) in shown_cubes:
            if int(value) > cubes[key]:
                possible = False
                break
            
        if possible:
            sum += gameID + 1
        
    return sum
        
def part2():
    file = open("data\day2.txt")
    sum = 0
    
    for (gameID, line) in enumerate(file.readlines()):
        line = line[line.find(":") + 1 :].rstrip()
        shown_cubes = [entries.strip().split(" ") for game in line.split(";") for entries in game.split(",")]
        power_map = defaultdict(int)
        for (value, key) in shown_cubes:
            power_map[key] = max(power_map[key], int(value))
        sum += math.prod(power_map.values())
        
    return sum       


print(part1({"red": 12, "green": 13, "blue":14}))
print(part2())

    