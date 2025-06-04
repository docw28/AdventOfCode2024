testInput1 = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

# for each test value, check i = each value, j = + or *
# return True or False
# total Trues

def ingest(x): # where x is puzzle input
    x = x.split("\n")
    for i in range(len(x)):
        x[i] = x[i].split(": ")
        x[i][1] = x[i][1].split(" ")
    return x
    
def validEquation(equation): # where "equation" is in the form ['xxx', ['aa', 'bb', 'cc']]
    testValue = equation[0]
    ops = len(equation[1]) - 1 # ops = operators
    
    return False
print(*ingest(testInput1), sep="\n")


