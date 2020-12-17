import re
import collections
import math


def readFile(filename):
    with open(filename) as f:
        return f.read().splitlines()


testInput = readFile('/Users/irfan/work/aoc20/inputs/day16.in.test')
testInput2 = readFile('/Users/irfan/work/aoc20/inputs/day16.in.test2')
input = readFile('/Users/irfan/work/aoc20/inputs/day16.in')


def parseInput(input):
    rules = {}
    tickets = []
    for line in input:
        if line == "":
            continue
        elif line == "your ticket:":
            break
        else:
            lineGroups = re.search(
                '^([a-zA-Z ]*): ([0-9]*)-([0-9]*) or ([0-9]*)-([0-9]*)$', line)
            ruleName = lineGroups.group(1)
            rules[ruleName] = [int(lineGroups.group(2)), int(lineGroups.group(
                3)), int(lineGroups.group(4)), int(lineGroups.group(5))]

    def parseTicket(ticket): return [int(x) for x in ticket.split(',')]

    myticket = parseTicket(input[len(rules)+2])
    tickets = [parseTicket(x) for x in input[len(rules)+5:]]
    return [rules, myticket, tickets]


def testRule(x, minA, maxA, minB, maxB):
    return minA <= x <= maxA or minB <= x <= maxB


def part1(fileData):
    rules, myTicket, tickets = parseInput(fileData)
    invalidValues = []
    validTickets = []
    positions = collections.defaultdict(lambda: [])
    for ticket in tickets:
        validTicket = True
        for i in range(len(ticket)):
            value = ticket[i]
            potentiallyValidRules = []
            valid = False
            for ruleName, ruleValues in rules.items():
                testResult = testRule(
                    value, ruleValues[0], ruleValues[1], ruleValues[2], ruleValues[3])
                valid |= testResult
                if testResult:
                    potentiallyValidRules.append(ruleName)

            if not valid:
                invalidValues.append(value)
            validTicket &= valid
            if(len(potentiallyValidRules)):
                positions[i].append(potentiallyValidRules)
        if validTicket:
            validTickets.append(ticket)

    print(f"Part 1 answer is: {sum(invalidValues)}")

    positions = {key: [set(value)
                       for value in values] for key, values in positions.items()}

    for pos, potentials in positions.items():
        validatedOptions = potentials[0].intersection(*potentials)
        positions[pos] = validatedOptions

    confirmedFields = collections.defaultdict(lambda: set())

    counter = 0
    while (len(positions)):
        counter += 1
        if counter % 100 == 1:
            print(f"{counter} -> Solved {len(confirmedFields)}")
        posToRemove = []
        for pos, fields in positions.items():
            others = {k: v for k, v in positions.items() if k != pos}
            for confirmed in confirmedFields.values():
                fields.discard(confirmed)
            differences = fields.difference(*others.values())
            found = False
            if len(fields) == 1:
                confirmedFields[pos] = fields.pop()
                found = True
            elif len(differences) == 1:
                confirmedFields[pos] = differences.pop()
                found = True
                # remove this field from all other sets:
            if found:
                posToRemove.append(pos)

        positions = {k: v for k, v in positions.items()
                     if k not in posToRemove}

    keysToCheck = {k: v for k, v in confirmedFields.items()
                   if 'departure' in v}
    valuesToCheck = [myTicket[k] for k in keysToCheck.keys()]
    print(f"Part 2 is {math.prod(valuesToCheck)}")
    return invalidValues


# testDataAnswer = part1(testInput)
# print(f"    Test 1 part1 is: {sum(testDataAnswer)} -> {testDataAnswer} ")

# dataAnswer = part1(input)
# print(f"Part 1 is: {sum(dataAnswer)} -> {dataAnswer} ")

# print("********************************************************")


# testDataAnswer = part1(testInput2)
# print(f"    Test 1 part2 is: {sum(testDataAnswer)} -> {testDataAnswer} ")

dataAnswer = part1(input)
print(f"    Test 1 part2 is: {sum(dataAnswer)} -> {dataAnswer} ")
