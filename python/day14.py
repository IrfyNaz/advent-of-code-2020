from collections import defaultdict
import re
import itertools


def readFile(filename):
    with open(filename) as f:
        return f.read().splitlines()


testInput = readFile('../inputs/day14.in.test')
input = readFile('../inputs/day14.in')


def part1(program):
    bitmask = ''
    mem = defaultdict(lambda: 0)
    for line in program:
        if line.startswith('mask'):
            # ::-1 gives a reversed slice
            bitmask = line.split('mask = ')[-1][::-1]
        elif line.startswith('mem'):
            lineGroups = re.search('^mem\[([0-9]*)\] = (\d*)$', line)
            value = int(lineGroups.group(2))

            for i, m in enumerate(bitmask):
                if m == '1':
                    value |= (1 << i)
                elif m == '0':
                    value &= ~(1 << i)
                # print(f"value = {value} | mask = {i}:{m}")
            mem[int(lineGroups.group(1))] = value

    return sum(mem.values())


testDataAnswer = part1(testInput)
print(f"    Test 1 part1 is: {testDataAnswer}")

# dataAnswer = part1(input)
# print(f"Answer Part 1 is: {dataAnswer}")

print("********************************************************")


def part2(program):
    bitmask = ''
    mem = defaultdict(lambda: 0)
    for line in program:
        if line.startswith('mask'):
            # ::-1 gives a reversed slice
            bitmask = line.split('mask = ')[-1]
            print(f"new mask: {bitmask}")
        elif line.startswith('mem'):
            lineGroups = re.search('^mem\[([0-9]*)\] = (\d*)$', line)
            value = int(lineGroups.group(2))
            memAdd = int(lineGroups.group(1))
            bMemAdd = f"{memAdd:36b}"
            print(f"{memAdd} => {bMemAdd.rjust(36, '0')}")
            for i, m in enumerate(bitmask):
                if m == '1':
                    memAdd |= (1 << i)
                elif m == '0':
                    continue
                else m == 'X':

    return False


testDataAnswer = part2(testInput)
print(f"    Test 1 part2 is: {testDataAnswer}")

# dataAnswer = part2(input)
# print(f"Answer Part 2 is: {dataAnswer}")
