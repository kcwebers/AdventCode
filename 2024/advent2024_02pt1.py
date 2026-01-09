# --- Day 2: Red-Nosed Reports ---
# Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

# While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

# They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

# The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# This example data contains six reports each containing five levels.

# The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
# In the example above, the reports can be found safe or unsafe by checking those rules:

# 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
# 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
# 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
# 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
# 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
# 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
# So, in this example, 2 reports are safe.

# Analyze the unusual data from the engineers. How many reports are safe?

from variables import inputs_day02

def convert_str_to_dict(input_str):
    # convert a string of numbers into a dict
    # keys = report number
    # values = list of values

    # split string into list of 'report' strings, then store info in dict

    list_of_str, dict_of_reports = input_str.split("\n"), {}
    for i in range(len(list_of_str)):
        dict_of_reports[i] = [int(i) for i in list_of_str[i].split()]
    return dict_of_reports

# print(convert_str_to_dict(inputs_day02))

def count_safe_reports(input):
    # convert data to dictionary of lists
    map_of_reports = convert_str_to_dict(input)
    count = 0
    # access each report and check list 
    # MUST either be increasing or decreasing
    # MUST only increase/decrease by 1-3 (inclusive)
    # this means a list cannot contain duplicates!

    # O(N)
    for report in map_of_reports.values():
        print(report)

        # no dupes in my town
        if len(report) != len(set(report)):
            print("unsafe")
            continue

        # increasing report
        if report[0] < report[1]:
            i = 0
            # O(N)
            while (i < len(report) - 1) and (report[i] < report[i+1]):
                print("still safe")
                if report[i+1] - report[i] > 3:
                    print("ope not safe anymore")
                    i += 1
                    break
                # no need to check the final number, just need to check final number against the second-to-last number
                if i == len(report) - 2:
                    i += 1
                    count += 1
                i += 1

        # decreasing report
        if report[0] > report[1]:
            i = 0
            # O(N)
            while (i < len(report) - 1) and (report[i] > report[i+1]):
                print("still safe")
                if report[i] - report[i+1] > 3:
                    print("ope not safe anymore")
                    i += 1
                    break
                # no need to check the final number, just need to check final number against the second-to-last number
                if i == len(report) - 2:
                    i += 1
                    count += 1
                i += 1

    # O(N^2) yikes
    return count

print(count_safe_reports(inputs_day02))
