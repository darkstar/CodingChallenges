class Deer:
    def __init__(self, name, speed, runtime, cooldown):
        self.name = name
        self.speed = speed
        self.runtime = runtime
        self.cooldown = cooldown
        self.distance = 0
        self.remaining_cooldown = 0
        self.running_time = 0

    def tick(self):
        # are we in cooldown?
        if self.remaining_cooldown > 0:
            self.remaining_cooldown -= 1

        if self.remaining_cooldown > 0:
            return

        if self.running_time >= self.runtime:
            # switch to cooldown
            self.running_time = 0
            self.remaining_cooldown = self.cooldown
            return

        # not in cooldown, running
        self.running_time += 1
        self.distance += self.speed

deers = {}

with open('input.txt', mode='r') as f:
    for line in f.readlines():
        words = line.split()

        name, speed, runtime, cooldown = words[0], int(words[3]), int(words[6]), int(words[13])
        deer = Deer(name, speed, runtime, cooldown)
        deers[name] = deer

    t = 0
    while t < 2503:
        for deer in deers:
            deers[deer].tick()
        t += 1 

    results = [x.distance for x in deers.values()]

    print(max(results))

