import re

result = 0

with open("input.txt", mode="r") as f:
    lines = f.readlines()

for addr in lines:
    # check for ABBA within brackets
    m = re.search(r"\[[^\]]*([^\]])([^\]])\2\1[^\]]*\]", addr)
    if m is None:
        # now check for ABBA outside of brackets (all the rest)
        m = re.search(r"([^\]])([^\]])\2\1", addr)
        if m is not None:
            if m.group(1) != m.group(2):
                result = result + 1


print(result)
