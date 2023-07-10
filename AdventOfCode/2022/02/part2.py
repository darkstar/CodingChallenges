def score(move):
    scores = { "A": 1, "B": 2, "C": 3 }
    losers = { "A": "C", "B": "A", "C": "B" }
    winners = { "A": "B", "B": "C", "C": "A" }

    if move[1] == "X": # lose
        return scores[losers[move[0]]]
    if move[1] == "Y": # draw
        return 3 + scores[move[0]]
    # else win
    return 6 + scores[winners[move[0]]]

with open("input.txt", mode="r") as f:
    rounds = [ x.strip().split(" ") for x in f.readlines() ]


print(sum(map(score, rounds)))

