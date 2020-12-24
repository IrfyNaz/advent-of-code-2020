import re
# How to layout a Hexgrid using a normal array:
#   https://www.redblobgames.com/grids/hexagons/

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


def part1(instructions):
  dim = max([len(i) for i in instructions]) * 2 # the maximum size of our hexagonal grid
  grid = [[[False for i in range(dim)] for j in range(dim)] for x in range(dim)]
  for instruction in instructions:
    x, y, z = int(dim/2), int(dim/2), int(dim/2)
    for step in instruction:
      x, y, z = directionMap[step](x, y, z)
    # print(f"Toggling = {x} {y} {z}: {grid[x][y][z]} -> {not grid[x][y][z]}")
    grid[x][y][z] = not grid[x][y][z]
  
  count = 0
  for x in range(dim):
    for y in range(dim):
      for z in range(dim):
        if grid[x][y][z]:
          # print(f"{x} {y} {z}")
          count += 1
  return count

testData = readFile('inputs/day24.in.test')
testA = part1(testData)
print(testA)

testData = readFile('inputs/day24.in')
testA = part1(testData)
print(testA)
