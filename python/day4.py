import re


def convertRowToDictionary(row):
    return {x.split(':')[0]: x.split(':')[1] for x in row.split(' ')}


def getData(file):
    with open(file) as f:
        data = [x.replace('\n', ' ') for x in re.split('[\r\n]{2,}', f.read())]
        return [convertRowToDictionary(row) for row in data]


def checkDocuments(doc, keys):
    return not (set(keys) - doc.keys())


def part1(documents, mandatoryKeys):
    validDocuments = [checkDocuments(x, mandatoryKeys) for x in documents]
    return validDocuments


def validateHeight(height):
    valid = False
    if (re.match('^(\d+)cm$', height)):
        heightInt = int(height[:-2])
        valid = heightInt >= 150 and heightInt <= 193
    elif (re.match('^(\d+)in$', height)):
        heightInt = int(height[:-2])
        valid = heightInt >= 59 and heightInt <= 76
    return valid


mandatoryFields = {
    'byr': lambda x: re.match('^[0-9]{4}', x) and int(x) >= 1920 and int(x) <= 2002,
    'iyr': lambda x: re.match('^[0-9]{4}', x) and int(x) >= 2010 and int(x) <= 2020,
    'eyr': lambda x: re.match('^[0-9]{4}', x) and int(x) >= 2020 and int(x) <= 2030,
    'hgt': lambda x: validateHeight(x),
    'hcl': lambda x: bool(re.match('^#[a-z0-9]{6}$', x)),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: bool(re.match('^[0-9]{9}$', x))
}

optionalKeys = ['cid']


def part2(documents, mandatoryFields):
    validDocuments = filter(lambda x: checkDocuments(
        x, mandatoryFields.keys()), documents)
    return sum([all([test(document[k]) for k, test in mandatoryFields.items()]) for document in validDocuments])


# Part 1
print(sum(part1(getData('../inputs/day4.in.test'), mandatoryFields.keys())))
print(sum(part1(getData('../inputs/day4.in'),  mandatoryFields.keys())))

# Part 2
print(part2(getData('../inputs/day4.in.test'), mandatoryFields))
print(part2(getData('../inputs/day4-2-bad.in.test'), mandatoryFields))
print(part2(getData('../inputs/day4-2-good.in.test'), mandatoryFields))
print(part2(getData('../inputs/day4.in'), mandatoryFields))
