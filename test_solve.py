def readMaze(file_name):
    f = open(file_name)
    maze1 = f.read()
    f.close()
    return maze1

def convertMaze(maze1):
    cm = []
    lines = maze1.splitlines()
    for line in lines:
        cm.append(list(line))
    return cm

def print_maze(maze1):
    for row in maze1:
        for item in row:
            print(item, end="")
        print()

def start_point(maze1):
    for row in range(len(maze1)):
        for col in range(len(maze1[0])):
            if maze1[row][col] == '^':
                return row, col

def valid_position(maze1, y, x):
    if y < 0 or x < 0:
        return False     
    if y >= len(maze1) or x >= len(maze1[0]):
        return False
    if maze1[y][x] in ' E':
        return True
    return False

def solve(maze1, start, numberOfSteps):
    mazelist = []
    mazelist.append(start)
    while len(mazelist) > 0 :
        y, x = mazelist.pop() 
        if maze1[y][x] == 'E':
          print("Finish Line")
          return True
        if maze1[y][x] == 'X': #Already visited here
            continue
        maze1[y][x] = 'X'
        if valid_position(maze1, y - 1, x):
            mazelist.append((y - 1, x))
        if valid_position(maze1, y + 1, x):
            mazelist.append((y + 1, x))
        if valid_position(maze1, y, x - 1):
            mazelist.append((y, x - 1))
        if valid_position(maze1, y, x + 1):
            mazelist.append((y, x + 1))
        if len(mazelist) >= numberOfSteps:
            print(f'Cant solve this with number of steps {numberOfSteps}')
            break
        print('Mazelist:' , mazelist)
        print_maze(maze1)

    return False
    
maze1 = readMaze('.vscode\maze-task-first_(2).txt')
maze1 = convertMaze(maze1)
print_maze(maze1)
start = start_point(maze1)
print(start)
# numberOfSteps = input()
numberOfSteps = print(solve(maze1, start, 150)) #Set up any input number to calculate how many step this needs go trough the maze