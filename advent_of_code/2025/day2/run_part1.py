from compare_substrings import compare_substrings

INPUT_FILE ='input.txt'

f = open(INPUT_FILE)

#invalid_numbers = [] FOR DEBUGGING
result_sum = 0
for range_str in f.read().split(','):
    start, end = [int(number) for number in range_str.split('-')]
    #print(start, " - ", end)
    for i in range(start, end + 1):
        i_str = str(i)
        i_len = len(i_str)
        if i_len % 2 == 1:
            continue

        if compare_substrings(i_len, i_str, 2):
            #invalid_numbers.append(i) FOR DEBUGGING
            result_sum += i

#print(invalid_numbers) FOR DEBUGGING
print(result_sum) # 17077011375
