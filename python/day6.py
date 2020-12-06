from functools import reduce


def readData(file):
    with open(file) as f:
        return f.read().replace('\n\n', '|').split('|')


def part1(file):
    uniqueCharacters = [set(x.replace('\n', '')) for x in file]
    return sum([len(x) for x in uniqueCharacters])


def commonIntersectForGroup(group):
    return len(reduce(set.intersection, [set(x)
                                         for x in group.split("\n")]))


def part2(file):
    return sum([commonIntersectForGroup(group) for group in file])


testData = readData('../inputs/day6.in.test')
data = readData('../inputs/day6.in')

print(part1(testData))
print(part1(data))

print(part2(testData))
print(part2(data))
