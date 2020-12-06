import math

with open("../inputs/day3.in") as f:
    data = [list(x) for x in f.read().splitlines()]
with open("../inputs/day3.in.test") as f:
    testData = [list(x) for x in f.read().splitlines()]


def part1(data, xStep, yStep):
    yIndices = range(0, len(data), yStep)
    width = len(data[0])
    xIndices = range(0, width * math.ceil(len(data)/width) * xStep, xStep)
    return(sum([data[y][x % width] == '#' for y, x in zip(yIndices, xIndices)]))


print(part1(testData, 3, 1))
print(part1(data, 3, 1))

paths = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

print(math.prod([part1(testData, x, y) for x, y in paths]))
print(math.prod([part1(data, x, y) for x, y in paths]))
