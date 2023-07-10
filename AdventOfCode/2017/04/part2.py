with open("input.txt") as f:
    phrases = f.readlines()

valid = 0

for phrase in phrases:
    words = phrase.split()
    # first, we sort each word by letters
    check = set(map(lambda x: "".join(sorted(x)), words))
    # then we build a set out of those and see if it's shorter
    if len(words) == len(check):
        valid += 1

print(valid)
