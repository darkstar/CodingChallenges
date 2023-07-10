total_code_size = 0
total_string_size = 0

def parse(l):
    val = 0

    x = 1
    while x < len(l) - 1:
        if l[x] == '\\':
            x += 1
            if l[x] in [ '\\', '\"' ]:
                x += 1
                val += 1
            elif l[x] == 'x':
                x += 3
                val += 1
        else:
            val += 1
            x += 1

    return val

with open('input.txt', mode='r') as f:
    lines = [x.rstrip() for x in f.readlines()]
    for line in lines:
        total_code_size += len(line)
        total_string_size += parse(line)

print(total_code_size - total_string_size)
