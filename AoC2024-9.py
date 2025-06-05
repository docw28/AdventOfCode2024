testInput1 = "12345"
testInput2 = "2333133121414131402"
        
def decrypt(diskMap):
    output = []
    outputChar = "ID"
    ID = 0
    for number in diskMap:
        if outputChar == "ID":
            for i in range(int(number)):
                output.append(ID)
            ID += 1
            outputChar = "."
        elif outputChar == ".":        
            for i in range(int(number)):
                output.append(".")
            outputChar = "ID"
    return(output)
    
def defrag(decryptedMap):
    x = decryptedMap
    output = []
    for i in range(len(x)):
        print(*x)
        if x[len(x)-(i+1)] != ".":
            for j in range(len(x)):
                if x[j] == ".":
                    x[j] = x[len(x)-(i+1)]
                    x[len(x)-(i+1)] = "."
    return x
        
test = testInput1
print(test)
print(*decrypt(test), sep="")
print(*defrag(decrypt(test)), sep="")
