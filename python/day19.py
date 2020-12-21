import re
import copy


def readFile(filename):
    with open(filename) as f:
        return f.read().splitlines()


def parseInnerRule(value):
    if '"' in value:
        return value.replace('"', '')
    elif value == "|":
        return value
    else:
        return int(value)


def parseFile(filename):
    fileData = readFile(filename)
    rules = {}
    messages = []
    for i in range(len(fileData)):
        line = fileData[i]
        if ":" in line:
            ruleNum, rule = line.split(':')
            rules[int(ruleNum)] = [parseInnerRule(x)
                                   for x in rule.split(' ') if x != '']
        else:
            messages = fileData[i+1:]
            break
    return [rules, messages]


def expandRule(curRule, rules):
    # get new strings
    options = [copy.copy(curRule)]
    if "|" in curRule:
        idx = curRule.index("|")
        options = [curRule[:idx]]
        options.append(curRule[idx+1:])
    strings = []
    for option in options:
        optionStrings = ['']
        for subrule in option:
            if(isinstance(subrule, str)):
                subStrings = [subrule]
            else:
                subStrings = expandRule(rules[subrule], rules)
            optionStrings = [a + o for o in subStrings for a in optionStrings]

        strings += optionStrings
    return strings


def part1(rules, messages):
    possibleMessages = expandRule(rules[0], rules)
    print(possibleMessages)
    count = 0
    for message in messages:
        if message in possibleMessages:
            count += 1
    return count


# testRules, testMessages = parseFile(
#     '/Users/irfan/work/aoc20/inputs/day19.in.test')
# print(part1(testRules, testMessages))


# rules, messages = parseFile(
#     '/Users/irfan/work/aoc20/inputs/day19.in')
# print(part1(rules, messages))


###########################################
# PART 2
# some rules are infinitely repeatable:
# 0: 8 11
#          -> this means [42]{1,} [42]* [31]{1,}
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
rules, messages = parseFile(
    '/Users/irfan/work/aoc20/inputs/day19.in')
possibleStringsFor42 = expandRule(rules[42], rules)
possibleStringsFor31 = expandRule(rules[31], rules)


print(f"min: {min([len(x) for x in possibleStringsFor42])}, max {max([len(x) for x in possibleStringsFor42])}")
print(f"min: {min([len(x) for x in possibleStringsFor31])}, max {max([len(x) for x in possibleStringsFor31])}")
# Since my rule 0 is 8 then 11... my actual rule is:
# strings that start with any valid 42 any number of times, (at least once)
# followed by strings that contain one of 42, then any number of 31s
# All allowed options are exactly 8 characters wide. Therefor valid messages must be a multiple of this


def testPart2(message, startStrings, endStrings):
    # split string into 8 character chunks:
    n = len(startStrings[0])
    chunks = [message[i:i+n] for i in range(0, len(message), n)]
    if len(message) % n or len(chunks) < 3:
        return False
    checkEnds = False
    startCount = 0
    endCount = 0
    for c in chunks:
        if not checkEnds:
            isStart = c in startStrings
            if isStart:
                startCount += 1
                continue
            if not isStart:
                checkEnds = True
        if checkEnds:
            if c in endStrings:
                endCount += 1
            else:
                return False

    return startCount > 1 and endCount > 0 and endCount < startCount


possibleMessages = list(filter(lambda x: testPart2(
    x, possibleStringsFor42, possibleStringsFor31), messages))

print(len(possibleMessages))
