import re
import functools

with open("input.txt", "r") as file:
    corrupted_data = file.read().replace("\n", "")

def perform_mul_on_data(data):
    mul_opening = re.escape("mul(")
    mul_inner_comma = re.escape(",")
    mul_closing = re.escape(")")

    matches = re.findall(mul_opening + r"\d+" + mul_inner_comma + r"\d+" + mul_closing, data)

    total = 0

    for match in matches:
        num_1 = int(match.split("mul(")[1].split(",")[0])
        num_2 = int(match.split(",")[1].split(")")[0])
        total += num_1 * num_2

    return total

#Part 1
print(perform_mul_on_data(corrupted_data))

#Part 2
deactivation_re = re.escape("don't()")
activation_re = re.escape("do()")

enabled_corrupted_data = re.sub(deactivation_re + r".*?" + activation_re, '', corrupted_data)

trailing_dont_block_split = enabled_corrupted_data.rsplit("do()", 1)[-1].split("don't()", 1)

if len(trailing_dont_block_split) > 1:
    enabled_corrupted_data = enabled_corrupted_data.replace(trailing_dont_block_split[1], '') #Remove data after a trailing "don't()"

print(perform_mul_on_data(enabled_corrupted_data))

