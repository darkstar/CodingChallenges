from collections import defaultdict
from functools import reduce

weapons = [
        { "name": "Dagger", "cost": 8, "dmg": 4, "armor": 0 },
        { "name": "Shortsword", "cost": 10, "dmg": 5, "armor": 0 },
        { "name": "Warhammer", "cost": 25, "dmg": 6, "armor": 0 },
        { "name": "Longsword", "cost": 40, "dmg": 7, "armor": 0 },
        { "name": "Greataxe", "cost": 74, "dmg": 8, "armor": 0 }
        ]

armors = [
        { "name": "None", "cost": 0, "dmg": 0, "armor": 0 },
        { "name": "Leather", "cost": 13, "dmg": 0, "armor": 1 },
        { "name": "Chainmail", "cost": 31, "dmg": 0, "armor": 2 },
        { "name": "Splintmail", "cost": 53, "dmg": 0, "armor": 3 },
        { "name": "Bandedmail", "cost": 75, "dmg": 0, "armor": 4 },
        { "name": "Platemail", "cost": 102, "dmg": 0, "armor": 5 },
        ]

rings = [
        { "name": "None", "cost": 0, "dmg": 0, "armor": 0 },
        { "name": "Damage +1", "cost": 25, "dmg": 1, "armor": 0 },
        { "name": "Damage +2", "cost": 50, "dmg": 2, "armor": 0 },
        { "name": "Damage +3", "cost": 100, "dmg": 3, "armor": 0 },
        { "name": "Defense +1", "cost": 20, "dmg": 0, "armor": 1 },
        { "name": "Defense +2", "cost": 40, "dmg": 0, "armor": 2 },
        { "name": "Defense +3", "cost": 80, "dmg": 0, "armor": 3 },
        ]

loadouts= []

def calcdmg(damage, armor):
    rawdmg = damage - armor
    return max(1, rawdmg)

def simulate(x):
    (w, a, lr, rr, damage, armor, cost) = x

#    print("{}/{}/{}".format(damage, armor, cost))
    hp = [100, targethp]
    dmg = [damage, targetdamage]
    arm = [armor, targetarmor]
    turn = 0
    opponent = 1
    while True:
        hp[opponent] -= calcdmg(dmg[turn], arm[opponent])
        if hp[opponent] < 1:
            if opponent == 1:
#                print("Opponent killed. Try again...")
                return
            else:
                print("Player died! Cost was {} ({}, {}, {}, {})".format(cost, w, a, lr, rr))
                exit(1)
        opponent = 1 - opponent
        turn = 1 - turn


def generate_loadouts():
    for w in weapons:
        for a in armors:
            for lr in range(len(rings)):
                for rr in range(lr, len(rings)):
                    if lr > 0 and (lr == rr): continue # skip double rings
                    damage = w["dmg"] + a["dmg"] + rings[lr]["dmg"] + rings[rr]["dmg"]
                    armor = w["armor"] + a["armor"] + rings[lr]["armor"] + rings[rr]["armor"]
                    cost = w["cost"] + a["cost"] + rings[lr]["cost"] + rings[rr]["cost"]
                    loadouts.append((w["name"], a["name"], rings[lr]["name"], rings[rr]["name"], damage, armor, cost))
#                    print("W: {}, A: {}, LR: {}, RR: {} -> Damage={}, Armor={}, Cost={}"
#                            .format(w["name"], a["name"], rings[lr]["name"], rings[rr]["name"], damage, armor, cost))

with open('input.txt', mode='r') as f:
    lines = f.readlines()
    targethp = int(lines[0].split(":")[1].strip())
    targetdamage = int(lines[1].split(":")[1].strip())
    targetarmor = int(lines[2].split(":")[1].strip())
    print("Target: HP={}, Damage={}, Armor={}".format(targethp, targetdamage, targetarmor))

# generate all possible loadout combinations
generate_loadouts()
# sort loadouts by cost descending
loadouts.sort(key=lambda t: -t[6])

for x in loadouts:
    simulate(x)

