import json

totalsum = 0

def visit(o):
    global totalsum

    if type(o) is list or type(o) is tuple:
        for x in o: visit(x)
    elif type(o) is dict:
        if "red" not in o.values():
           for x in o.items():
                visit(x[1])
    elif type(o) is str:
        pass
    else:
        totalsum += o

with open('input.txt', mode='r') as f:
    j = json.loads(f.readlines()[0])

    visit(j)

    print(totalsum)
