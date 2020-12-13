from collections import defaultdict
from functools import reduce


def readFile(filename):
    with open(filename) as f:
        earliestTime, buses = f.read().splitlines()
        buses = buses.split(',')
        return [int(earliestTime), buses]


testEarliestTime, testBuses = readFile('../inputs/day13.in.test')
earliestTime, buses = readFile('../inputs/day13.in')


def part1(earliestTime, buses):
    print(earliestTime)
    # The maximum amount of time you have to wait will be x + lowest bus number. So you can simply mod earliest time and add to this.
    validBuses = filter(lambda x: x != 'x', buses)
    validBuses = [int(x) for x in validBuses]
    validBuses.sort()
    minBus = validBuses[0]
    maxTime = earliestTime + minBus
    times = defaultdict(lambda: [])
    for bus in validBuses:
        remainder = bus - (earliestTime % bus)
        times[remainder].append(bus)
        # print(f"{bus} -> {earliestTime} -> {remainder}")

    soonestBusTime = min(times)
    return soonestBusTime * times[soonestBusTime][0]


testDataAnswer = part1(testEarliestTime, testBuses)
print(
    f"    Test 1 part1 is: {testDataAnswer}")
dataAnswer = part1(earliestTime, buses)
print(
    f"Answer Part 1 is: {dataAnswer}")

print("********************************************************")


# https://math.stackexchange.com/questions/2612036/how-to-combine-congruences
# https://mathworld.wolfram.com/Congruence.html
# https://www.youtube.com/watch?app=desktop&v=zIFehsBHB8o  <- Chinese
# https://www.youtube.com/watch?v=ru7mWZJlRQg

def part2(buses):
    validBuses = filter(lambda x: x != 'x', buses)
    n = [int(x) for x in validBuses]
    a = []
    for i in range(0, len(buses)):
        if buses[i] != 'x':
            a.append(int(buses[i]) - i)

    return chinese_remainder(n, a)


# def findLowestCommonMultiplier(x):
#     lcm = x[0]
#     for i in x[1:]:
#         lcm = lcm*i//gcd(lcm, i)
#     return lcm


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


tests = [[[17, 'x', 13, 19], 3417],
         [[67, 7, 59, 61], 754018],
         [[67, 'x', 7, 59, 61], 779210],
         [[67, 7, 'x', 59, 61], 1261476],
         [[1789, 37, 47, 1889], 1202161486],
         [[7, 13, 'x', 'x', 59, 'x', 31, 19], 1068788]]


print(part2([17, 'x', 13, 19]))

# Check if tests pass:
print("Running tests")
for test in tests:
    print(f"      {test[1] == part2(test[0])}")


testDataAnswer = part2(testBuses)
print(
    f"    Test 1 part2 is: {testDataAnswer}")


dataAnswer = part2(buses)
print(
    f"Answer Part 2 is: {dataAnswer}")
