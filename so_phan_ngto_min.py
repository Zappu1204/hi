from math import *
from bisect import bisect_left
import sys
MAXN = 10 ** 8

# Fuction check prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0: 
            return False
    return True

# Fuction generate prime numbers
def gen_primes():
    list_p = []
    pri = 1
    for i in range(2, int(sqrt(MAXN))):
        if is_prime(i): 
            list_p.append(i)
            pri *= i
            if pri > MAXN:
                break
    return list_p

list_p = gen_primes() # Những thừa số nguyên tố cấu tạo nên ~= MAXN. 

# Fuction generate list of highly composite numbers
def gen_hcn():
    # List of (number, number of divisors, exponents of the factorization)
    hcn = [(1, 1, [])]
    for i in range(len(list_p)):
        new_hcn = []
        for el in hcn:
            new_hcn.append(el)
            if len(el[2]) < i: continue
            e_max = el[2][i-1] if i >= 1 else int(log(MAXN, 2))
            n = el[0]
            for e in range(1, e_max+1):
                n *= list_p[i]
                if n > MAXN: break
                div = el[1] * (e+1)
                exponents = el[2] + [e]
                new_hcn.append((n, div, exponents))
        new_hcn.sort()
        hcn = [(1, 1, [])]
        for el in new_hcn:
            if el[1] > hcn[-1][1]: hcn.append(el)
    return hcn

hcn = gen_hcn()

list_hcn = [] # Những số HCN <= MAXN
for el in hcn:
    list_hcn.append(el[0])

t = int(input())
i = 0
for line in sys.stdin:
    n = int(line)
    i += 1
    print(list_hcn[bisect_left(list_hcn, n)])
    if i == t: break