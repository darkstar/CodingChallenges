with open("input.txt", mode="r") as f:
    starttime = int(f.readline())
    times = list(map(int, filter(lambda x: x != "x", f.readline().strip().split(","))))

arrivals = list(map(lambda x: (x, ((starttime + x - 1) // x) * x), times))
arrivals.sort(key = lambda x: x[1])

print(arrivals[0][0] * (arrivals[0][1] - starttime))
