import re
import copy
import collections

# How to layout a Hexgrid using a normal array:
#   https://www.redblobgames.com/grids/hexagons/

WHITE = False
BLACK = True

def readFile(filename):
    with open(filename) as f:
        fileData = f.read().splitlines()
        lines = []
        for line in fileData:
            lines.append([x for x in filter(lambda x: x != "", re.split('(se|sw|ne|nw|e|w)', line))])
    return lines

directionMap = {
  'ne': lambda x, y, z: [x+1, y, z-1],
  'e': lambda x, y, z: [x+1, y-1, z],
  'se': lambda x, y, z: [x, y-1, z+1],
  'sw': lambda x, y, z: [x-1, y, z+1],
  'w': lambda x, y, z: [x-1, y+1, z],
  'nw': lambda x, y, z: [x, y+1, z-1]
}

def getDim(grid):
  return len(grid.keys()) # the maximum size of our hexagonal grid

def getStartGrid(instructions):
  grid = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(lambda: False)))
  return(grid)

def countBlack(grid):
  count = 0
  for x in grid.values():
    for y in x.values():
      for z in y.values():
          count += z
  return count

def part1(instructions, startGrid):
  grid = copy.deepcopy(startGrid)
  for instruction in instructions:
    x, y, z = 0, 0, 0
    for step in instruction:
      x, y, z = directionMap[step](x, y, z)
    # print(f"Toggling = {x} {y} {z}: {grid[x][y][z]} -> {not grid[x][y][z]}")
    grid[x][y][z] = not grid[x][y][z]
  
  return grid

testData = readFile('inputs/day24.in.test')
testA = part1(testData, getStartGrid(testData))
print(countBlack(testA))

data = readFile('inputs/day24.in')
dataA = part1(data, getStartGrid(data))
print(countBlack(dataA))


def getAdjacentBlackCells(cx, cy, cz, grid):
  count = 0
  # print(f" {cx} {cy} {cz} {getDim(grid)}")
  for k, d in directionMap.items():
    x, y, z = d(cx, cy, cz)
    # print(f"    {x} {y} {z} => {grid[x][y][z]} + {count}")
    count += grid[x][y][z]
  return count

flatten = lambda t: [item for sublist in t for item in sublist]

def getPossibleCoordinates(grid):
    xs = list(grid.keys())
    ys = list(set(flatten([y.keys() for y in grid.values()])))
    zs = []
    for x, yv in grid.items():
      for y, zv in yv.items():
        for z, v in zv.items():
          zs.append(z)
    zs = list(set(zs))
    return [xs, ys, zs] 

def part2(instructions, iterations):
  curGrid = part1(instructions, getStartGrid(instructions))
  for i in range(iterations):
    nextGrid = copy.deepcopy(curGrid)
    checkGrid = copy.deepcopy(curGrid)

    xs, ys, zs = getPossibleCoordinates(curGrid)

    for x in range(min(xs)-2, max(xs) + 3):
      for y in range(min(ys)-2, max(ys) + 3):
        for z in range(min(zs)-2, max(zs)+3):
          count = getAdjacentBlackCells(x, y, z, checkGrid)
          if checkGrid[x][y][z] == WHITE and count == 2:
            nextGrid[x][y][z] = BLACK
          elif checkGrid[x][y][z] == BLACK and (count == 0 or count > 2):
            nextGrid[x][y][z] = WHITE

    curGrid = copy.deepcopy(nextGrid)
    print(f"iteration {i+1}: {countBlack(nextGrid)}")
  return curGrid


ans2t = part2(testData, 100)
print(countBlack(ans2t))

ans2 = part2(data, 100)
print(countBlack(ans2))