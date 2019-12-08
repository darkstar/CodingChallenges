
layersize = 25 * 6

image = [ '2' for x in range(layersize) ]

with open("input.txt", mode="r") as f:
    pixeldata = f.readline().strip()

while len(pixeldata) > 0:
    layerdata = pixeldata[:layersize]
    pixeldata = pixeldata[layersize:]

    for x in range(layersize):
        px = layerdata[x]
        cur = image[x]
        if cur == '2':
            image[x] = px

for x in range(6):
    print("".join(map(lambda c: '#' if c == '1' else ' ', image[25 * x:25 * (x+1)])))
