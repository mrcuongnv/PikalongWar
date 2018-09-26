#!/usr/bin/env python3

###
# Given a text. Count n words with the most frequent occurrences (case insensitive, i.e Word, WORD or WoRd are the same). If there are many words with the same frequency, select the words with the smallest alphabetical order (for example, “an” has the lower  alphabetical order than “bow”).
###

import sys
import re
from collections import Counter
from functools import cmp_to_key


def compareWordCount(x, y):
    if x[1] < y[1]:
        return 1
    elif x[1] > y[1]:
        return -1
    else:
        if x[0] < y[0]:
            return -1
        elif x[0] > y[0]:
            return 1
        else:
            return 0


def mostCommonWords(text, n):
    word_count = Counter(re.findall("[a-z]+", text.lower()))
    result = sorted(word_count.items(), key=cmp_to_key(compareWordCount))[:n]
    for i in range(n - len(result)):
        result.append("")
    return result


def main():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("text", metavar='"TEXT"',
                        help="The text to be counted")
    parser.add_argument("n", metavar='N', type=int,
                        help="The number of the most common words to be printed out")
    args = parser.parse_args()
    print(mostCommonWords(args.text, args.n))


if __name__ == "__main__":
    sys.exit(main())
