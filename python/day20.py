import re
import math


def readFile(filename):
    with open(filename) as f:
        fileData = f.read().splitlines()
        data = {}
        for i in range(0, len(fileData), 12):
            tile = re.search('^Tile ([0-9]*):$', fileData[i])
            data[int(tile.group(1))] = fileData[i+1:i+11]
    return data


def rotateTile(tile):
    return list(map("".join, zip(*reversed(tile))))


def reflectTile(tile):
    return [x[::-1] for x in tile]


def getTilePossibleEdges(tile):
    # print(tile)
    edges = [tile[0], tile[9]]
    reflectedTile = reflectTile(tile)
    edges.append(reflectedTile[0])
    edges.append(reflectedTile[9])
    rotatedTile = rotateTile(tile)
    edges.append(rotatedTile[0])
    edges.append(rotatedTile[9])
    rotatedReflectedTile = reflectTile(rotatedTile)
    edges.append(rotatedReflectedTile[0])
    edges.append(rotatedReflectedTile[9])
    return edges


def matchingEdge(tile1, tile2):

    if tile1[0] == tile2[9] or tile2[0] == tile1[9]:
        return True
    return False


def checkIfEdgePiece(tile, otherTiles):
    edges = getTilePossibleEdges(tile)
    otherEdges = []
    for ot in otherTiles.values():
        otherEdges = otherEdges + getTilePossibleEdges(ot)

    edgeMatchCount = 0
    for e in edges:
        if e in otherEdges:
            edgeMatchCount += 1
    print(edgeMatchCount)
    return edgeMatchCount == 4


# print("\n".join(testFile[2311]))
# print()
# print("\n".join(rotateTile(testFile[2311])))
# print()
# print("\n".join(reflectTile(testFile[2311])))

# print(matchingEdge(testFile[2311], testFile[3079]))

def part1(fileData):
    edges = []
    for tileName, tile in fileData.items():
        print(f"checking {tileName}")
        if checkIfEdgePiece(tile, {k: v for k, v in fileData.items() if k not in [tileName]}):
            print(f" *** {tileName} ***")
            edges.append(tileName)
    return edges


testData = readFile('inputs/day20.in.test')
data = readFile('inputs/day20.in')
testAnswer = 20899048083289


print(f" Answer: {math.prod(part1(testData))}")
print(f" Answer: {math.prod(part1(data))}")
