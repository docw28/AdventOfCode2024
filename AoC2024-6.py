import time

testInput1 = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

puzzleInput = str(open("day6input").read().strip())

directions = {"^":[-1,0], ">":[0,1], "v":[1,0], "<":[0,-1]}
rotations = {"^":">", ">":"v", "v":"<", "<":"^"}
def ingest(x): # where x is the puzzle input
    x = x.split("\n")
    for i in range(len(x)):
        print(x[i])
        x[i] = [char for char in x[i]] 
    return x

def step(grid, pos): # iterate on the current state of the grid
    # time.sleep(0.05)
    vector = directions[grid[pos[0]][pos[1]]]
    nextPos = [pos[0]+vector[0],pos[1]+vector[1]]
    insideGrid = True
    #if nextPos is out of range, pos = "X", return
    if (nextPos[0]<0) or (nextPos[0]>=len(grid)) or (nextPos[1]<0) or (nextPos[1]>=len(grid[0])):
        grid[pos[0]][pos[1]] = "X"
        insideGrid = False
    elif grid[nextPos[0]][nextPos[1]] != "#":
        grid[nextPos[0]][nextPos[1]] = grid[pos[0]][pos[1]]
        grid[pos[0]][pos[1]] = "X"
    else:
        grid[pos[0]][pos[1]] = rotations[grid[pos[0]][pos[1]]] 
    #for line in grid:
        #print(line)
    return [grid, insideGrid]

def guardGallivant(grid):
    thing = []
    pos = []
    uniquePositions = 0
    grid = ingest(grid)
    insideGrid = True

    while insideGrid:
        for i in range(len(grid)): # find current position
            for j in range(len(grid[i])):
                if grid[i][j] in ["^",">","v","<"]:
                    pos = [i,j]

        thing = step(grid, pos)
        grid = thing[0]
        insideGrid = thing[1]
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                uniquePositions += 1

    return uniquePositions
print(guardGallivant(puzzleInput))

# Next step: How many positions would add a loop if you placed an object there

# Identify loops. Visiting same place twice? Thrice? Making the same turn!
# Iterate over every instance of the map, with an object at every position
