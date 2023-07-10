
layersize = 25 * 6

with open("input.txt", mode="r") as f:
    pixeldata = f.readline().strip()

layer = 1
fewest = 9999
result = 0

while len(pixeldata) > 0:
    layerdata = pixeldata[:layersize]
    pixeldata = pixeldata[layersize:]
    if layerdata.count('0') < fewest:
        fewest = layerdata.count('0')
        result = layerdata.count('1') * layerdata.count('2')

print(result)
