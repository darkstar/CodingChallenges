players = 0
last_marble_value = 0

marbles = [0]
current_marble = 0

next_marble = 1
current_player = 0

score = []

def print_state():
    m = [str(x) for x in marbles]
    m[current_marble] = "[{}]".format(m[current_marble])
    print('[{}] - {}'.format(current_player, ' '.join(m)))

with open('input.txt', mode='r') as f:
    words = f.readlines()[0].split()
    players = int(words[0])
    last_marble_value = int(words[6])
    score = [0 for x in range(players + 1)]

while True:
    #print_state()

    if next_marble % 23 == 0:
        # scoring
        score[current_player] += next_marble
        to_remove = (current_marble - 7) % len(marbles)
        additional_score = marbles.pop(to_remove)
        score[current_player] += additional_score
        current_marble = to_remove % len(marbles)
    else:
        # find spot after which to place the next marble
        new_pos = (current_marble + 1) % len(marbles)
        marbles.insert(new_pos + 1, next_marble)
        current_marble = new_pos + 1

    if next_marble == last_marble_value:
        print("Last Marble value: ", next_marble)
        print("Highscore: ", max(score))
        exit(1)

    next_marble += 1
    current_player += 1
    if current_player > players:
        current_player = 1
