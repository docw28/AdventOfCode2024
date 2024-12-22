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

puzzleInput = str(open("day4input").read())

vectors = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

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
    for i in range(len(array)):
        print("\n", end="")
        for j in range(len(array[i])):
            if array[i][j] == string[0]: # string is "XMAS"
                print("-", end="")
                for vector in vectors:
                    maxI = i + (vector[0] * ((len(string))-1))
                    maxJ = j + (vector[1] * ((len(string))-1))
                    print(maxI,maxJ)
                    if (0 <= maxI < len(array)) and (0 <= maxJ < len(array[i])):
                      check = ""
                      for c in range(len(string)):
                          check += array[i+(vector[0]*c)][j+(vector[1]*c)]
                      print(",", check, end="")
                      if check == string:
                          total += 1
    return total

def ceresSearch(Input, string):
    Input = ingest(Input)
    answer = wordSearch(Input, string)
    return answer

print("\n", ceresSearch(testInput1, "XMAS"))
print("\n", ceresSearch(puzzleInput, "XMAS"))

