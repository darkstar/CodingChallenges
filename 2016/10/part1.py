import re

bots = {}
botrules = {}
outputs = {}

with open("input.txt", mode="r") as f:
    cmds = f.readlines()

    for c in cmds:
        c = c.strip()
        m = re.match(r"value (\d+) goes to bot (\d+)", c)
        if m is not None:
            v = int(m.group(1))
            b = int(m.group(2))
            if b in bots:
                bots[b].append(v)
            else:
                bots[b] = [ v ]
            continue
        m = re.match(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)", c)
        if m is not None:
            b = int(m.group(1))
            lo = int(m.group(3))
            hi = int(m.group(5))
            lox = "b" if m.group(2) == "bot" else "o"
            hix = "b" if m.group(4) == "bot" else "o"
            botrules[b] = ( ( lox, lo ), ( hix, hi ) )
            # ensure the bot exists even if it has no input yet
            if not b in bots:
                bots[b] = [ ]
            continue
        print("Unmatched line: {}".format(c))
        exit(1)

distcount = 0

while True:
    distcount = 0
    # check for all bots
    for b in bots:
        if len(bots[b]) == 2:
#            print("running bot {}: {}".format(b, bots[b]))
            distcount += 1
            # bot has 2 inputs, disperse them
            lo = min(bots[b][0], bots[b][1])
            hi = max(bots[b][0], bots[b][1])
            if lo == 17 and hi == 61:
                print(b)
                exit(0)
            lorule = botrules[b][0]
            hirule = botrules[b][1]
            lodest = lorule[0]
            loval = lorule[1]
            hidest = hirule[0]
            hival = hirule[1]
#            print("putting {} to {} {} and {} to {} {}".format(lo, lodest, loval, hi, hidest, hival))
#            print("before:")
#            print("  {}: {}".format(loval, bots[loval]))
#            print("  {}: {}".format(hival, bots[hival]))
            # distribute low value
            if lodest == "o":
                if loval in outputs:
                    outputs[loval].append(lo)
                else:
                    outputs[loval] = [ lo ]
            else:
                bots[loval].append(lo)
            # same for high value
            if hidest == "o":
                if hival in outputs:
                    outputs[hival].append(hi)
                else:
                    outputs[hival] = [ hi ]
            else:
                bots[hival].append(hi)
            bots[b] = []
#            print("after:")
#            print("  {}: {}".format(b, bots[b]))
#            print("  {}: {}".format(loval, bots[loval]))
#            print("  {}: {}".format(hival, bots[hival]))

    if distcount == 0:
#        print(outputs)
        exit(1)
