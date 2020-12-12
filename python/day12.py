import math


def readFile(filename):
    with open(filename) as f:
        return [[x[0], int(x[1:])] for x in f.read().splitlines()]


testData = readFile('../inputs/day12.in.test')
data = readFile('../inputs/day12.in')

instructionToVector = {
    'N': lambda x, y, angle, distance: [x, y + distance, angle],
    'S': lambda x, y, angle, distance: [x, y - distance, angle],
    'E': lambda x, y, angle, distance: [x + distance, y, angle],
    'W': lambda x, y, angle, distance: [x - distance, y, angle],
    'L': lambda x, y, angle, distance: [x, y, angle + distance],
    'R': lambda x, y, angle, distance: [x, y, angle - distance],
    'F': lambda x, y, angle, distance: getDistanceForAngle(x, y, angle, distance),
    'B': lambda x, y, angle, distance: getDistanceForAngle(x, y, angle, -distance)
}


def getDistanceForAngle(x, y, angle, distance):
    angleInRadians = (angle) * math.pi / 180
    xx = int(distance * math.cos(angleInRadians))
    yy = int(distance * math.sin(angleInRadians))
    return [x + xx, y + yy, angle]


def part1(file):
    x = 0
    y = 0
    shipAngle = 0
    for i in range(0, len(file)):
        instruction, value = file[i]
        x, y, shipAngle = instructionToVector[instruction](
            x, y, shipAngle, value)
        print(f"{file[i]} => {x} {y} @ {shipAngle}")
    return [x, y, shipAngle]


def getManhattenDistance(x, y):
    return abs(x) + abs(y)


testDataAnswer = part1(testData)
print(
    f"    Test 1 part1 is: {getManhattenDistance(testDataAnswer[0], testDataAnswer[1])}")
dataAnswer = part1(data)
print(
    f"part1 is: {getManhattenDistance(dataAnswer[0], dataAnswer[1])}")


instructionToVectorPart2 = {
    'N': lambda x, y, xW, yW, distance: [x, y, xW, yW + distance],
    'S': lambda x, y, xW, yW, distance: [x, y, xW, yW - distance],
    'E': lambda x, y, xW, yW, distance: [x, y, xW + distance, yW],
    'W': lambda x, y, xW, yW, distance: [x, y, xW - distance, yW],
    'L': lambda x, y, xW, yW, angle: rotateWaypoint(x, y, xW, yW, -angle),
    'R': lambda x, y, xW, yW, angle: rotateWaypoint(x, y, xW, yW, angle),
    'F': lambda x, y, xW, yW, distance: [x + (distance * xW), y + (distance * yW), xW, yW],
    'B': lambda x, y, xW, yW, distance: [x - (distance * xW), y - (distance * yW), xW, yW]
}


def rotateWaypoint(x, y, xW, yW, angle):
    angleInRadians = (angle) * math.pi / 180
    yyW = yW * math.cos(angleInRadians) - xW * math.sin(angleInRadians)
    xxW = yW * math.sin(angleInRadians) + xW * math.cos(angleInRadians)
    return [x, y, round(xxW), round(yyW)]


def part2(file):
    waypointX = 10
    waypointY = 1

    x = 0
    y = 0

    for i in range(0, len(file)):
        instruction, value = file[i]
        x, y, waypointX, waypointY = instructionToVectorPart2[instruction](
            x, y, waypointX,  waypointY, value)
        print(f"{file[i]} => {x} {y} @ {waypointX} {waypointY}")
    return [x, y, waypointX, waypointY]

    return False


print("*****************************************")
testDataAnswer2 = part2(testData)
dataAnswer2 = part2(data)
print(
    f"    Test 1 part2 is: {getManhattenDistance(testDataAnswer2[0], testDataAnswer2[1])}")
print(
    f"part2 is: {getManhattenDistance(dataAnswer2[0], dataAnswer2[1])}")
