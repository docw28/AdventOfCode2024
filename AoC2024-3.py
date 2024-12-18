import re

testInput1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
testInput2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

puzzleInput = str(open("day3input").read())

def extractInstructions(string, withDo): # withDo True if you want "do()" and "don't()" detected
    if withDo:
        pattern = r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)"
    else:
        pattern = r"mul\(\d+,\d+\)"
    instructions = re.findall(pattern, string)
    return instructions

def numsFromInstructions(instructions):
    nums = []
    do = True
    for instruction in instructions:
        if instruction == "do()":
            do = True
        elif instruction == "don't()":
            do = False
        elif do == True:
            nums.append(instruction[4:-1].split(","))
    return nums

def multiplyNums(nums):
    total = 0
    for num in nums:
        total += int(num[0]) * int(num[1])
    return total

def mullItOver(string, withDo):
    instructions = extractInstructions(string, withDo)
    nums = numsFromInstructions(instructions)
    return multiplyNums(nums)

print(mullItOver(puzzleInput, False))
print(mullItOver(puzzleInput, True))

