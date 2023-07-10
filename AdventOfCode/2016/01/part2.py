
movements = [ (0, 1), (1, 0), (0, -1), (-1, 0) ] # N E S W
position = (0, 0)
direction = 0 # north
visited = { (0, 0): True }
found = False

with open("input.txt", mode="r") as f:
    instructions = f.readline().strip().split(", ")

    for step in instructions:
        if found: break
        rot = step[0]
        delta = int(step[1:])
        if rot == "L":
            direction -= 1
        elif rot == "R":
            direction += 1
        direction %= 4
        for x in range(delta):
            position = (position[0] + movements[direction][0],
                        position[1] + movements[direction][1])
            if (position in visited):
                found = True
                break
            visited[position] = True

print("distance: {}".format(abs(position[0]) + abs(position[1])))

