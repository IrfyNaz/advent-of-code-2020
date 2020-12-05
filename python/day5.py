def readData(file):
    with open(file) as f:
        return [[x[:7], x[7:]] for x in f.read().splitlines()]


def convertSequence(sequence):
    return[x in ['F', 'L'] for x in sequence]


def getMidDistance(start, end):
    distance = (end - start)
    if distance % 2:
        distance -= 1
    return int((distance / 2) + 1)


def split(sequence, startRow, endRow):
    # Expects a sequence of True or False for picking the first or second half.
    # That is to say F or L == True
    # print('Start: {}, end: {}, seq: {}'.format(startRow, endRow, sequence))
    midDistance = getMidDistance(startRow, endRow)
    if(endRow - startRow == 1):
        if(sequence[0]):
            return startRow
        else:
            return endRow

    if sequence[0]:
        return split(sequence[1:], startRow, endRow - midDistance)

    return split(sequence[1:], startRow + midDistance, endRow)


def getSeatNumber(rowMap, columnMap):
    rowNum = split(convertSequence(rowMap), 0, 127)
    columnNum = split(convertSequence(columnMap), 0, 7)
    return rowNum * 8 + columnNum


testData = readData('day5.in.test')
print([getSeatNumber(x, y) for x, y in testData])

data = readData('day5.in')
seats = [getSeatNumber(x, y) for x, y in data]
print(max(seats))


# Part 2
minSeat = min(seats)
maxSeat = max(seats)

print(sum(range(minSeat, maxSeat + 1, 1)) - sum(set(seats)))
