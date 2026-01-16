# --- Day 4: Ceres Search ---
# "Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

# As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

# This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....
# The actual word search will be full of letters instead. For example:

# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX

# In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

# ....XXMAS.
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
# Take a look at the little Elf's word search. How many times does XMAS appear?

# assumption: rows are of uniform length, filled only with capital letters

# input is a block of text with consistent line lengths
# can break information into a matrix? no need to double split, just split once to get uniform rows of strings, then iterate through
# check up, down, diagonal both forward and back
# look for an x and then search the directions based on location in matrix 
# - x must be at least in 4th row for upwards, upwards diagonals
# - x must be at least in 4th spot for backwards, backwards diagonal
# - x must be at least 4 from end for diagonal forward

from variables import inputs_day04

def find_xmas_count(input):
    # create matrix to run through
    matrix = input.split("\n")
    # count for total number of "xmas"
    total_xmas = 0
    # strings we are looking for
    words = ["XMAS", "SAMX"]

    # loop through and find the "x" and then continue searching
    # loop into each row (r) 
    for r in range(len(matrix)):
        # loop to check each individual letter based on position in string (c for column; this is where the row/col meet)
        for c in range(len(matrix[r])):
            # print(r[i])

            # find "XMAS" forward (sample = 3)
            if matrix[r][c:(c+4)] in words:
                total_xmas += 1
            # find "XMAS" vertically (sample = 1)
            if r < (len(matrix) - 3):
                if "".join(letter[c] for letter in matrix[r:(r+4)]) in words:
                    total_xmas += 1
                # find "XMAS" vertical forwards (sample = 1)
                if c < (len(matrix[r]) - 3): 
                    # create a string comprised of the initial "x" found and iterations upwards
                    # print("".join(matrix[r + l][i + l] for l in range(4)))
                    if "".join(matrix[r + i][c + i] for i in range(4)) in words:
                        total_xmas += 1
                # find "XMAS" vertical backwards (sample = 1)
                if c >= 3:
                    # create a string comprised of the initial "x" found and iterations upwards
                    # print("".join(matrix[r + l][i + l] for l in range(4)))
                    if "".join(matrix[r + i][c - i] for i in range(4)) in words:
                        total_xmas += 1

    return total_xmas

sample = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

print(find_xmas_count(sample))
print(find_xmas_count(inputs_day04))