
layersize = 25 * 6

image = [ '2' for x in range(layersize) ]

with open("input.txt", mode="r") as f:
    pixeldata = f.readline().strip()

while len(pixeldata) > 0:
    layerdata = pixeldata[:layersize]
    pixeldata = pixeldata[layersize:]

    image = list(map(lambda x: x[1] if x[0] == '2' else x[0], zip(image, layerdata)))

for x in range(6):
    print("".join(map(lambda c: '#' if c == '1' else ' ', image[25 * x:25 * (x+1)])))
