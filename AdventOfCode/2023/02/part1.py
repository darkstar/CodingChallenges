def mk_game_dict(s):
    result = {}

    k = s.split(",")
    for x in k:
        count, color = x.strip().split(" ")
        result[color] = int(count)

    return result

def is_game_valid(g):
    return g.get("red", 0) <= 12 and \
           g.get("green", 0) <= 13 and \
           g.get("blue", 0) <= 14

games = {}

with open("input.txt", mode="r") as f:
    while l := f.readline():
        game, rest = l.strip().split(":")
        gamenum = int(game.split(" ")[-1])
        draws = rest.split(";")
        games[gamenum] = list(map(mk_game_dict, draws))

result = 0

for num, game in games.items():
    if all(map(is_game_valid, game)):
        result += num

print(result)
