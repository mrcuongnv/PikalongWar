###
# Easy / 200
#
# Given a natural number n. Find the number of divisors of n.
#
# Input:
#
# The natural number n. (1 <= n <= 10^14)
#
# Output:
#
# The number of divisors of n. The maximum execution time is 3 seconds
###

import sys
from math import sqrt
from itertools import count, islice


def isPrime(n):
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in islice(count(3, 2), int(sqrt(n))):
        if n % i == 0:
            return False
    return True


def numOfDivisors(n):
    if n == 1:
        return 1
    elif n == 2 or n == 3:
        return 2
    
    prime_count = {}
    m = n
    if m % 2 == 0:
        prime_count[2] = 0
        while m != 1 and m % 2 == 0:
            prime_count[2] += 1
            m /= 2
    i = 3
    max_i = int(sqrt(m))
    while m != 1 and i <= max_i:
        if isPrime(i) and m % i == 0:
            prime_count[i] = 0
            while m != 1 and m % i == 0:
                prime_count[i] += 1
                m /= i
        i += 2
        max_i = int(sqrt(m))
    
    if m != 1:
        prime_count[m] = 1
    
    nod = 1
    for p in prime_count:
        nod *= prime_count[p] + 1

    return nod


def main():
    print(numOfDivisors(int(sys.argv[1])))


if __name__ == "__main__":
    sys.exit(main())
