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
def ingest(x): # where x is the puzzle input
    x = x.split("\n")
    for line in x:
        print(line)
        line = line.split()
    return x

def step(grid, pos): # iterate on the current state of the grid
    vector = directions[grid[pos[0]][pos[1]]]
    print(vector)
    nextPos = [pos[0]+vector[0],pos[1]+vector[1]]
    print(pos, nextPos, grid[nextPos[0]][nextPos[1]] == ".")
    if grid[nextPos[0]][nextPos[1]] == ".":
        grid[nextPos[0]][nexPost[1]] = grid[pos[0]][pos[1]]

    return grid

def guardGallivant(grid):
    pos = []
    uniquePositions = 0
    grid = ingest(grid)

    for i in range(len(grid)): # find starting position
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                pos = [i,j]
                
    grid = step(grid, pos)
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                uniquePositions += 1

    return uniquePositions
print(guardGallivant(testInput1))
