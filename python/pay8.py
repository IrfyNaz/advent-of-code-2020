
def readFile(filename):
    with open(filename) as f:
        return [[x[:3], int(x[3:])] for x in f.read().splitlines()]


testData = readFile('../inputs/day8.in.test')
data = readFile('../inputs/day8.in')

instructionMap = {
    'acc': lambda a, i, ins: [a + ins, i+1],
    'nop': lambda a, i, ins: [a, i+1],
    'jmp': lambda a, i, ins: [a, i + ins]
}


def part1(data):
    acc = 0
    visited = []
    i = 0
    while i not in visited and i < len(data):
        instruction, value = data[i]
        new_acc, new_i = instructionMap[instruction](acc, i, value)
        visited.append(i)
        if(new_i in visited):
            print('stuck in a loop')
            break
        elif(new_i >= len(data)):
            print('completed')
            acc = new_acc
            break
        else:
            acc = new_acc
            i = new_i
    return([i + 1, acc])


print("Test part1 is: {}".format(part1(testData)))
print("The answer to part1 is: {}".format(part1(data)))


# Modify one nop -> jmp OR one jmp -> nop
def part2(data):
    for i in range(0, len(data)):
        new_data = data.copy()
        instruction, value = new_data[i]
        # can the line be modified?
        if instruction == 'jmp':
            new_data[i] = ['nop', value]
        elif instruction == 'nop':
            new_data[i] = ['jmp', value]
        [check, acc] = part1(new_data)
        if check >= len(data):
            return acc


print("Test part2 is: {}".format(part2(testData)))
print("The answer to part2 is: {}".format(part2(data)))
