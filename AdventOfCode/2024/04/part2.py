dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1) ]

def get_letter(board, x, y, size):
    if x < 0 or x >= size[0] or y < 0 or y >= size[1]:
        return ""
    return board[y][x]

def get_word(board, x, y, size, dir):
    w = [ get_letter(board, x + a * dir[0], y + a * dir[1], size) for a in range(3) ]
    return "".join(w)

with open("input.txt", mode="r") as f:
    board = f.readlines()

size = (len(board[0]), len(board))
found = 0

for y in range(1, size[1] - 1):
    for x in range(1, size[0] - 1):
        w1 = get_word(board, x - 1, y - 1, size, (1, 1))
        w2 = get_word(board, x - 1, y + 1, size, (1, -1))
        if (w1 == "MAS" or w1 == "SAM") and (w2 == "MAS" or w2 == "SAM"):
            found += 1

print(found)
