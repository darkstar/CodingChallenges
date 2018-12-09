players = 0
last_marble_value = 0

next_marble = 1
current_player = 0

score = []

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

current_marble = Node(0)
current_marble.left = current_marble
current_marble.right = current_marble

with open('input.txt', mode='r') as f:
    words = f.readlines()[0].split()
    players = int(words[0])
    last_marble_value = 100 * int(words[6])
    score = [0 for x in range(players + 1)]

while True:
    if next_marble % 23 == 0:
        # scoring
        score[current_player] += next_marble

        to_remove = current_marble.left.left.left.left.left.left.left
        additional_score = to_remove.val
        l = to_remove.left
        r = to_remove.right
        l.right = r
        r.left = l
        score[current_player] += additional_score
        current_marble = r
    else:
        # find spot after which to place the next marble
        newnode = Node(next_marble)
        l = current_marble.right
        r = current_marble.right.right
        l.right = newnode
        newnode.left = l
        newnode.right = r
        r.left = newnode
        current_marble = newnode

    if next_marble == last_marble_value:
        print("Last Marble value: ", next_marble)
        print("Highscore: ", max(score))
        exit(1)

    next_marble += 1
    current_player += 1
    if current_player > players:
        current_player = 1
