from collections import defaultdict

packages = []
totalweight = 0
targetweight = 0
partitions = []
minlength = 999
minentanglement = 99999999999999999999

def entanglement(x):
    r = 1
    for i in x:
        r *= i
    return r

def addpartition(t):
    global minlength
    global partitions
    global minentanglement

    if len(t[0]) > minlength:
        return
    if len(t[0]) < minlength:
        print("new minimum length: {}".format(len(t[0])))
        partitions = list(t[0])
        minlength = len(t[0])
        minentanglement = 99999999999999999999
    else:
        partitions.append(t[0])
    
    # calculate new best entanglement
    ent = entanglement(t[0])
    if (ent < minentanglement):
        minentanglement = ent
        print("New minimal entanglement: {}".format(ent))

# select a number of packets that meet the weight requirements
# from the list of packages
def genpartition(a, packages, start, targetweight):
    if len(a) > 0 and sum(a) == targetweight:
        addpartition((a, packages))
        return
    if len(a) > 0 and sum(a) > targetweight:
        return
    for x in range(start, len(packages)):
        newlist = a.copy()
        newlist.append(packages[x])
        genpartition(newlist, packages, x + 1, targetweight)

with open('input.txt', mode='r') as f:
    programcode = f.readlines()
    for l in programcode:
        packages.append(int(l.strip()))
        totalweight += int(l.strip())

targetweight = totalweight // 4

packages.reverse()

genpartition([], packages, 0, targetweight)

