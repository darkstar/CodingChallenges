fw = {}

with open("input.txt") as f:
    for line in f.readlines():
        pfilter = line.strip().split(": ")
        fw[int(pfilter[0])] = { "depth": int(pfilter[0]), "range": int(pfilter[1]), "cur": 0 , "dir": 1 }

last = int(pfilter[0])

# for testing
#fw = { 0: { "depth": 0, "range": 3, "cur": 0, "dir": 1},
#       1: { "depth": 1, "range": 2, "cur": 0, "dir": 1},
#       4: { "depth": 4, "range": 4, "cur": 0, "dir": 1},
#       6: { "depth": 6, "range": 4, "cur": 0, "dir": 1}}
#last = 6

# OPTIMIZATION: instead of running the simulation, just check
# (ps + depth) % (2 * range[depth] - 2) == 0
# for each filter

ps = 0
severity = 0
packets = [ { "start": 0, "pos": 0 } ] # the position of each packet
while True:
#    print("time {}:".format(ps))
#    print("  packets inflight: {}".format(packets))
    # for each packet, check if we have a filter at the current position
    drop = []
    for pa in packets:
        if pa["pos"] in fw:
            # check if the packet moved into a controlled layer
            flt = fw[pa["pos"]]
            if flt["cur"] == 0:
                drop.append(pa)
    # drop packets that were caught
    packets = list(filter(lambda p: not p in drop, packets))
#    print("  packets dropped: {}".format(drop))

    # move all filters
    for flt in fw:
        fw[flt]["cur"] = fw[flt]["cur"] + fw[flt]["dir"]
        # invert movement direction if we hit the end
        if fw[flt]["cur"] == 0 or fw[flt]["cur"] == fw[flt]["range"] - 1:
            fw[flt]["dir"] *= -1

    # move all packets
    for pa in packets:
        pa["pos"] += 1
        if pa["pos"] > last:
            print(pa["start"])
            break
    # tick time
    ps += 1
    # add new packet
    packets.append( { "start": ps, "pos": 0 } )

