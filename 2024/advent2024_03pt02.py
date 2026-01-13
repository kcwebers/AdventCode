# --- Part Two ---
# As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

# There are two new instructions you'll need to handle:

# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.
# Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

# For example:

# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

# This time, the sum of the results is 48 (2*4 + 8*5).

# Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?

from variables import inputs_day03
import re

# looking for a specific pattern in string
# "mul(###,###)"
# add together the total of all valid patterns

# new parameters == need to enable / disable multiplier based on preceding ido or don't

def find_valid_multiples(input_string):
    # use regex to locate all occurrences of the pattern specified
    # regex will find the standard mul(###,###) OR do() OR don't()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"

    # switch to track whether or not the functions dp() or dont() have enabled the mul()
    enabled = True
    valid_multiples = []

    for match in re.finditer(pattern, input_string):
        # print(match)
        # print(match.group(0))
        # print(match.groups())
        instruction = match.group(0)
        
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif instruction.startswith("mul") and enabled:
            nums = match.groups()
            valid_multiples.append((int(nums[0]), int(nums[1])))
    return valid_multiples

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