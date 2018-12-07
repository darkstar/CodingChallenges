import hashlib

i = 0

with open('input.txt', mode='r') as f:
    prefix = f.readlines()[0].rstrip()
    
    while True:
        test = prefix + str(i)
        hash = hashlib.md5(test.encode('utf-8')).hexdigest()

        if hash.startswith('0' * 5):
            print(i)
            exit(0)

        i += 1
