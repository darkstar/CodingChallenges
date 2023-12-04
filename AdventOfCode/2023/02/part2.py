def mk_game_dict(s):
    result = {}

    k = s.split(",")
    for x in k:
        count, color = x.strip().split(" ")
        result[color] = int(count)

    return result

def minimum_cubes(games):
    result = {}
    for color in ["red", "green", "blue"]:
        result[color] = max(list(map(lambda x: x.get(color, 0), games)))
    return result

def power(game):
    return game["red"] * game["green"] * game["blue"]

games = {}

with open("input.txt", mode="r") as f:
    while l := f.readline():
        game, rest = l.strip().split(":")
        gamenum = int(game.split(" ")[-1])
        draws = rest.split(";")
        games[gamenum] = list(map(mk_game_dict, draws))

result = 0

for num, game in games.items():
    result += power(minimum_cubes(game))

print(result)
