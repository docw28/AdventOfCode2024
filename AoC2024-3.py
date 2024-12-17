testInput = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

validChars = ["m", "u", "l", "(", ")", ",", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
puzzleInput = testInput

def removeInvalidChars(inputList):
    validList = []
    inputList = list(inputList)
    for char in inputList:
        if char in validChars:
            validList.append(char)
    validList = "".join(validList)
    return validList

print(removeInvalidChars(puzzleInput))




