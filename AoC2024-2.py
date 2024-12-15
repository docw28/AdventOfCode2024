puzzleInput = str(open("day2input").read())

def isCorrectDirection(reading): # checks for change in direction
  if reading == sorted(reading) or reading == sorted(reading, reverse=True):
    return True
  else:
    return False

def isLowChange(reading): # checks for large changes
  for i in range(1, len(reading)):
    difference = reading[i] - reading[i-1]
    if difference == 0 or abs(difference) > 3:
      return False
  return True

def problemDampener(reading): # checks to see if removing a value would make a reading safe
    print(reading)
    for i in range(len(reading)):
        temp = list(reading)
        temp.pop(i)
        if isCorrectDirection(temp) and isLowChange(temp):
            return True
    return False 
    
# split the input into a 2D array so it can be iterated easily
puzzleInput = puzzleInput.split("\n")
puzzleInput.pop() # pop because splitting by newline adds a blank string at the end of array
for i in range(len(puzzleInput)):
  puzzleInput[i] = puzzleInput[i].split(" ")
  for j in range(len(puzzleInput[i])):
    puzzleInput[i][j] = int(puzzleInput[i][j])

safe = 0
dampenable = 0
for x in puzzleInput:
  if isCorrectDirection(x) and isLowChange(x):
    safe += 1
  elif problemDampener(x):
      dampenable += 1
  
print("Inital Safe Total = ", safe)
print("Total Safe after Dampening = ", dampenable + safe)
