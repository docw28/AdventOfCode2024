import math

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

puzzleInput = str(open("day4input").read())

def ingest(inputString):
    # converts a string with linebreaks into a 2D array
    inputList = []
    ingestedString = []

    inputList = inputString.strip().split("\n")
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

def hasMAS(array, position):
    if (array[position[0]-1][position[1]-1] == "M") and (array[position[0]-1][position[1]+1] == "M") and (array[position[0]+1][position[1]+1] == "S") and (array[position[0]+1][position[1]-1] == "S"):
        return True
    if (array[position[0]-1][position[1]-1] == "S") and (array[position[0]-1][position[1]+1] == "M") and (array[position[0]+1][position[1]+1] == "M") and (array[position[0]+1][position[1]-1] == "S"):
        return True
    if (array[position[0]-1][position[1]-1] == "S") and (array[position[0]-1][position[1]+1] == "S") and (array[position[0]+1][position[1]+1] == "M") and (array[position[0]+1][position[1]-1] == "M"):
        return True
    if (array[position[0]-1][position[1]-1] == "M") and (array[position[0]-1][position[1]+1] == "S") and (array[position[0]+1][position[1]+1] == "S") and (array[position[0]+1][position[1]-1] == "M"):
        return True
    return False

def wordSearch(inputString, desiredWord):
    total = 0
    vectors = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    inputArray = ingest(inputString)
    starters = weFindAnyChar(inputArray, desiredWord[0])
    for position in starters:
        for vector in vectors:
            maxL = position[0] + (vector[0] * (len(desiredWord)-1))
            maxC = position[1] + (vector[1] * (len(desiredWord)-1))
            if (0 <= maxL < len(inputArray)) and (0 <= maxC < len(inputArray[position[0]])):
                check = ""
                for c in range(len(desiredWord)):
                    check += inputArray[position[0]+(vector[0]*c)][position[1]+(vector[1]*c)]
                if check == desiredWord:
                    total += 1
    return total

def crossSearch(inputString, desiredWord):
    total = 0
    test = []
    inputArray = ingest(inputString)
    starters = weFindAnyChar(inputArray, desiredWord[math.floor(len(desiredWord)/2)])
    for position in starters:
        if (1 <= position[0] < (len(inputArray)-1)) and (1 <= position[1] < (len(inputArray[position[0]])-1)) and hasMAS(inputArray, position):
            total += 1
    return total

# print(wordSearch(testInput1, "XMAS"))
# print(crossSearch(testInput1, "MAS"))
# print(wordSearch(puzzleInput, "XMAS"))
print(crossSearch(puzzleInput, "MAS"))
