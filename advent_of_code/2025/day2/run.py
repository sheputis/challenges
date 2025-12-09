INPUT_FILE ='input.txt'

f = open(INPUT_FILE)

def check(size, string, n):
    partition_len = int(size/n)
    partition = string[0:partition_len]
    for k in range(1, n):
        start = k * partition_len
        end   = start + partition_len
        if partition != string[start:end]:
            return False
    return True

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

        if check(i_len, i_str, 2):
            #invalid_numbers.append(i) FOR DEBUGGING
            result_sum += i

#print(invalid_numbers) FOR DEBUGGING
print(result_sum) # 17077011375

# PART 2

f = open(INPUT_FILE)
#invalid_numbers = [] #FOR DEBUGGING
result_sum = 0
for range_str in f.read().split(','):
    a = 1
    start, end = [int(number) for number in range_str.split('-')]
    for i in range(start, end + 1):
        i_str = str(i)
        i_len = len(i_str)

        for n in range(2, i_len + 1):
            if i_len % n == 0:
                if check(i_len, i_str, n):
                    # invalid_numbers.append(i) #FOR DEBUGGING
                    result_sum += i
                    break

#print(invalid_numbers) #FOR DEBUGGING
print(result_sum) # 36037497037
