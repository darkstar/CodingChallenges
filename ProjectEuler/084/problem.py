import random

field = [ 0 for x in range(40) ]
cc = [None for x in range(14)] + ["GO", "JAIL" ]
ch = [None for x in range(6)] + [ "GO", "JAIL", "11", "24", "39", "5", "R", "R", "U", "-3" ]

random.seed()
random.shuffle(cc)
random.shuffle(ch)

steps = 0
pos = 0

doubles = 0

print("Please wait this will take a while, it is a simulation after all...")
while steps < 30000000:
    field[pos] += 1
    #print("Player at", pos)
    # würfeln
    d1 = random.randint(1, 4)
    d2 = random.randint(1, 4)
    dice = d1 + d2
    # beim dritten pasch -> ab ins Gefängnis
    if d1 == d2:
        doubles += 1
        if doubles == 3:
            pos = 10
            continue
    else:
        doubles = 0
    # vorwärts gehen
    pos += dice
    pos %= 40
    # Community Chest
    if pos in [2, 17, 33]:
        # draw a card
        card = cc[0]
        cc = cc[1:] + [ cc[0] ]
        #print("cc card:", card)
        # evaluate card
        if card == "GO":
            pos = 0
        if card == "JAIL":
            pos = 10
    # Chance fields
    elif pos in [7, 22, 36]:
        # draw a card
        card = ch[0]
        ch = ch[1:] + [ ch[0] ]
        #print("ch card:", card)
        # evaluate card
        if card is None:
            pass
        elif card == "GO":
            pos = 0
        elif card == "JAIL":
            pos = 10
        elif card == "-3":
            pos -= 3
            if pos < 0:
                pos += 40
        elif card == "U":
            if (pos < 12) or (pos >= 28):
                newpos = 12
            elif pos <28:
                newpos = 28
            pos = newpos
        elif card == "R":
            if (pos < 5) or (pos >= 35):
                newpos = 5
            elif pos < 15:
                newpos = 15
            elif pos < 25:
                newpos = 25
            elif pos < 35:
                newpos = 35
            pos = newpos
        else:
            pos = int(card)
    # go to jail
    elif pos == 30:
        pos = 10

    #print("new pos =", pos)
    steps += 1

result = [ (a, field[a]) for a in range(40) ]
result.sort(key = lambda x: x[1])
result = result[-3:]
print("{0:02d}{1:02d}{2:02d}".format(result[2][0], result[1][0], result[0][0]))
