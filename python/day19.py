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
    count = 0
    for message in messages:
        if message in possibleMessages:
            count += 1
    return count


testRules, testMessages = parseFile(
    '/Users/irfan/work/aoc20/inputs/day19.in.test')
print(part1(testRules, testMessages))


rules, messages = parseFile(
    '/Users/irfan/work/aoc20/inputs/day19.in')
print(part1(rules, messages))


# testFile = readFile('../inputs/day19.in.test')
# realFile = readFile('../inputs/day19.in')
