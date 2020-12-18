import copy

ACTIVE = '#'
INACTIVE = '.'


def convertActive(x):
    return [i == ACTIVE for i in x]


def convertPrint(x):
    return "".join([i == True and ACTIVE or INACTIVE for i in x])


def readFile(filename):
    with open(filename) as f:
        return [[convertActive(x) for x in f.read().splitlines()]]


testInput = readFile('/Users/irfan/work/aoc20/inputs/day17.in.test')
input = readFile('/Users/irfan/work/aoc20/inputs/day17.in')

# Rules
# If a cube is active and (2 or 3) neighbors are active, cube - active.
# Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
# Otherwise, the cube remains inactive.


def cubeRemainActive(xO, yO, zO, domain):
    activeNeighbourCount = 0
    indexesChecked = []
    for x in range(max(0, xO - 1), min(len(domain), xO + 2)):
        for y in range(max(0, yO - 1), min(len(domain[x]), yO + 2)):
            for z in range(max(0, zO - 1), min(len(domain[x][y]), zO + 2)):
                # print(f" [{xO}, {yO}, {zO}] | [{x}, {y}, {z}]")
                if(xO == x and yO == y and zO == z):
                    continue
                indexesChecked.append(f"{x}.{y}.{z}[{domain[x][y][z]}]")
                if domain[x][y][z]:
                    activeNeighbourCount += 1
    # print(f"{xO}.{yO}.{zO} -> {indexesChecked} -> {activeNeighbourCount}")
    return activeNeighbourCount


# [ [.], [.], [.] ] => [[., ., .], [., ., .], [., ., .], [., ., .], [., ., .]]
# [ [., ., .], [., ., .], [., ., .] ] -> [ [., ., ., ., .], [., ., ., ., .], [., ., ., ., .], [., ., ., ., .], [., ., ., ., .] ]
def expandDimensions(domain):
    newDomain = [[len(domain[0][0]) * [False]] * len(domain[0])] + \
        copy.deepcopy(domain) + \
        [[len(domain[0][0]) * [False]] * len(domain[0])]
    for i in range(len(newDomain)):
        newDomain[i] = [len(newDomain[i][0]) * [False]] + newDomain[i] + \
            [len(newDomain[i][0]) * [False]]
        for j in range(len(newDomain[i])):
            newDomain[i][j] = [False] + newDomain[i][j] + [False]

    return newDomain


def countActive(domain):
    activeNodes = 0
    print(domain)
    for x in range(len(domain)):
        for y in range(len(domain[x])):
            for z in range(len(domain[x][y])):
                activeNodes += domain[x][y][z]
    return activeNodes


def printStage(domain):
    for z in range(len(domain)):
        zf = z - ((len(domain) - 1) // 2)
        print("")
        print(f"z={zf}")
        for x in range(len(domain[z])):
            print(convertPrint(domain[z][x]))


def part1(input, iterations):
    nextArray = copy.deepcopy(input)
    print("")
    print("Before iterations")
    printStage(nextArray)
    for i in range(iterations):
        # print(f"Iteration: {i+1}")
        # print(nextArray)
        nextArray = expandDimensions(nextArray)
        prevArray = copy.deepcopy(nextArray)

        for x in range(len(nextArray)):
            for y in range(len(nextArray[x])):
                for z in range(len(nextArray[x][y])):
                    activeNeighbourCount = cubeRemainActive(x, y, z, prevArray)
                    # print(
                    #     f" {x} {y} {z} -> {prevArray[x][y][z]} {activeNeighbourCount}")
                    toggle = (
                        (prevArray[x][y][z] == True and not (activeNeighbourCount == 2 or activeNeighbourCount == 3)) or
                        (prevArray[x][y][z] == False and activeNeighbourCount == 3))
                    if toggle:
                        # print(f'   Toggling -> {not prevArray[x][y][z]}')
                        nextArray[x][y][z] = not prevArray[x][y][z]
        print("")
        print(f"After iteration {i+1}")
        printStage(nextArray)

    return nextArray


testDataAnswer = part1(testInput, 6)
print(f"    Test 1 part1 is: {countActive(testDataAnswer)} ")

dataAnswer = part1(input, 6)
print(f"Part 1 is: {countActive(dataAnswer)} ")

# print("********************************************************")


# testDataAnswer = part2(testInput)
# print(f"    Test 1 part2 is: {sum(testDataAnswer)} -> {testDataAnswer} ")
# dataAnswer = part2(input)
# print(f"Part 2 is: {sum(dataAnswer)} -> {dataAnswer} ")
