import heapq
import copy
BlockDict = {}
explored = []
frontier = []
goalObject = None

class Block:
    def __init__(self, name):
        self.name = name
        self.goalStack = None
        self.goalLevel = None
        self.down = None

class BlockWorld:

    def __init__(self, state, move = None, parent = None):
        self.state = state
        self.move = move
        self.parent = parent

    def __lt__(self, other):
        return self.state < other.state

def Manhattan(state):
    heuristic = 0

    for Stack in state:
        for char in Stack:
            block = BlockDict[char]
            heuristic += abs(block.goalStack - state.index(Stack)) + abs(block.goalLevel - Stack.index(char))

    return heuristic

def Euclidean(state):
    heuristic = 0

    for Stack in state:
        for char in Stack:
            block = BlockDict[char]
            heuristic += (block.goalStack - state.index(Stack))**2 + (block.goalLevel - Stack.index(char))**2

    return heuristic

def ParseInput(fileName):
    blockWorld = BlockWorld([])
    input = open(fileName)
    
    status = 'input'
    
    x = 0
    
    for line in input:
        if (status == 'input'):
            if (len(line) != 1):
                Stack = []
                line = line.strip('\n')
                for char in line:
                    Stack.append(char)

                blockWorld.state.append(Stack)
            else:
                status = 'output'
            
        elif (status == 'output'):
            line = line.strip('\n')
            y = 0
            for char in line:
                block = Block(char)
                block.goalStack = x
                block.goalLevel = y
                
                BlockDict[char] = block
                prevChar = char
                y += 1
            x += 1
        prevChar = None

    return blockWorld

def Explore(blockWorld, heuristic):
    global goalObject

    if (heuristic(blockWorld.state) == 0):
        goalObject = blockWorld
        return True

    for Stack in blockWorld.state:
        if(len(Stack)):
            for newStack in blockWorld.state:
                if newStack != Stack:
                    newBlockWorld = BlockWorld(copy.deepcopy(blockWorld.state), None, blockWorld)
                    block = newBlockWorld.state[blockWorld.state.index(Stack)].pop()
                    newBlockWorld.state[blockWorld.state.index(newStack)].append(block)
                    newBlockWorld.move = (block, blockWorld.state.index(Stack), blockWorld.state.index(newStack))

                    if (newBlockWorld.state not in [x.state for x in explored] and newBlockWorld.state not in [x[1].state for x in frontier]):
                        heapq.heappush(frontier, (heuristic(newBlockWorld.state), newBlockWorld))

    
    explored.append(blockWorld)
    return False

def Begin(blockWorld, Heuristic):
    goalFound = False
    heapq.heappush(frontier, (Heuristic(blockWorld.state), blockWorld))
    
    while(len(frontier) and not goalFound):
        toExplore = heapq.heappop(frontier)
        goalFound = Explore(toExplore[1], Heuristic)

    if (goalFound):
        print("Goal Found!")
    elif (len(frontier) == 0):
        print("Frontier Empty!")

def printOutput():
    global goalObject

    if (goalObject == None):
        print("No Solution!")
        return

    print("Solution:")
    current = goalObject
    path = []
    while(current != None):
        path.insert(0,current)
        current = current.parent

    isNotFirst = False

    for x in path:
        if (isNotFirst):
            print(f"Move block {x.move[0]} from Stack {x.move[1]} to Stack {x.move[2]} ")
        else:
            isNotFirst = True
        for stack in x.state:
            for block in stack:
                print(block, end='')
            print()

    print(f"States Explored: {len(explored)}")
    print(f"Length of Path: {len(path)}")

if __name__ == '__main__':
    blockWorld = ParseInput('input.txt')
    Begin(blockWorld, Manhattan)
    printOutput()