with open("day2.in") as f:
    data = f.read().splitlines()

with open('day2.in.test') as f:
    testData = f.read().splitlines()


def checkPart1Rule(min, max, rule, password):
    characterCheck = password.count(rule)
    if(min <= characterCheck and max >= characterCheck):
        return True
    return False


def checkPart2Rule(indexA, indexB, rule, password):
    aCheck = password[indexA-1] == rule
    bCheck = password[indexB-1] == rule
    if(aCheck + bCheck == 1):
        return True
    return False


def checkAnswer(lines, ruleFunction):
    valid = 0
    for line in lines:
        range, rule, password = line.replace(':', '').split(' ')
        a, b = [int(x) for x in range.split('-')]
        valid += ruleFunction(a, b, rule, password)

    print(valid)


checkAnswer(testData, checkPart1Rule)
checkAnswer(data, checkPart1Rule)
checkAnswer(testData, checkPart2Rule)
checkAnswer(data, checkPart2Rule)
