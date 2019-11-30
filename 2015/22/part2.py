from collections import defaultdict
from functools import reduce
import json

def stateexists(states, state):
    for s in states:
        if json.dumps(state, sort_keys=True) == json.dumps(s, sort_keys=True):
            return True
    return False

# player attack
def cast(spell, state):
    newstate = state.copy()
    if spell == "Magic Missile":
        if state["playermana"] < 53: return None     # enough mana?
        newstate["totalmanaspent"] += 53
        newstate["playermana"] -= 53
        newstate["bosshealth"] -= 4
        return newstate
    if spell == "Drain":
        if state["playermana"] < 73: return None     # enough mana?
        newstate["totalmanaspent"] += 73
        newstate["playermana"] -= 53
        newstate["bosshealth"] -= 2
        newstate["playerhealth"] += 2
        return newstate
    if spell == "Shield":
        if state["playermana"] < 113: return None    # enough mana?
        if state["shieldduration"] > 0: return None  # Shield already active?
        newstate["totalmanaspent"] += 113
        newstate["playermana"] -= 113
        newstate["shieldduration"] = 6
        return newstate
    if spell == "Poison":
        if state["playermana"] < 173: return None    # enough mana?
        if state["poisonduration"] > 0: return None  # Poison already active?
        newstate["totalmanaspent"] += 173
        newstate["playermana"] -= 173
        newstate["poisonduration"] = 6
        return newstate
    if spell == "Recharge":
        if state["playermana"] < 229: return None     # enough mana?
        if state["rechargeduration"] > 0: return None # Recharge already active?
        newstate["totalmanaspent"] += 229
        newstate["playermana"] -= 229
        newstate["rechargeduration"] = 5
        return newstate
    print("Invalid spell: {}".format(spell))
    return None

# evaluate / tick effects
def evaleffects(state):
    if state["shieldduration"] > 0:
        state["shieldduration"] -= 1
    if state["poisonduration"] > 0:
        state["poisonduration"] -= 1
        state["bosshealth"] -= 3
    if state["rechargeduration"] > 0:
        state["rechargeduration"] -= 1
        state["playermana"] += 101

# boss attack
def attack(state):
    playerarmor = 7 if state["shieldduration"] > 0 else 0
    dmg = max(1, state["bossdamage"] - playerarmor)
    state["playerhealth"] -= dmg

def checkvictory(state):
    if state["bosshealth"] < 1:
        print("Boss died! Total mana spent is {}".format(state["totalmanaspent"]))
        exit(0)
    
with open('input.txt', mode='r') as f:
    lines = f.readlines()
    targethp = int(lines[0].split(":")[1].strip())
    targetdamage = int(lines[1].split(":")[1].strip())
    print("Target: HP={}, Damage={}".format(targethp, targetdamage))

States = []

StartState = {
        "playerhealth": 50,
        "playermana": 500,
        "bosshealth": targethp,
        "bossdamage": targetdamage,
        "totalmanaspent": 0,
        "shieldduration": 0,
        "poisonduration": 0,
        "rechargeduration": 0,
        "whoseturn": "player"
    }

States.append(StartState)

while True:
    # sort states by least amount of mana used
    States.sort(key=lambda x: x["totalmanaspent"])
    # get the first state
    state = States.pop(0)
    # part2: every turn we lose 1 health
    if state["whoseturn"] == "player":
        state["playerhealth"] -= 1
    # check if player is dead
    if state["playerhealth"] < 1:
        continue
    # we already know that 1900 is too high so let's cap it at that
    if state["totalmanaspent"] > 1900:
        continue
    # check if boss is dead already?
    checkvictory(state)
    # evaluate pending effects
    evaleffects(state)
    # check again if boss is dead now
    checkvictory(state)
    # simulate turn
    if state["whoseturn"] == "player":
        # player turn. eval all possible spells
        for s in "Magic Missile", "Drain", "Shield", "Poison", "Recharge":
            newstate = cast(s, state)
            if not newstate is None:
                # next turn: boss
                newstate["whoseturn"] = "boss"
                if not stateexists(States, newstate):
                    States.append(newstate)
    else:
        # boss turn. simply attack
        attack(state)
        state["whoseturn"] = "player"
        States.append(state)
