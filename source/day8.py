from math import lcm

def part1(instructions, mappings) -> int:
    step_count = 0
    current_node = "AAA"
    while True:
        for instruction in instructions:
            step_count += 1
            match instruction:
                case 'L':
                    current_node = mappings[current_node][0]
                case 'R':
                    current_node = mappings[current_node][1]

            if current_node == "ZZZ":
                return step_count

def part2(instructions, mappings) -> int:
    """Calculate the number of steps before all nodes end on an Z

    :param instructions: the instructions to follow
    :param mappings: the mappings for the instructions
    :return: the number of steps needed
    """

    # I really don't like this approach this relies on the fact that it seems AOC
    # enforces the cycle is symmetric and the distance to an Z node is exactly half the cycle
    # meaning you just really need to find the first Z node and your problem is solved.
    # Once you have these distances you can just take the LCM and you have your answer

    step_count = 0
    current_nodes = [key for key in mappings.keys() if key[-1] == 'A']
    distances = [0] * len(current_nodes)
    while True:
        for instruction in instructions:
            step_count += 1
            finished = True
            for (index, node) in enumerate(current_nodes):
                if distances[index] != 0:
                    continue

                finished = False

                match instruction:
                    case 'L':
                        current_nodes[index] = mappings[node][0]
                    case 'R':
                        current_nodes[index] = mappings[node][1]

                if current_nodes[index][-1] == 'Z':
                    distances[index] = step_count

        if finished:
            break

    return lcm(*distances)

def main():
    with open("data/day8.txt", encoding="utf8") as file:
        lines = file.readlines()
        instructions = lines[0].strip()
        mappings = {}
        for line in lines[2:]:
            # I am to lazy to do nice pattern matching so we simply remove any
            # characters besides spaces and the mapping entries.
            line = line.translate({ord('('): None, ord(')'): None,
                                   ord(','): None, ord('='): None, ord('\n'): None})

            (key, left, right) = [entry for entry in line.split(' ') if len(entry) != 0 ]

            mappings[key] = (left, right)

    print(part1(instructions, mappings))
    print(part2(instructions, mappings))

if __name__ == '__main__':
    main()