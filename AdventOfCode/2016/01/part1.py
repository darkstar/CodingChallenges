
movements = [ (0, 1), (1, 0), (0, -1), (-1, 0) ] # N E S W
position = (0, 0)
direction = 0 # north

with open("input.txt", mode="r") as f:
    instructions = f.readline().strip().split(", ")

    for step in instructions:
        rot = step[0]
        delta = int(step[1:])
        if rot == "L":
            direction -= 1
        elif rot == "R":
            direction += 1
        direction %= 4
        position = (position[0] + delta * movements[direction][0],
                    position[1] + delta * movements[direction][1])

print("distance: {}".format(abs(position[0]) + abs(position[1])))

