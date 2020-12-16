import operator


def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read().split(',')]


testInput = readFile('../inputs/day15.in.test')
input = readFile('../inputs/day15.in')

iterations = 2020


def part1(data, iterations):
    values = {k: v+1 for v, k in enumerate(data[:-1])}
    print(values)
    newValue = data[-1]
    for i in range(len(data), iterations):
        if newValue in values.keys():
            nextNewValue = i - values[newValue]
        else:
            nextNewValue = 0
        values[newValue] = i
        newValue = nextNewValue
        # print(f"{i+1} {newValue}")

    return newValue


testDataAnswer = part1(testInput, iterations)
print(f"    Test 1 part1 is: {testDataAnswer}")

dataAnswer = part1(input, iterations)
print(f"part1 is: {dataAnswer}")

print("********************************************************")


iterations = 30000000

# testDataAnswer = print(f"  part 2 test answer: {part1(testInput, iterations)}")
# testDataAnswer = print(f"  part 2 test answer: {part1([1,3,2], iterations)}")
# testDataAnswer = print(f"  part 2 test answer: {part1([2,1,3], iterations)}")
# testDataAnswer = print(f"  part 2 test answer: {part1([1,2,3], iterations)}")
# testDataAnswer = print(f"  part 2 test answer: {part1([2,3,1], iterations)}")
# testDataAnswer = print(f"  part 2 test answer: {part1([3,2,1], iterations)}")
# testDataAnswer = print(f"  part 2 test answer: {part1([3,1,2], iterations)}")

dataAnswer = part1(input, iterations)
print(f"part2 is: {dataAnswer}")
