"""Solve day 9 of advent of code"""

import re

def build_difference_tree(entry):
    """build the difference tree based on oasis history data

    :param entry: the history entry to calculate the difference tree of
    :return: tree of all differences
    """
    tree = [entry]
    all_zero = False
    while all_zero is False:
        all_zero = True
        tree.append([])

        if len(tree[-2]) == 1:
            tree[-1].append(0)

        for x,y in zip(tree[-2], tree[-2][1:]):
            # This gives us the abs distance however the difference might be negative as well if
            # y is smaller then x and then it needs to be inverted
            difference = abs(y - x)
            if y < x :
                difference = -difference

            tree[-1].append(difference)
            if difference != 0:
                all_zero = False

    return tree

def calculate_next_tree_entry(tree) -> int:
    """Calculate the next history value

    :param tree: the difference tree produced by build_difference_tree
    :return: the next value in the history
    """
    for index in range(1, len(tree)):
        difference = tree[-index][-1]
        tree[-(index + 1)].append(tree[-(index + 1)][-1] + difference)

    return tree[0][-1]

def calculate_prev_tree_entry(tree) -> int:
    """Calculate the previous history value

    :param tree: the difference tree produced by build_difference_tree
    :return: the previous value in the history
    """
    for index in range(1, len(tree)):
        difference = tree[-index][0]
        next_value = tree[-(index + 1)][0] - difference
        tree[-(index + 1)].insert(0, next_value)

    return tree[0][0]



def part1(entries) -> int:
    """Solve part 1 of day 9"""
    total_count = 0
    for entry in entries:
        tree = build_difference_tree(entry)
        total_count += calculate_next_tree_entry(tree)
    return total_count

def part2(entries) -> int:
    """Solve part 2 of day 9"""
    total_count = 0
    for entry in entries:
        tree = build_difference_tree(entry)
        total_count += calculate_prev_tree_entry(tree)
    return total_count

def main():
    with open("data/day9.txt", encoding="utf8") as file:
        entries = [[int(entry) for entry in re.findall(R"-?\d+", line)] for line in file.readlines()]
        print(part1(entries))
        print(part2(entries))
if __name__ == "__main__":
    main()