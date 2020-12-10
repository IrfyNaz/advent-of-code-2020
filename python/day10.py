
def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().splitlines()]


testData = readFile('../inputs/day10.in.test')
testData2 = readFile('../inputs/day10-2.in.test')
data = readFile('../inputs/day10.in')


def getDeviceJoltage(adapters):
    return max(adapters) + 3


def part1(adapters):
    data = adapters.copy()
    data.append(getDeviceJoltage(data))
    data.sort()
    print(data)
    prev = 0
    diffs = [-prev + (prev := x) for x in data]
    return diffs.count(1) * diffs.count(3)


invalidTest = part1(testData)
print("Test part1 is: {}".format(invalidTest))
invalidTest2 = part1(testData2)
print("Test (2) part1 is: {}".format(invalidTest2))

invalidData = part1(data)
print("The answer to part1 is: {}".format(invalidData))


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
    data = adapters.copy()
    data.append(getDeviceJoltage(data))
    data.append(0)
    data.sort()
    return countPaths(data, 0, 0)


def part2dp(adapters):
    data = adapters.copy()
    deviceJolt = getDeviceJoltage(data)
    data.append(deviceJolt)
    data.append(0)
    data.sort()

    bucket = [1] + [0 for x in range(data[-1])]
    for a in data:
        for i in range(max(0, a-3), a):
            bucket[a] += bucket[i]

    return bucket[-1]


# print("Test part2 is: {}".format(part2(testData)))
# print("Test part2 is: {}".format(part2(testData2)))
# print("Data part2 is: {}".format(part2(data)))

print(part2dp(testData))
print(part2dp(testData2))
print(part2dp(data))
