all_units = {}

with open('input.txt',mode='r') as f:
  polymer = f.read(65536).rstrip()

  for u in polymer:
    all_units[u.lower()] = 0

  for unit in all_units:
    poly = polymer.replace(unit, '').replace(unit.upper(), '')

    i = 0
    while i < len(poly) - 1:
      (x, y) = (poly[i], poly[i+1])

      if ord(x) ^ ord(y) == 0x20:
        poly = poly[:i] + poly[i+2::]
        if i > 0:
          i -= 1
      else:
        i += 1

    all_units[unit] = len(poly)

print(min(all_units.values()))

