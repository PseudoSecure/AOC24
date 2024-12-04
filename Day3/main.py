import re

def part1():

    total = 0
    pattern = r"mul\(\d+,\d+\)"
    with open('input.txt', 'r') as file:
        for line in file:
            elements = line
            matches = re.findall(pattern, elements)

    for match in matches:
        extraction_pattern = r"mul\((\d+),(\d+)\)"
        match = re.match(extraction_pattern, match)
        num1, num2 = match.groups()
        total += int(num1)*int(num2)


    print(total)


def part2():
    pass

part1()

# part2()