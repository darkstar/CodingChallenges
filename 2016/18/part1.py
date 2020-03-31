import re

with open("input.txt") as f:
    start = f.readlines()[0].strip()

#start = "..^^."
#start = ".^^.^.^^^^"

def rule(s):
    return "^" if s in [ "^^.", ".^^", "^..", "..^" ] else "."

a = start
safespots = 0

for step in range(40):
    # count the number of safe spots in the current row
    safespots += a.count(".")
    # append the "safe" walls left and right (for easier iterating)
    temp = "." + a + "."
    # start building the new row
    nextrow = ""
    for x in range(len(a)):
        nextrow += rule(temp[x:x+3])

    a = nextrow

print(safespots)
