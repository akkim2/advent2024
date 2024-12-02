reports = []

with open("input.txt", "r") as file:
    for line in file:
        split_line = line.split(" ")
        reports.append([ int(x) for x in split_line ])

def level_satisfies_checks(current_level, next_level, should_ascend):
    maintains_direction = True if (next_level > current_level) == should_ascend else False
    level_difference_in_range = True if 0 < abs(next_level-current_level) <= 3 else False
    return all([maintains_direction, level_difference_in_range])

def find_first_potentially_problematic_levels(report):
    """
    Determines if a report is safe
    :param report: The report to verify
    :return: List of first two-three detected potentially problematic levels, if any
    """
    should_ascend = True if report[1] > report[0] else False  # set initial direction
    for level in range(len(report) - 1):
        if not level_satisfies_checks(report[level], report[level + 1], should_ascend):
            return [level - 1, level, level + 1] if level > 0 else [level, level + 1]
    return []

#Part 1

num_safe_reports = 0

for report in reports:
    if len(find_first_potentially_problematic_levels(report)) == 0:
        num_safe_reports = num_safe_reports + 1

print(num_safe_reports)

#Part 2

def pop_and_remove(arr, index):
    arr.pop(index)
    return arr

num_safe_reports = 0

for report in reports:
    first_problematic_levels = find_first_potentially_problematic_levels(report)
    if len(first_problematic_levels) == 0:
        num_safe_reports = num_safe_reports + 1
    else:
        #Try removing each suggested problematic level and see if the report is safe
        level_removal_tries = []
        for level_index in first_problematic_levels:
            level_removal_tries.append(
                len(find_first_potentially_problematic_levels(pop_and_remove(report.copy(), level_index)))==0
            )
        if any(level_removal_tries):
           num_safe_reports = num_safe_reports + 1

print(num_safe_reports)
