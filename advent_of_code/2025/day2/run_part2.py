import time
from compare_substrings import compare_substrings

INPUT_FILE ='input.txt'

# PART 2

f = open(INPUT_FILE)
#invalid_numbers = [] #FOR DEBUGGING
def main():
    result_sum = 0
    for range_str in f.read().split(','):
        start, end = [int(number) for number in range_str.split('-')]
        for i in range(start, end + 1):
            i_str = str(i)
            i_len = len(i_str)

            for n in range(2, i_len + 1):
                if i_len % n == 0:
                    if compare_substrings(i_len, i_str, n):
                        # invalid_numbers.append(i) #FOR DEBUGGING
                        result_sum += i
                        break

    #print(invalid_numbers) #FOR DEBUGGING
    print(result_sum) # 36037497037

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Runtime: {end - start:.3f} seconds") # the median after 9 runs: 5.350 s