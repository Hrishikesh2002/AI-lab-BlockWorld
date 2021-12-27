class Block:

    def __init__(self, name):
        self.name = name
        self.goalStack = None
        self.goalLevel = None


BlockWorld = []

def ParseInput(fileName):
    input = open(fileName)
    
    status = 'input'
    
    x = 0
    for line in input:
        if (status == 'input'):
            if (len(line) != 1):
                Stack = []
                line = line.strip('\n')
                for char in line:
                    block = Block(char)
                    Stack.append(block)

                BlockWorld.append(Stack)
            else:
                status = 'output'
            
        elif (status == 'output'):
            line = line.strip('\n')
            y = 0
            for char in line:
                for Stack in BlockWorld:
                    for block in Stack:
                        if(block.name == char):
                            block.goalStack = x
                            block.goalLevel = y
                y += 1
            x += 1
                    
    BlockWorld.append([])

if __name__ == '__main__':
    ParseInput('input.txt')
    for Stack in BlockWorld:
        for block in Stack:
            print(block.name, block.goalStack, block.goalLevel)