import hashlib

index = 0

with open("input.txt", mode="r") as f:
    door = f.readline().strip()

password = ""

while len(password) < 8:
    s = "{}{}".format(door, index)
    dig = hashlib.new("md5", s.encode()).hexdigest()
    if dig[:5] == "00000":
        password += dig[5]

    index += 1

print(password)
