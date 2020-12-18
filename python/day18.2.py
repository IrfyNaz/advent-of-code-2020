import operator
import re


def readFile(filename):
    with open(filename) as f:
        return [x.replace(' ', '') for x in f.read().splitlines()]


testInput = readFile('../inputs/day18.in.test')
input = readFile('../inputs/day18.in')

OPEN_PAREN = "("
CLOSE_PAREN = ")"

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor
}


def processLine(input):
    value = 0
    # First collapse any paranthesis:
    input = re.split(r'(\D)', "".join(input))
    input = list(filter(None, input))

    while OPEN_PAREN in input:
        startIdx = input.index(OPEN_PAREN)
        endIdx = len(input)
        openParen = 0
        for i in range(startIdx + 1, endIdx):
            curVal = input[i]
            if curVal == OPEN_PAREN:
                openParen += 1
            elif openParen == 0 and curVal == CLOSE_PAREN:
                endIdx = i
                break
            elif curVal == CLOSE_PAREN:
                openParen -= 1
        replacementValue = processLine(input[startIdx+1:endIdx])
        newInput = []
        if startIdx > 0:
            newInput = input[0:startIdx]
        newInput = newInput + [f"{replacementValue}"]
        if endIdx < len(input) - 1:
            newInput = newInput + input[endIdx+1:]
        input = newInput

    # process '+' first!
    while "+" in input:
        idx = input.index("+")
        newValue = int(input[idx - 1]) + int(input[idx + 1])
        newInput = []
        if(idx > 2):
            newInput = input[:idx-1]
        newInput += [newValue]
        if(idx < len(input) - 1):
            newInput += input[idx+2:]
        input = newInput

    curOp = ops['+']
    value = int(input[0])
    for i in range(1, len(input)):
        curVal = input[i]
        if curVal in ops.keys():
            curOp = ops[curVal]
        else:
            print(f"{value} => {curOp} => {curVal} => {i}")
            value = curOp(value, int(curVal))

    return value


def part1(inputs):
    outputs = []
    for line in inputs:
        print(f"******Processing new line | {line}")
        outputs.append(processLine(line))
    return outputs


print(part1(testInput))
print(sum(part1(input)))
