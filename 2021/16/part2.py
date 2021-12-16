from functools import reduce

def hex2bin(h):
 return "".join(map(lambda x: ("000" + bin(int(x, 16))[2:])[-4:], h))

def oper(typ, vals):
  if typ == 0:
    return sum(vals)
  if typ == 1:
    return reduce(lambda a, b: a * b, vals, 1)
  if typ == 2:
    return min(vals)
  if typ == 3:
    return max(vals)
  if typ == 5:
    return 1 if vals[0] > vals[1] else 0
  if typ == 6:
    return 1 if vals[0] < vals[1] else 0
  if typ == 7:
    return 1 if vals[0] == vals[1] else 0

def parsepacket(p):
  global version
  # check to see if we're at the end of the packet
  if len(p) <= 6 and all(map(lambda k: k == 0, p)):
    return None, 0
  # parse packet header
  ver = int(p[:3],2)
  typ = int(p[3:6],2)
  rest = p[6:]

  # add version to global version sum
  version += ver

  if typ == 4:
    # literal value
    num = 0
    while True:
      # grab 5 bits
      nbits = rest[:5]
      rest = rest[5:]
      # add their value
      num = num * 16
      num = num + int(nbits[1:], 2)
      # exit if last group
      if nbits[0] == "0":
        break
    # end of type 4 packet
    return rest, num

  # operator packet
  ltype = int(rest[0],2)
  rest = rest[1:]
  if ltype ==  0:
    vals = []
    # type 0: 15 bits of packet length
    length = int(rest[:15], 2)
    rest = rest[15:]
    subpacket = rest[:length]
    rest = rest[length:]
    while len(subpacket) > 0:
      subpacket, v = parsepacket(subpacket)
      vals.append(v)
      
    return rest, oper(typ, vals)

  if ltype == 1:
    vals = []
    # type 1: number of sub-packets
    count = int(rest[:11], 2)
    rest = rest[11:]
    for i in range(count):
      rest, v = parsepacket(rest)
      vals.append(v)

    return rest, oper(typ, vals)

with open("input.txt", mode="r") as f:
  hexdata = f.readline().strip()

bindata = hex2bin(hexdata)

version = 0

#bindata = hex2bin("C200B40A82")
#bindata = hex2bin("04005AC33890")
#bindata = hex2bin("880086C3E88112")
#bindata = hex2bin("9C0141080250320F1802104A08")

_, val = parsepacket(bindata)

print(val)
