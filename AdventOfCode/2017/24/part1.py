with open("input.txt") as f:
    ports = list(map(lambda x: tuple(map(int, x.strip().split("/"))), f.readlines()))

def strength(path):
    s = 0
    for i in path:
        s += ports[i][0] + ports[i][1]
    return s

def pathstr(path):
    return list(map(lambda s: ports[s], path))

maxstr = 0

def walk(path, endpiece):
    global maxstr

    # build a path of ports
    for port in range(len(ports)):
        # skip ports we already used
        if port in path:
            continue
        if ports[port][0] == endpiece:
            walk(path + [ port ], ports[port][1])
        if ports[port][1] == endpiece:
            walk(path + [ port ], ports[port][0])
    # check the current path for its strength
    if strength(path) > maxstr:
        maxstr = strength(path)

walk([], 0)

print(maxstr)
