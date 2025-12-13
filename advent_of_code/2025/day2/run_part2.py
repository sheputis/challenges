"""Solves the second part of the AoC 2025 day 2 problem."""

import time
from prime_numbers import resolve_prime_numbers

INPUT_FILE = 'input.txt'

# PART 2


def main():
    """
    Loops over ranges like 11-50, 1200-1255, and so on and selects the ones
    that have repeating patterns, lke 11, 44, 1212 and so on.
    """
    prime_numbers = [2]
    prime_numbers_map = {}

    result_nums = []

    f = open(INPUT_FILE)

    for range_str in f.read().split(','):
        start_str, end_str = range_str.split('-')
        ranges_per_digit_count = [[start_str]]
        for k in range(len(start_str), len(end_str)):
            ranges_per_digit_count[-1].append('9'*k)
            ranges_per_digit_count.append(['1' + '0' * k])
        ranges_per_digit_count[-1].append(end_str)

        for start_str, end_str in ranges_per_digit_count:
            n = len(start_str)
            total_lower = int(start_str)
            total_upper = int(end_str)
            n_primes = prime_numbers_map.get(n)
            if n_primes is None:
                n_primes = prime_numbers_map[n] = resolve_prime_numbers(n, prime_numbers)
            for n_prime in n_primes:
                partition_size = int(n / n_prime)
                lower = int(start_str[0:partition_size])
                upper = int(end_str[0:partition_size])
                for val in range(lower, upper + 1):
                    val_int = int(str(val) * n_prime)
                    if (total_lower <= val_int) and (val_int <= total_upper):
                        result_nums.append(val_int)

    result_nums = set(result_nums)

    sumsies = 0
    for el in result_nums:
        sumsies += int(el)
    print(sumsies)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Runtime: {end_time - start_time:.6f} seconds")

# Answer: 36037497037
# Before ading prime number approach: the median after 9 runs: 5.350 s
# With the prime number approach: ~ 3 s
# With the non-looping approach: ~ 1.3 ms
