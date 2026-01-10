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


def check_for_safety(input):
    # count safe reports 
    count = 0
    # convert data into usable list
    reports = input.split("\n")

    # loop through reports and convert each line 
    for r in reports:
        # convert values from string to int to be more usable
        report = [int(i) for i in r.split(" ")]
        # print(report)
        # if len(report) != len(set(report)):
        #     print("unsafe")
        #     continue
        # increasing report
        if report[0] < report[1]:
            i = 0
            problem_count = 0
            # O(N)
            while i < len(report) - 1:
                # if you encounter an issue, remove it from the report and recheck same step
                if report[i] > report[i+1] or report[i] == report[i+1] or report[i+1] - report[i] > 3:
                    if problem_count == 0:
                        print("found anomaly")
                        report.remove(report[i+1])
                        problem_count += 1
                        # i stays the same so we can recheck against next element after removal of anomaly
                        continue
                    else:
                        print("ope not safe anymore")
                        break
                # no need to check the final number, just need to check final number against the second-to-last number
                # if made it through all checks, count as safe!
                if i == len(report) - 2:
                    count += 1
                # made it through iteration without failing safety check, or completing report check
                i += 1
        # decreasing report
        if report[0] > report[1]:
            i = 0
            problem_count = 0
            # O(N)
            while i < len(report) - 1:
                print("still safe")
                if report[i] < report[i+1] or report[i] == report[i+1] or report[i] - report[i+1] > 3:
                    if problem_count == 0:
                        print("found anomaly")
                        report.remove(report[i+1])
                        problem_count += 1
                        # i stays the same so we can recheck against next element after removal of anomaly
                        continue
                    else:
                        print("ope not safe anymore")
                        # break out of loop and don't count towards safe reports
                        break
                # no need to check the final number, just need to check final number against the second-to-last number
                # if made it through all checks, count as safe!
                if i == len(report) - 2:
                    count += 1
                # made it through iteration without failing safety check, or completing report check
                i += 1
    return count

print(check_for_safety(inputs_day02))