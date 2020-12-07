import re


def readRules(file):
    with open(file) as f:
        lines = f.read().splitlines()
        return {x.split(' bags contain ')[0]: parseInnerRule(x.split(' contain ')[1]) for x in lines}


def parseInnerRule(rule):
    regex = "(\d+) ([a-z ]*) bag[s,.]{1,2}"
    return({x: y for y, x in re.findall(regex, rule)})


def part1(rules, bagType):
    containerBags = []
    for key, rule in rules.items():
        if(bagType in rule.keys()):
            containerBags.append(key)
            containerBags.extend(part1(rules, key))

    return set(containerBags)


def part2(rules, bagType, includeContainerBag):
    counter = includeContainerBag
    for key, times in rules[bagType].items():
        counter += int(times) * part2(rules, key, 1)
    return counter


testData = readRules('../inputs/day7.in.test')
testData2 = readRules('../inputs/day7.in.test2')
print(len(part1(testData, 'shiny gold')))

data = readRules('../inputs/day7.in')
print("The answer to part 1 is: {}".format(len(part1(data, 'shiny gold'))))

print("part 2 test data: {}".format(part2(testData, 'shiny gold', 0)))
print("part 2 test data: {}".format(part2(testData2, 'shiny gold', 0)))
print("The answer to part 2 is: {}".format(part2(data, 'shiny gold', 0)))
