import re

testInput = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

puzzleInput = str(open("day3input").read())

def extractInstructions(string):
    pattern = r"mul\(\d+,\d+\)"
    instructions = re.findall(pattern, puzzleInput)
    return instructions

def numsFromInstructions(instructions):
    for i in range(len(instructions)):
        instructions[i] = (instructions[i][4:-1]).split(",")
    return instructions

def executeInstructions(garbledInstructions):
    total = 0
    instructions = extractInstructions(garbledInstructions)
    nums = numsFromInstructions(instructions)
    for pair in nums:
        total += int(pair[0]) * int(pair[1])
    return total

print(executeInstructions(puzzleInput))
