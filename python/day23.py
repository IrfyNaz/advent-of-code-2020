import numpy as np
import datetime

def readFile(filename):
    with open(filename) as f:
        return [int(x) for x in f.read()]


def part1(numbers, moves):
    i = 0
    dim = len(numbers)
    print(dim)
    while(moves > 0):
        curMove = numbers[i % dim]
        print(f"{moves} | cups: {numbers} => {curMove}")
        indicesToRemove = [(i+1) % dim, (i+2) % dim, (i+3) % dim]
        numbersToRemove = [numbers[x] for x in indicesToRemove]
        print(f"{moves} | pick up: {numbersToRemove}")
        [numbers.remove(x) for x in numbersToRemove]
        # Find where to insert them back!
        x = curMove - 1
        while x not in numbers:
            x -= 1
            if (x < 1):
                x = max(numbers)
        print(f"{moves} | destination: {x}")
        x = numbers.index(x)
        numbers[x+1:x+1] = numbersToRemove
        # Rearrange so that curMove is still at its original position (i)
        newIndex = numbers.index(curMove)
        if newIndex > i % dim:
            if moves == 3:
                print("Irfan")
            print('  shifting left')
            print(f"  {numbers}")
            shift = newIndex - i % dim
            numbers = numbers[shift:] + numbers[:shift]
            print(f"  {numbers}")
        elif newIndex < i % dim:
            print('  shifting right')
            print(f"  {numbers}")
            shift = i % dim - newIndex
            numbers = numbers[:-shift] + numbers[:dim - shift]
            print(f"  {numbers}")
        print()
        i += 1
        moves -= 1

    return numbers


testData = readFile('../inputs/day23.in.test')
data = readFile('../inputs/day23.in')

# print(part1(testData, 100))
# print(part1(data, 100))


def part2attempt1(numbers, maxNum, moves):
    numbers = np.array(numbers + list(range(max(numbers)+1, maxNum+1)))
    dim = len(numbers)
    idx = 0
    while moves > 0:
        # print(numbers)
        valAtIdx = numbers[idx % maxNum]
        picked = np.take(numbers, range(idx+1, idx+4), mode='wrap')
        indicesToRemove = np.isin(numbers, picked)
        numbers = np.delete(numbers, indicesToRemove)

        insertionVal = valAtIdx - 1
        if insertionVal < 1:
            insertionVal = maxNum
        while insertionVal in picked:
            insertionVal -= 1
            if(insertionVal < 1):
                insertionVal = maxNum
        # print(
        #     f"   numbers: {numbers}, insertionVal: {insertionVal}, picked: {picked}")
        insertionIdx = np.where(numbers == insertionVal)[0][0]
        # print(f"   inserting at {insertionIdx}")
        numbers = np.insert(numbers, (insertionIdx + 1) % maxNum, picked)

        newIdx = np.where(numbers == valAtIdx)[0][0]
        # print(f"   {idx} -> {newIdx} ({numbers})")
        numbers = np.roll(numbers, idx - newIdx)
        idx = (idx + 1) % dim
        moves -= 1
        if moves % 10000 == 0:
            print(moves)
    return numbers

class Node:
    # Contains data
    # has a pointer to the next node
    # Do we need a link to the previous node? (single linked list vs double linked list)

    def __init__(self, value):
        self.value = value
        self.next = None
        return

    def __str__(self):
        return f'({self.previous != None}) {self.value} ({self.next != None})'
    
    def setNext(self, next):
        self.next = next
        next.previous = self

    def getNextItems(self, numberOfItems):
        values = []
        item = self.next
        for i in range(numberOfItems):
            values.append(item)
            item = item.next
        return values

class DoubleLinkedList:
    def __init__(self):
        "constructor to initiate this object"
        self.map = {}
        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        "add an item at the end of the list"

        if isinstance(item, Node):
            if self.head is None:
                self.head = item
                item.previous = item
                item.next = item
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item
                item.next = self.head
        if (item.value not in self.map.keys()):
            self.map[item.value] = item

        return    

    def insert_item_after_value(self, value, item):
        valueItem = self.map[value] 
        oldNext = self.map[value].next
        oldNext.previous = item
        valueItem.next = item
        item.previous = valueItem
        item.next = oldNext

        return

    def insert_item_chain_after_value(self, value, items):
        # remove the sequence from the linked list
        items[0].previous.next = items[-1].next
        items[-1].next.previous = items[0].previous

        valueItem = self.map[value] 
        oldNext = self.map[value].next
        valueItem.next = items[0]
        items[0].previous = valueItem
        items[-1].next = oldNext
        if oldNext == None:
            self.tail = items[-1]
        else:
            oldNext.previous = items[-1]
        
        return


def part2(numbers, maxNum, moves):
    myLL = DoubleLinkedList()
    [myLL.add_list_item(Node(x)) for x in numbers]
    [myLL.add_list_item(Node(x)) for x in range(max(numbers)+1, maxNum+1)]
    
    curNode = myLL.head
    print(curNode)
    while moves > 0:
        pickedNodes = curNode.getNextItems(3)
        pickedNodeValues = [n.value for n in pickedNodes]

        insertionVal = curNode.value - 1
        if insertionVal < 1:
            insertionVal = maxNum
        while insertionVal in pickedNodeValues:
            insertionVal -= 1
            if(insertionVal < 1):
                insertionVal = maxNum

        myLL.insert_item_chain_after_value(insertionVal, pickedNodes)
        curNode = curNode.next
        moves -= 1
        if moves % 1000000 == 0:
            print(moves)

    return myLL
    
results = part2(data, 1000000, 10000000)
nextTwo = results.map[1].getNextItems(2)
vals = [n.value for n in nextTwo]
print(vals[0] * vals[1])
