def hex2bin(h):
 return "".join(map(lambda x: ("000" + bin(int(x, 16))[2:])[-4:], h))

def parsepacket(p):
  global version
  # check to see if we're at the end of the packet
  if len(p) <= 6 and all(map(lambda k: k == 0, p)):
    return
#  print("packet:")
  # parse packet header
  ver = int(p[:3],2)
  typ = int(p[3:6],2)
  rest = p[6:]

  # add version to global version sum
  version += ver

#  print("  ver  {}".format(ver))
#  print("  type {}".format(typ))
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
#    print("    literal = {}".format(num))
    return rest

  # operator packet
  ltype = int(rest[0],2)
  rest = rest[1:]
#  print("    operator packet length type {}".format(ltype))
  if ltype ==  0:
    # type 0: 15 bits of packet length
    length = int(rest[:15], 2)
    rest = rest[15:]
#    print("    len = {}".format(length))
    subpacket = rest[:length]
    rest = rest[length:]
    while len(subpacket) > 0:
#      print("    subpacket:")
      subpacket = parsepacket(subpacket)

    return rest

  if ltype == 1:
    # type 1: number of sub-packets
    count = int(rest[:11], 2)
    rest = rest[11:]
#    print("    count = {}".format(count))
    for i in range(count):
#      print("    subpacket {}:".format(i+1))
      rest = parsepacket(rest)
    return rest

with open("input.txt", mode="r") as f:
  hexdata = f.readline().strip()

bindata = hex2bin(hexdata)

version = 0

#parsepacket("110100101111111000101000")
#parsepacket("00111000000000000110111101000101001010010001001000000000")
#parsepacket("11101110000000001101010000001100100000100011000001100000")
#parsepacket(hex2bin("8A004A801A8002F478"))
#parsepacket(hex2bin("A0016C880162017C3686B18A3D4780"))

parsepacket(bindata)

print(version)
