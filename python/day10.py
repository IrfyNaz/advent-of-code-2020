

def getDeviceJoltage(adapters):
    return max(adapters) + 3


def readFile(filename):
    with open(filename) as f:
        file = [int(x) for x in f.read().splitlines()]
        file.sort()
        return [0] + file + [getDeviceJoltage(file)]


testData = readFile('../inputs/day10.in.test')
testData2 = readFile('../inputs/day10-2.in.test')
testRichard = readFile('../inputs/day10.in.richard')
data = readFile('../inputs/day10.in')


def part1(adapters):
    prev = adapters[0]
    diffs = [-prev + (prev := x) for x in data[1:]]
    return diffs.count(1) * diffs.count(3)


print("Test part1 is: {}".format(part1(testData)))
print("Test (2) part1 is: {}".format(part1(testData2)))
print("The answer to part1 is: {}".format(part1(data)))


def countPaths(adapters, index, count):
    if index == len(adapters) - 1:
        return count + 1
    for i in range(index + 1, index + 4):
        if i >= len(adapters):
            break

        if adapters[i] - adapters[index] <= 3:
            count = countPaths(adapters, i, count)
        else:
            break
    return count


def part2(adapters):
    return countPaths(adapters, 0, 0)


def part2dp(adapters):
    bucket = [1] + [0 for x in range(adapters[-1])]
    for a in adapters:
        for i in range(max(0, a-3), a):
            bucket[a] += bucket[i]

    return bucket[-1]


print("Test 1 part2 is: {}".format(part2(testData)))
print("Test 2 part2 is: {}".format(part2(testData2)))
print("Data part2 is: {}".format(part2dp(data)))
