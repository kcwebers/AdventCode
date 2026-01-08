# --- Part Two ---
# Your analysis only confirmed what everyone feared: the two lists of location IDs are indeed very different.

# Or are they?

# The Historians can't agree on which group made the mistakes or how to read most of the Chief's handwriting, but in the commotion you notice an interesting detail: a lot of location IDs appear in both lists! Maybe the other numbers aren't location IDs at all but rather misinterpreted handwriting.

# This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

# Here are the same example lists again:

# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# For these example lists, here is the process of finding the similarity score:

# The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
# The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
# The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
# The fourth number, 1, also does not appear in the right list.
# The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
# The last number, 3, appears in the right list three times; the similarity score again increases by 9.
# So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

# Once again consider your left and right lists. What is their similarity score?

from inputs_01 import provided_values

# see site for real input
list_of_locations = provided_values

# this is very labor intensive
# instead of splitting string, can parse through string directly
def convert_input(input):
    # convert wall of numbers to usable format

    # creates new list of strings formatted "num1   num2"
    converted = input.split("\n")

    # pool numbers into 2 usable lists
    list1 = []
    list2 = []
    for value in converted:
        num_pair = value.split("   ")
        list1.append(int(num_pair[0]))
        list2.append(int(num_pair[1]))

    # print(list1)
    # print(list2)

    return list1, list2

# convert_input(list_of_locations)

def how_much_similarity(given_input):
    total_similarity = 0
    
    # convert given input into usable lists
    list1, list2 = convert_input(given_input)

    # sort lists
    # iterate through SECOND list to find duplicates of value in first list
    # track number of occurrences and multiply num by that number

    # sort lists min to max
    # # O(NLog(N))
    # list1.sort()
    # # O(NLog(N))
    # list2.sort()

    count = {}
    # O(N)
    for value in list2:
        if value in count:
            count[value] += 1
        else:
            count[value] = 1

    # print(count)

    # loop through list one and check if value in KEYS of count variable
    # if in keys, then mult by value
    # if not them mult by 0
    for value in list1:
        if value in count:
            total_similarity += value * count[value]



    # # multiply each value by the number of occurrences of that value in list2
    # # O(N)
    # for value in list1:
    #     # O(N)
    #     total_similarity += (int(value) * list2.count(value))
    # Total Complexity O(N^2)

    return total_similarity

print(how_much_similarity(list_of_locations))
