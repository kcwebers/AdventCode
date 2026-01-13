# "Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

# The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

# The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

# It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

# However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

# For example, consider the following section of corrupted memory:

# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

# Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

from variables import inputs_day03
import re

# looking for a specific pattern in string
# "mul(###,###)"
# add together the total of all valid patterns


def find_valid_multiples(input_string):
    # use regex to locate all occurrences of the pattern specified

    # pattern looks for string that starts with mul(), and only contains numbers 1-3 digits lone
    # regex_pattern = r'mul\(\d{1,3},\d{1,3}\)'

    # this pattern only pulls the numbers, but keeps the same parameters for searching
    regex_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    valid_multiples = re.findall(regex_pattern, input_string)
    multiples = [(int(a), int(b)) for a, b in valid_multiples]
    return multiples

def sum_of_multiples(input):
    # loop through list of valid multiples and find the product of the 2 numbers
    # add all together to find the final sum

    total = 0

    valid_multiples = find_valid_multiples(input)

    for number_pair in valid_multiples:
        total += (number_pair[0] * number_pair[1])

    return total

# sample_str = "}mul(620,236)where()*@}!&[mul(589,126)]&^]mul(260,42)"
# print(find_valid_multiples(sample_str))

print(sum_of_multiples(inputs_day03))