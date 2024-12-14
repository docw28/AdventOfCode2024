

puzzleInput = str(open("day1input").read())

listA = []
listB = []
totalDistance = 0


puzzleInput = puzzleInput.split("\n")
puzzleInput.pop()

for pair in puzzleInput:
    pair = pair.split("   ")
    listA.append(pair[0])
    listB.append(pair[1])
    
listA = sorted(listA)
listB = sorted(listB)
print(listA, listB)

i = 0
while i < len(listA):
    totalDistance += abs(int(listA[i]) - int(listB[i]))
    i += 1

print(totalDistance)
