class Node:
    t = ""
    n = ""
    s = ""
    sub = None
    parent = None
    def __init__(self, typ, name, size = 0, par = None):
        self.t = typ
        self.n = name
        self.s = size if typ == "file" else 0
        self.sub = None if typ == "file" else {}
        self.parent = par

allsizes = {}

def fullpath(node):
    s = node.n
    while node.parent != None:
        s = "/" + s
        node = node.parent
        s = node.n + s
    return s[1:]

def siz(node):
    global allsizes

    ts = 0
    for x in node.sub.values():
        if x.t == "dir":
            ts += siz(x)
        else:
            ts += x.s
    if ts < 100000:
        allsizes[fullpath(node)] = ts
    return ts

with open("input.txt", mode="r") as f:
    l = [ x.strip() for x in f.readlines() ]

root = Node("dir", "/")
sel = None

i = 0
while i < len(l):
    c = l[i]
    if c[0] == "$":
        if c[2:4] == "cd":
            # change dir
            to = c[5:]
            #print("chdir to {}".format(to))
            if to == "..":
                #print("  cdup")
                sel = sel.parent
            else:
                if to[0] == "/":
                    #print("starting at /")
                    sel = root
                    to = to[1:]
                path = to.split("/")
                while len(path) > 0:
                    if len(path[0]) == 0:
                        break
                    #print("  goto {}".format(path[0]))
                    sel = sel.sub[path[0]]
                    path = path[1:]

            #print("now at {}".format(fullpath(sel)))
        elif c[2:4] == "ls":
            # ls
            #print("ls")
            pass
        else:
            #print("invalid command {}".format(c[2:]))
            exit(1)
    else:
        # ls output
        x, y = c.split(" ")
        if x == "dir":
            subdir = Node("dir", y, 0, sel)
            #print("new subdir {}".format(y))
            sel.sub[y] = subdir
        else:
            f = Node("file", y, int(x), sel)
            #print("new file {}".format(y))
            sel.sub[y] = f
    i += 1

x = siz(root)

print(sum(allsizes.values()))
