testInput1 = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

puzzleInput = str(open("day5input").read())

def ingest(string, section): # section should be "rules" or "updates"
    string = string.strip().split("\n\n")
    if section == "rules":
        string = string[0].split("\n")
        for i in range(len(string)):
            string[i] = string[i].split("|")
    elif section == "updates":
        string = string[1].split("\n")
        for i in range(len(string)):
            string[i] = string[i].split(",")
    return string

def isValidUpdate(update, rules):
    for i in range(len(update)-1):
        for j in range(i+1,len(update)):
            if [update[i],update[j]] not in rules:
                return False
    return True

def printQueue(string):
    total = 0
    rules = ingest(string, "rules")
    updates = ingest(string, "updates")
    for i in range(len(updates)):
        if (isValidUpdate(updates[i],rules)):
            total += int(updates[i][len(updates[i])//2])
    return total

print(printQueue(puzzleInput))
