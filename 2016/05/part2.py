import hashlib

index = 0

with open("input.txt", mode="r") as f:
    door = f.readline().strip()

password = [ "_" ] * 8

while True:
    s = "{}{}".format(door, index)
    dig = hashlib.new("md5", s.encode()).hexdigest()
    if dig[:5] == "00000":
        pos = dig[5]
        val = dig[6]
        if pos in "01234567":
            if password[int(pos)] == "_":
                password[int(pos)] = val
                print("".join(password))
                if not "_" in password: break

    index += 1

print("password: {}".format("".join(password)))
