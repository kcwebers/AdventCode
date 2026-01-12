# --- Part Two ---
# The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

# The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

# Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

# More of the above example's reports are now safe:

# 7 6 4 2 1: Safe without removing any level.
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.
# Thanks to the Problem Dampener, 4 reports are actually safe!

# Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

# MUST either be increasing or decreasing
# MUST only increase/decrease by 1-3 (inclusive)
# dupes can happen, if one of the dupes can be removed and pass a safe test
# 1 increase / decrease in contrast can happen but only if one item can be removed and maintain overall pattern

from variables import inputs_day02

# different approach: have a contained function that determines safe / unsafe and return True or False
# THEN count the number of True returns

def safety_check(report):
    # takes in a single list (report) and checks for parameters
    if report[0] < report[1]:
            i = 0
            # O(N)
            while (i < len(report) - 1) and (report[i] < report[i+1]):
                # print("still safe")
                if report[i+1] - report[i] > 3:
                    # print("ope not safe anymore")
                    return False
                # no need to check the final number, just need to check final number against the second-to-last number
                if i == len(report) - 2:
                    return True
                i += 1
        # decreasing report
    if report[0] > report[1]:
        i = 0
        # O(N)
        while (i < len(report) - 1) and (report[i] > report[i+1]):
            # print("still safe")
            if report[i] - report[i+1] > 3:
                # print("ope not safe anymore")
                return False
            # no need to check the final number, just need to check final number against the second-to-last number
            if i == len(report) - 2:
                return True
            i += 1
    return False


def check_for_anomalies(input_str):
    # count safe reports 
    safe_count = 0
    # convert data into usable list
    reports = input_str.split("\n")

    for r in reports:
        # convert values from string to int to be more usable
        report = [int(i) for i in r.split(" ")]
        # print(report)
        if safety_check(report):
            safe_count += 1
            # print("safe")
        else:
            failures = 0
            for i in range(len(report)):
                # list create new list with each element as long as it is not located at the current spot in the list
                new_report = [report[x] for x in range(len(report)) if x != i]
                # print(new_report)
                # check this new list to see if it still fails
                if safety_check(new_report) == False:
                    failures += 1
            # if safety check DID NOT fail every time (for the length of the report), then it now passes!
            if failures < len(report):
                safe_count += 1

    return safe_count


fake = """25 26 29 30 32 35 37 35
15 16 17 20 22 24 26 26
80 81 83 85 89
76 77 79 82 84 87 89 95
73 75 78 81 83 84 81 84
9 10 11 12 11 8
27 28 30 33 35 34 37 37
67 70 69 72 74 78"""

print(check_for_anomalies(inputs_day02))