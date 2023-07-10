from functools import reduce

def points(l):
    valid = { '<': '>', '(': ')', '{': '}', '[': ']' }
    points = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
    stack = []
    for c in l:
        if c in "<{[(":
            stack.append(c)
        else:
            # opening element
            tos = stack.pop()
            #check if opening and closing elements match
            if c != valid[tos]:
                return points[c]
    return 0
            
with open("input.txt", mode="r") as f:
    code = [ x.strip() for x in f.readlines()]

#code = ["[({(<(())[]>[[{[]{<()<>>","[(()[<>])]({[<{<<[]>>(","{([(<{}[<>[]}>{[]{[(<()>","(((({<>}<{<{<>}{[]{[]{}",
#"[[<[([]))<([[{}[[()]]]","[{[{({}]{}}([{[{{{}}([]","{<[[]]>}<{[{[{[]{()[[[]","[<(<(<(<{}))><([]([]()",
#"<{([([[(<>()){}]>(<<{{","<{([{{}}[<[[[<>{}]]]>[]]"]

points = list(map(points, code))
total = reduce(lambda a, b: a + b, points, 0)

print(total)
