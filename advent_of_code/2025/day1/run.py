
FILE_NAME = 'input_1.txt'

# PART 1
f = open(FILE_NAME, 'r')
current_number = 50
zero_count = 0
for line in f:
    letter = line[0]
    number = int(line[1:].strip())
    if letter == 'R':
        current_number += number
    else:
        current_number -= number

    current_number = current_number % 100

    if current_number == 0:
        zero_count += 1

print(zero_count)

# PART 2 BRUTE FORCE for testing O(n*m) where m is the size highest number in the sequence

f = open(FILE_NAME, 'r')
current_number = 50
zero_count = 0

for line in f:
    letter = line[0]
    number = int(line[1:].strip())

    for i in range(number):
        if letter == 'R':
            current_number += 1
        else:
            current_number -= 1
        current_number = current_number % 100
        if current_number == 0:
            zero_count += 1

print(zero_count)

# PART 2

f = open(FILE_NAME, 'r')
current_number = 50
zero_count = 0

for line in f:
    letter = line[0]
    number = int(line[1:].strip())

    if letter == 'R':
        current_number += number
        quotient = int(current_number / 100)
        zero_count += quotient
    else:
        if current_number == 0:
            current_number = 100
        current_number -= number
        if current_number < 1:
            quotient = int(abs(current_number) / 100)
            zero_count += quotient + 1

    current_number = current_number % 100

print(zero_count)
