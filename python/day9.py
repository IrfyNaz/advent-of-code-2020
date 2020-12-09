
def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().splitlines()]


testData = readFile('../inputs/day9.in.test')
data = readFile('../inputs/day9.in')


def existSummablePair(set, target):
    for i in range(0, len(set)-1):
        for j in range(i+1, len(set)):
            if set[i] + set[j] == target:
                return True
    return False


def part1(data, lookbackRange):
    for i in range(lookbackRange, len(data)):
        if not existSummablePair(data[i-lookbackRange:i], data[i]):
            return [i, data[i]]
    return True


invalidTest = part1(testData, 5)
print("Test part1 is: {}".format(invalidTest))
invalidData = part1(data, 25)
print("The answer to part1 is: {}".format(invalidData))


def existSummableRange(set, target):
    for i in range(0, len(set)-1):
        for j in range(i+2, len(set)):
            if(sum(set[i:j]) == target):
                return(set[i:j])
    return False


def part2(data, target):
    result = existSummableRange(data, target)
    return(min(result) + max(result))


print("Test part2 is: {}".format(part2(testData, invalidTest[1])))
print("The answer to part2 is: {}".format(part2(data, invalidData[1])))
