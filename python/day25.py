def readFile(filename):
  with open(filename) as f:
      lines = f.read().splitlines()
      return {'card': int(lines[0]), 'door': int(lines[1])}

def getLoopSize(publicKey):
  i = 0
  value = 1
  sn = 7
  while value != publicKey:
    i += 1
    value = value * sn
    value = value % 20201227
  return i

def getEncryptionKey(subjectNumber, loopSize):
  value = 1
  for i in range(loopSize):
    value = value * subjectNumber
    value = value % 20201227
  return value

def part1(file):
  keys = readFile(file)

  snC = keys['card']
  snD = keys['door']

  loopC = getLoopSize(snC)
  loopD = getLoopSize(snD)

  return getEncryptionKey(snC, loopD)

print(part1('inputs/day25.in.test'))
print(part1('inputs/day25.in'))