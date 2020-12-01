

# Find two numbers that add together to sum to 2020.
# Then return the answer when they are multiplied together

with open("day1.in") as f:
    numbers = [int(x) for x in f.readlines()]

target = 2020
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print('Found it!')
            answer = numbers[i] * numbers[j]
            print("Answer = {}".format(answer))
            break

print('Done')
