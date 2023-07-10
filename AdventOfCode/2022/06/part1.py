code = open("input.txt", mode="r").readline().strip()

for i in range(4, len(code)):
    mark = code[i-4:i]
    if len(set(mark)) == 4:
        print(i)
        break
