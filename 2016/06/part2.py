result = []

with open("input.txt", mode="r") as f:
    messages = f.readlines()

    # for every letter...
    for i in range(len(messages[0].strip())):
        # first clear the existing distribution
        distribution = {}
        for m in messages:
            ch = m[i]
            if ch in distribution:
                distribution[ch] = distribution[ch] + 1
            else:
                distribution[ch] = 1
        # now convert to list and sort
        ldist = []
        for k in distribution:
            ldist.append( (k, distribution[k]) )
        ldist.sort(key = lambda x: x[1])
        result.append(ldist[0][0])

print("".join(result))
