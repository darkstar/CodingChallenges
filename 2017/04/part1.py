with open("input.txt") as f:
    phrases = f.readlines()

valid = 0

for phrase in phrases:
    words = phrase.split()
    check = set(words)
    if len(words) == len(check):
        valid += 1

print(valid)
