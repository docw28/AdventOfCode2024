import time
puzzleInput = """3   4
4   3
2   5
1   3
3   9
3   3"""
listA = []
listB = []
totalDistance = 0
distanceTime = 0
similarityScore = 0
similarityTime = 0


puzzleInput = puzzleInput.split("\n")

for pair in puzzleInput:
    pair = pair.split("   ")
    listA.append(int(pair[0]))
    listB.append(int(pair[1]))
    
listA = sorted(listA)
listB = sorted(listB)
# print(listA, listB)

t = time.time()
i = 0
while i < len(listA):
    totalDistance += abs(listA[i] - listB[i])
    i += 1
distanceTime = time.time() - t
    
t = time.time()
for x in listA:
    for y in listB:
        if x == y:
            similarityScore += x
similarityTime = time.time() - t
    

print("Total distance = ", totalDistance, ", Time = ", distanceTime)
print("similarityScore = ", similarityScore, ", Time = ", similarityTime)