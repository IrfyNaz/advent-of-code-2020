with open("day2.in") as f:
    lines = f.read().splitlines()


def checkPart1Rule(min, max, rule, password):
    characterCheck = password.count(rule)
    if(min <= characterCheck and max >= characterCheck):
        return True
    return False


def checkPart2Rule(min, max, rule, password):
    minCheck = password[min-1] == rule
    maxCheck = password[max-1] == rule
    if(minCheck + maxCheck == 1):
        return True
    return False


valid = 0
for line in lines:
    range, rule, password = line.replace(':', '').split(' ')
    min, max = [int(x) for x in range.split('-')]
    valid += checkPart1Rule(min, max, rule, password)

print(valid)


valid = 0
for line in lines:
    range, rule, password = line.replace(':', '').split(' ')
    min, max = [int(x) for x in range.split('-')]
    valid += checkPart2Rule(min, max, rule, password)

print(valid)
