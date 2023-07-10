from functools import reduce

def noncorrupt(l):
    valid = { '<': '>', '(': ')', '{': '}', '[': ']' }
    stack = []
    for c in l:
        if c in "<{[(":
            stack.append(c)
        else:
            # opening element
            tos = stack.pop()
            #check if opening and closing elements match
            if c != valid[tos]:
                return False
    return True

def points(l):
    valid = { '<': '>', '(': ')', '{': '}', '[': ']' }
    points = { '(': 1, '[': 2, '{': 3, '<': 4 }
    stack = []
    total = 0
    for c in l:
        if c in "<{[(":
            stack.append(c)
        else:
            # opening element, assume closing element is correct
            stack.pop()

    stack.reverse()
    for x in stack:
        total *= 5
        total += points[x]
    return total


with open("input.txt", mode="r") as f:
    code = [ x.strip() for x in f.readlines()]

#code = [ "[({(<(())[]>[[{[]{<()<>>", "[(()[<>])]({[<{<<[]>>(", "(((({<>}<{<{<>}{[]{[]{}",
#        "{<[[]]>}<{[{[{[]{()[[[]", "<{([{{}}[<[[[<>{}]]]>[]]" ]

code = list(filter(noncorrupt, code))

points = sorted(list(map(points, code)))

print(points[len(points)//2])
