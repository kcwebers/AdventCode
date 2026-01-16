# --- Part Two ---
# The Elf looks quizzically at you. Did you misunderstand the assignment?

# Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

# M.S
# .A.
# M.S
# Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

# Here's the same example from before, but this time all of the X-MASes have been kept instead:

# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
# In this example, an X-MAS appears 9 times.

# Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?

# list of possibilities:
# M.S   M.M   S.M   S.S
# .A.   .A.   .A.   .A.
# M.S   S.S   S.M   M.M

# can concatenate to check for "MSAMS", "MMASS", "SMASM", "SSAMM"


from variables import inputs_day04

def find_x_mas_count(input):
    # create matrix to run through
    matrix = input.split("\n")
    # count for total number of "xmas"
    total_x_mas = 0
    # strings we are looking for
    words = ["MSAMS", "MMASS", "SMASM", "SSAMM"]

    # loop through and find the "x" and then continue searching
    # loop into each row (r) 
    for r in range(len(matrix)):
        # loop to check each individual letter based on position in string (c for column; this is where the row/col meet)
        for c in range(len(matrix[r])):
            # print(r[i])
            if r < (len(matrix) - 2) and c < (len(matrix[r]) - 2):
                # print("".join([matrix[r][c], matrix[r][c+2], matrix[r+1][c+1], matrix[r+2][c], matrix[r+2][c+2]]))
                if "".join([matrix[r][c], matrix[r][c+2], matrix[r+1][c+1], matrix[r+2][c], matrix[r+2][c+2]]) in words:
                    total_x_mas += 1

    return total_x_mas

sample = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

print(find_x_mas_count(sample))
print(find_x_mas_count(inputs_day04))