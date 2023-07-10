ranges = []

with open("input.txt") as f:
    for l in f.readlines():
        vals = l.strip().split("-")
        ranges.append( { "a" : int(vals[0]), "b" : int(vals[1]) } )

ranges.sort(key = lambda x: x["a"])

totalips = 0
ip = 0
for i in range(len(ranges)):
    x = ranges[i]
    # print("IP: {}, checking {}".format(ip, x))
    # skip the range if we're already past it
    if x["b"] < ip:
        # print("  skipped")
        continue
    # if the next range starts after the current IP, that IP is free
    if x["a"] > ip:
        # print("free until {} (exclusive), adding {} IPs".format(x["a"], x["a"] - ip))
        totalips += x["a"] - ip
    ip = x["b"] + 1

# end reached, add any remaining IPs until 2^32
totalips += 2**32 - ip

print(totalips)
