import md5

def day1(text):
    return text.count("(") - text.count(")")

def day2(text):
    total = 0
    for s in text.split("\n")[:-1]:
        l,w,h = [int(q) for q in s.split("x")]
        sides = [w*h,w*l,l*h]
        total += sum(sides)*2+min(sides)
    return total

def day3(text):
    x = 0
    y = 0
    houses = set()

    for c in text:
        if c == "^":
            x += 1
        elif c == "v":
            x -= 1
        elif c == "<":
            y -= 1
        elif c == ">":
            y += 1
        houses.add((x,y))
    return len(houses)

def day4(text):
    salt = text.strip("\n")
    num = 1
    while not md5.new(salt + str(num)).hexdigest().startswith("00000"):
        num += 1
    return num
