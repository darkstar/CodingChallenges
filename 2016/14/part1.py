import re
import hashlib

with open("input.txt") as f:
    salt = f.readlines()[0].strip()

index = 0
keycandidates = []
keys = []

while True:
    candidate = hashlib.md5((salt + str(index)).encode("ascii")).hexdigest()

    # find validators of previous candidates
    m = re.search(r'(.)\1\1\1\1', candidate)
    if m:
        # this validates all candidates from (index - 1000) to (index - 1)
        ch = m.groups(1)[0]
        # print("i={} -> {} / {} VALIDATING".format(index, ch, candidate))
        for j in range(len(keycandidates)):
            cand = keycandidates[j]
            if (index < cand["index"] + 1000) and (cand["char"] == ch):
                #print("VALID KEY: {}".format(cand))
                keys.append(cand)

    # check if the MD5 is a key candidate
    m = re.search(r'(.)\1\1', candidate)
    if m:
        # it is a key candidate. add it to our list
        ch = m.groups(1)[0]
        keycandidates.append({ "index": index, "char": ch, "key": candidate})
        # print("i={} -> {} / {} CANDIDATE".format(index, ch, candidate))

    # remove all old key candidates (to clean up)
    while (len(keycandidates) > 0) and (keycandidates[0]["index"] + 1000 < index):
        del(keycandidates[0])

    if index > 100000:
        break

    index += 1

print(sorted(keys, key=lambda x: x["index"])[63]["index"])

