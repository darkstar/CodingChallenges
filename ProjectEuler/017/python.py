import math

def digit(n):
    dig = { 0:"", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
            6: "six", 7: "seven", 8: "eight", 9: "nine" }
    return dig[n]

def say(n):
    tens = { 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
            15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen" }
    decs = { 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy",
            8: "eighty", 9: "ninety" }

    if n == 0:
        return ""

    if n == 1000:
        return "onethousand"

    if n >= 100:
        s = digit(n // 100) + "hundred"
        if n % 100 != 0:
            s = s + "and" + say(n % 100)
        return s

    if n >= 20:
        return decs[n // 10] + say(n % 10)

    if n >= 10:
        return tens[n]

    return digit(n)

result = 0
for i in range(1, 1001):
    result = result + len(say(i))

print(result)

