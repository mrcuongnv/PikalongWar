#!/usr/bin/env python3

# Problem: http://pikalongwar.com/task/detail?TaskID=1306&BatchID=1076&tabindex=0

NUM_READ = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]


def read3(n, has_prefix):
    tram = int(n[0])
    chuc = int(n[1])
    donvi = int(n[2])

    if tram == 0 and chuc == 0 and donvi == 0:
        return ""

    output = []
    # Hang tram
    if has_prefix or (not has_prefix and tram > 0):
        output.append(NUM_READ[tram])
        output.append("tram")
    
    # Hang chuc
    if chuc == 0:
        if (tram > 0 or has_prefix) and (donvi > 0):
            output.append("le")
    elif chuc == 1:
        output.append("muoi")
    else:
        output.append(NUM_READ[chuc])
        output.append("muoi")
    
    # Hang don vi
    if donvi == 4 and chuc >= 2:
        output.append("tu")
    elif donvi == 5 and chuc >= 1:
        output.append("lam")
    elif donvi > 0:
        output.append(NUM_READ[donvi])
    
    return " ".join(output)


def read9(n, has_prefix):
    UNIT_READ = ["ngan", "trieu"]

    output = []
    unit = 0
    while len(n) > 0:
        text = read3(n[-3:].rjust(3, "0"), has_prefix or (len(n) > 3))
        unit += 1
        if text != "":
            output.insert(0, text)
            if unit > 1:
                output.insert(1, UNIT_READ[unit - 2])
        n = n[:-3]
    return " ".join(output)


def number2Word(number):
    n = number.lstrip("0")
    
    if len(n) == 0:
        return "khong"
    
    output = []
    unit = 0
    while len(n) > 0:
        text = read9(n[-9:], len(n) > 9)
        unit += 1
        if text != "":
            output.insert(0, text)
            if unit > 1:
                output.insert(1, " ".join(["ty"] * (unit - 1)))
        n = n[:-9]
    return " ".join(output)



def main():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("number", metavar="N", type=str,
                        help="Number to be read")
    args = parser.parse_args()

    print(number2Word(args.number))


if __name__ == "__main__":
    main()
