"""Solves the second part of the AoC 2025 day 2 problem."""

import time
from compare_substrings import compare_substrings

INPUT_FILE = 'input.txt'

# PART 2

f = open(INPUT_FILE)


def main():
    """
    Loops over ranges like 11-50, 1200-1255, and so on and selects the ones
    that have repeating patterns, lke 11, 44, 1212 and so on.
    """
    result_sum = 0
    for range_str in f.read().split(','):
        start, end = [int(number) for number in range_str.split('-')]
        for i in range(start, end + 1):
            i_str = str(i)
            i_len = len(i_str)

            for n in range(2, i_len + 1):
                if i_len % n == 0:
                    if compare_substrings(i_len, i_str, n):
                        result_sum += i
                        break
    print(result_sum)


if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Runtime: {end_time - start_time:.3f} seconds")

# Answer: 36037497037
# the median after 9 runs: 5.350 s
