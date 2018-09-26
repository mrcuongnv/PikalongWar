#!/usr/bin/env python3

# Problem: http://pikalongwar.com/task/detail?TaskID=1262&BatchID=1076&tabindex=0


def soLuongGiaiMa(x):
    slgm = []
    if int(x[0]) == 0:
        return 0
    else:
        slgm.append(1)
    
    if len(x) > 1:
        if int(x[1]) == 0:
            if int(x[0]) > 2:
                return 0
            else:
                slgm.append(1)
        else:
            if 11 <= int(x[:2]) <= 26:
                slgm.append(2)
            else:
                slgm.append(1)
        
    for i in range(2, len(x)):
        xi = int(x[i])
        xi_10 = int(x[i-1:i+1])
        if xi == 0:
            if xi_10 > 20:
                return 0
            else:
                slgm.append(slgm[-2])
        else:
            if 11 <= xi_10 <= 26:
                slgm.append(slgm[-2] + 2)
            else:
                slgm.append(slgm[-1])

    return slgm[-1]


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("file", metavar="FILE",
                        help="File containing the input string.")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        print(soLuongGiaiMa(f.read().strip()))


if __name__ == "__main__":
    main()
