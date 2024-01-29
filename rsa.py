#!/usr/bin/env python3

import sys
import math
import gmpy2

def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = y = 2
    d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)
    return d

def factorize(n):
    p = pollards_rho(n)
    q = n // p
    return p, q

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                number = int(line)
                p, q = factorize(number)
                print(f"{number}={p}*{q}")

def main():
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    input_file = sys.argv[1]
    factorize_file(input_file)

if __name__ == "__main__":
    main()
