def area(x, y, xmin, xmax, ymin, ymax, outside, img):
  b = ""
  for yy in range(y - 1, y + 2):
    for xx in range(x - 1, x + 2):
      if xx < xmin or xx > xmax or yy < ymin or yy > ymax:
        b += str(outside)
      else:
        v = 1 if (xx, yy) in img else 0
        b += str(v)
  return int(b, 2)

def prn(xmin, xmax, ymin, ymax, outside, image):
  for y in range(ymin - 1, ymax + 2):
    for x in range(xmin - 1, xmax + 2):
      if x < xmin or x > xmax or y < ymin or y > ymax:
        print("#" if outside == 1 else ".", end="")
      else:
        if (x, y) in image:
          print("#", end="")
        else:
          print(".", end="")
    print("")

with open("input.txt", mode="r") as f:
  rule = f.readline().strip()
  f.readline()
  img = [ x.strip() for x in f.readlines() ]

#debug
#rule = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##"\
#  "#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###"\
#  ".######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#."\
#  ".#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#....."\
#  ".#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.."\
#  "...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#....."\
#  "..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
#img = [ "#..#.", "#....", "##..#", "..#..", "..###"]

# save only set bits here
outside = 0
image = {}
for y in range(len(img)):
  for x in range(len(img[0])):
    p = (x, y)
    v = img[y][x]
    if v == '#':
      image[p] = 1

for step in range(50):
  newimg = {}
  xmin = min(x for (x, y) in image)
  xmax = max(x for (x, y) in image)
  ymin = min(y for (x, y) in image)
  ymax = max(y for (x, y) in image)
  for y in range(ymin - 1, ymax + 2):
    for x in range(xmin - 1, xmax + 2):
      a = area(x, y, xmin, xmax, ymin, ymax, outside, image)
      nv = 1 if rule[a] == '#' else 0
      if nv == 1:
        newimg[(x, y)] = 1
  image = newimg
  outside = 1 - outside
#  print("After step {}".format(step+1))
#  prn(xmin, xmax, ymin, ymax, outside, image)

print(len(newimg))
