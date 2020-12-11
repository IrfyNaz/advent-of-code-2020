import copy


def readFile(filename):
    with open(filename) as f:
        return [list(x) for x in f.read().splitlines()]


testData = readFile('../inputs/day11.in.test')
data = readFile('../inputs/day11.in')


def printGrid(data):
    for row in data:
        print(''.join(row))


def countOccupied(data):
    return sum(x.count('#') for x in data)


def checkNeighbour(data, row, column):
    maxRow = len(data) - 1
    maxCol = len(data[0]) - 1
    count = 0
    for checkRow in range(max(0, row - 1), min(maxRow, row + 1) + 1):
        for checkColumn in range(max(0, column - 1), min(maxCol, column + 1) + 1):
            if checkRow == row and checkColumn == column:
                continue
            if data[checkRow][checkColumn] == '#':
                count += 1
    return count


def checkDirection(data, row, column, incRow, incCol):
    maxRow = len(data) - 1
    maxCol = len(data[0]) - 1

    row += incRow
    column += incCol

    # Check if row is out of bands:
    if (row < 0 or row > maxRow) or (column < 0 or column > maxCol):
        return False
    elif data[row][column] == '#':
        return True
    elif data[row][column] == 'L':
        return False

    return checkDirection(data, row, column, incRow, incCol)


def part1(file):
    counter = 0
    new_file = copy.deepcopy(file)
    while True:
        old_file = copy.deepcopy(new_file)
        changes = 0
        for row in range(0, len(old_file)):
            for column in range(0, len(old_file[row])):
                count = checkNeighbour(old_file, row, column)
                if old_file[row][column] == 'L' and count == 0:
                    changes += 1
                    new_file[row][column] = '#'
                elif old_file[row][column] == '#' and count > 3:
                    changes += 1
                    new_file[row][column] = 'L'
        counter += 1
        # print(f"{counter} -> {changes}")
        # printGrid(new_file)
        if changes == 0:
            break
    return new_file


print(f"    Test 1 part1 is: {countOccupied(part1(testData))}")
print(f"The answer to part1 is: {countOccupied(part1(data))}")


def part2(file):
    counter = 0
    new_file = copy.deepcopy(file)
    while True:
        old_file = copy.deepcopy(new_file)
        changes = 0
        for row in range(0, len(old_file)):
            for column in range(0, len(old_file[row])):
                count = 0
                count += checkDirection(old_file, row, column, -1, -1)
                count += checkDirection(old_file, row, column, -1, 0)
                count += checkDirection(old_file, row, column, -1, 1)
                count += checkDirection(old_file, row, column, 0, -1)
                count += checkDirection(old_file, row, column, 0, 1)
                count += checkDirection(old_file, row, column, 1, -1)
                count += checkDirection(old_file, row, column, 1, 0)
                count += checkDirection(old_file, row, column, 1, 1)

                if old_file[row][column] == 'L' and count == 0:
                    changes += 1
                    new_file[row][column] = '#'
                elif old_file[row][column] == '#' and count > 4:
                    changes += 1
                    new_file[row][column] = 'L'
        counter += 1
        # print(f"{counter} -> {changes}")
        # printGrid(new_file)
        if changes == 0:
            break
    return new_file


print("*****************************************")
print(f"    Test 1 part2 is: {countOccupied(part2(testData))}")
print(f"The answer to part2 is: {countOccupied(part2(data))}")
