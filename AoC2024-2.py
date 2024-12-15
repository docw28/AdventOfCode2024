puzzleInput = str(open("day2input").read())

def isCorrectDirection(reading):
  if reading == sorted(reading) or reading == sorted(reading, reverse=True):
    return True
  else:
    return False

def isLowChange(reading):
  for i in range(1, len(reading)):
    difference = reading[i] - reading[i-1]
    if difference == 0 or abs(difference) > 3:
      return False
  return True

# split the input into a 2D array so it can be iterated easily
puzzleInput = puzzleInput.split("\n")
puzzleInput.pop()
for i in range(len(puzzleInput)):
  puzzleInput[i] = puzzleInput[i].split(" ")
  for j in range(len(puzzleInput[i])):
    puzzleInput[i][j] = int(puzzleInput[i][j])

safe = 0
for x in puzzleInput:
  print(x)
  if isCorrectDirection(x) and isLowChange(x):
    safe += 1
  
print("\nTotal = ", safe)
