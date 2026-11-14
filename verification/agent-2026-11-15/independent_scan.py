#!/usr/bin/env python3
"""Independent y-interval search for extremal 4/n Egyptian fractions.

No factorization, divisor generation, or repository imports are used.
Integers only; candidate y's are enumerated in increasing order.
"""
from fractions import Fraction
from time import perf_counter
import argparse


def maximize(n, *, prune=True):
    record = 0
    witnesses = []
    tested = 0
    visited_x = 0
    for x in range(n // 4 + 1, (3 * n - 1) // 4 + 1):
        alpha = 4 * x - n
        beta = n * x
        first = max(x + 1, beta // alpha + 1)
        last = (2 * beta - 1) // alpha  # y < 2 beta / alpha, strictly
        if first > last:
            continue
        visited_x += 1
        if prune and beta * first < record * (alpha * first - beta):
            continue
        for y in range(first, last + 1):
            denominator = alpha * y - beta
            numerator = beta * y
            if prune and numerator < record * denominator:
                break  # z is strictly decreasing as y increases
            tested += 1
            quotient, remainder = divmod(numerator, denominator)
            if remainder or quotient <= y:
                continue
            if quotient > record:
                record = quotient
                witnesses = []
            if quotient == record:
                witnesses.append((x, y, quotient))
    return witnesses, tested, visited_x


def valid(n, triple):
    x, y, z = triple
    return (0 < x < y < z and
            Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--end', type=int, default=5000)
    args = parser.parse_args()
    assert args.end >= 2000
    begin = perf_counter()
    print('METHOD: independent direct search over y with an exact upper-bound stopping rule; no factorization', flush=True)
    print(f'RANGE: n=3..{args.end}', flush=True)
    failures_2000 = []
    failures_later = []
    ties_2000 = []
    ties_later = []
    checked_y = 0
    visited_x = 0
    x_above_floor_plus_two = []
    for n in range(3, args.end + 1):
        best, tested, xs = maximize(n)
        checked_y += tested
        visited_x += xs
        if not best or any(not valid(n, triple) for triple in best):
            raise AssertionError(('missing or invalid maximum', n, best))
        best_x = min(t[0] for t in best)
        allowed = {n // 4 + 1, n // 4 + 2} if n % 8 == 1 else {n // 4 + 1}
        if best_x not in allowed:
            (failures_2000 if n <= 2000 else failures_later).append((n, best_x))
        if best_x > n // 4 + 2:
            x_above_floor_plus_two.append((n, best_x))
        if len(best) > 1:
            (ties_2000 if n <= 2000 else ties_later).append((n, best))
        if n in (17, 73, 409, 2000, args.end):
            print(f'CHECKPOINT n={n}, winners={best}', flush=True)
        if n in (17, 73, 409):
            exhaustive, direct_trials, _ = maximize(n, prune=False)
            assert sorted(exhaustive) == sorted(best), (n, exhaustive, best)
            print(f'FULL_UNPRUNED n={n}, winners={exhaustive}, examined_y={direct_trials}', flush=True)
    print(f'FAILURES_3_2000 count={len(failures_2000)}: {failures_2000}', flush=True)
    print(f'FAILURES_2001_{args.end} count={len(failures_later)}: {failures_later}', flush=True)
    print(f'TIES_3_2000 count={len(ties_2000)}: {ties_2000}', flush=True)
    print(f'TIES_2001_{args.end} count={len(ties_later)}: {ties_later}', flush=True)
    print(f'X_GT_FLOOR_PLUS_2 count={len(x_above_floor_plus_two)}: {x_above_floor_plus_two}', flush=True)
    print(f'CANDIDATES_TESTED={checked_y} X_INTERVALS={visited_x}', flush=True)
    print(f'RUNTIME_SECONDS={perf_counter()-begin:.6f}', flush=True)
    print('STATUS=PASS', flush=True)


if __name__ == '__main__':
    main()
