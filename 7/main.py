import itertools

calibration_results = {} #Format is {calibration_result:[values]}

with open("input.txt", "r") as file:
    for line in file:
        split_line = line.split(": ")
        calibration_results[int(split_line[0])] = [ int(x) for x in split_line[1].split(" ") ]

def number_concat(a,b):
    return int(str(a) + str(b))

def get_new_accumulated_result(operator, a ,b):
    if operator == "+":
        return a + b
    elif operator == "*":
        return a * b
    else:
        return number_concat(a, b)

def check_if_value_is_possible(result, values, can_concat):
    operators = ['+', '*', '||'] if can_concat else ['+', '*']
    possible_operator_order = list(itertools.product(operators, repeat=len(values)))
    for order in possible_operator_order:
        accumulated_result = get_new_accumulated_result(order[0], values[0], values[1])
        for value_idx in range(2, len(values)):
            accumulated_result = get_new_accumulated_result(order[value_idx], accumulated_result, values[value_idx])
        if accumulated_result == result:
            return True
    return False

# Part 1
possible_calibration_results = [result if check_if_value_is_possible(result, values, False) else 0 for result, values in calibration_results.items()]
print(sum(possible_calibration_results))

#Part 2
possible_calibration_results = [result if check_if_value_is_possible(result, values, True) else 0 for result, values in calibration_results.items()]
print(sum(possible_calibration_results))