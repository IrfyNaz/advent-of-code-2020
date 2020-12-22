import copy


def readFile(filename):
    with open(filename) as f:
        fileData = f.read().splitlines()
        p2idx = fileData.index('Player 2:')
        player1 = [int(x) for x in fileData[1:p2idx-1]]
        player2 = [int(x) for x in fileData[p2idx+1:]]

    return([player1, player2])


def part1(p1, p2):
    while(len(p1) > 0 and len(p2) > 0):
        x = p1.pop(0)
        y = p2.pop(0)
        if x > y:
            p1.extend([x, y])
        else:
            p2.extend([y, x])
    return p1 + p2


def getScore(cards):
    score = sum([i * v for i, v in enumerate(cards[::-1], start=1)])
    return score


test1, test2 = readFile('inputs/day22.in.test')
print(getScore(part1(test1, test2)))

player1, player2 = readFile('inputs/day22.in')
print(getScore(part1(player1, player2)))


def part2(p1, p2):
    rounds = []
    i = 1
    while(len(p1) > 0 and len(p2) > 0):
        # print(f" Round {i} {p1} {p2}")
        # if game has occurred previous, end and p1 wins:
        if [p1, p2] in rounds:
            print(f'Recursion detected, p1 wins {p1} {p2}')
            return [1, p1]
        rounds.append([copy.copy(p1), copy.copy(p2)])
        x = p1.pop(0)
        y = p2.pop(0)

        if x <= len(p1) and y <= len(p2):
            # recursive combat!
            winPlayer, winCards = part2(copy.copy(p1[:x]), copy.copy(p2[:y]))
        elif x > y:
            winPlayer = 1
        else:
            winPlayer = 2

        if winPlayer == 1:
            p1.extend([x, y])
        else:
            p2.extend([y, x])
        i += 1

    if len(p1) > 0:
        return [1, p1]
    return [2, p2]


test1, test2 = readFile('inputs/day22.in.test')
player, cards = part2(test1, test2)
print(getScore(cards))


player1, player2 = readFile('inputs/day22.in')
player, cards = part2(player1, player2)
print(getScore(cards))
