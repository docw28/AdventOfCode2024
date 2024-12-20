testInput1 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""" # solution is 18

def ingest(inputString):
    inputList = []
    ingestedString = []

    inputList = inputString.split("\n")
    for line in inputList:
        ingestedString.append(list(line))
        print(list(line))
    return ingestedString

def wordSearch(array, string):
    total = 0
    for line in array:
        print("\n", end="")
        for char in line:
            if char == string[0]:
                print("ding", end="")
    # look for each instance of the starting character
    # check each direction for the next character
    # if found, check the same direction for the next character
    return total

def ceresSearch(puzzleInput, string):
    puzzleInput = ingest(puzzleInput)
    answer = wordSearch(puzzleInput, string)
    return answer

print(ceresSearch(testInput1, "XMAS"))
