def score(move):
    draws = [ "AX", "BY", "CZ" ]
    wins = [ "AY", "BZ", "CX" ]
    scores = { "X": 1, "Y": 2, "Z": 3 }

    x = "{}{}".format(move[0], move[1])
    if x in draws:
        return 3 + scores[move[1]]
    if x in wins:
        return 6 + scores[move[1]]
    return scores[move[1]]

with open("input.txt", mode="r") as f:
    rounds = [ x.strip().split(" ") for x in f.readlines() ]


print(sum(map(score, rounds)))

