# Find three numbers that add together to sum to 2020.
# Then return the answer when they are multiplied together

with open("day1.in") as f:
    numbers = [int(x) for x in f.readlines()]

target = 2020
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                answer = numbers[i] * numbers[j] * numbers[k]
                print("Answer = {}".format(answer))
                break

print('Done')
