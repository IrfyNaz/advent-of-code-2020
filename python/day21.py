import re
import collections
import itertools
import copy


def readFile(filename):
    with open(filename) as f:
        fileData = f.read().splitlines()
        lines = []
        for line in fileData:
            splitPoint = line.index('(')
            allergens = line[splitPoint + 10:-1].split(', ')
            ingredients = line[:splitPoint-1].split(' ')
            lines.append([ingredients, allergens])
    return lines


def part1(lists):
    # allergens = set(itertools.chain(*[a for i, a in lists]))
    allergens = collections.defaultdict(lambda: list())
    for ingres, allers in lists:
        for a in allers:
            allergens[a].append(set(ingres))

    confirmed = {}
    while len(confirmed) != len(allergens):
        for k, v in allergens.items():
            options = v[0].intersection(*v)
            if len(options) == 1:
                value = options.pop()
                confirmed[k] = value
                for a in allergens.values():
                    for v in a:
                        print(v)
                        v.discard(value)

    allIngredients = list(itertools.chain(*[i for i, a in lists]))
    badCount = 0
    for v in confirmed.values():
        badCount += allIngredients.count(v)
    print(f"Part 1: {len(allIngredients) - badCount}")

    part2 = [confirmed[k] for k in sorted(confirmed)]
    print(f"Part 2: {','.join(part2)}")
    return(len(allIngredients) - badCount)


testData = readFile('inputs/day21.in.test')
print(part1(testData))

data = readFile('inputs/day21.in')
print(part1(data))
