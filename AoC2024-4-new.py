testInput1 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""" # solution 1 is 18, solution 2 is 9

def ingest(inputString):
    # converts a string with linebreaks into a 2D array
    inputList = []
    ingestedString = []

    inputList = inputString.split("\n")
    for line in inputList:
        ingestedString.append(list(line))
        print(list(line))
    return ingestedString

def weFindAnyChar(gridOfLetters, desiredChar):
    # returns a list of every location of that character in a 2D array
    coOrds = []
    for l in range(len(gridOfLetters)):
        for c in range(len(gridOfLetters[l])):
            if gridOfLetters[l][c] == desiredChar:
                coOrds.append([l,c])
    return coOrds

def wordSearch(inputString, desiredWord):
    vectors = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    starters = weFindAnyChar(ingest(inputString), desiredWord[0])
    for position in starters:
        for vector in vectors:

    return 

def crossSearch():
    return

print(wordSearch(testInput1, "XMAS"))
