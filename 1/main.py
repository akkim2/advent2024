left_list = []
right_list = []

with open("input.txt", "r") as file:
    for line in file:
        split_line = line.split("   ")
        left_list.append(int(split_line[0]))
        right_list.append(int(split_line[1]))

sorted_left_list = sorted(left_list)
sorted_right_list = sorted(right_list)

#Part 1

total = 0

for x in range(len(sorted_left_list)):
    total = total + abs(sorted_right_list[x] - sorted_left_list[x])

print(total)


#Part 2
import collections

right_list_number_frequency = collections.Counter(right_list)

total = 0

for x in range(len(sorted_left_list)):
    total = total + (sorted_left_list[x] * right_list_number_frequency[sorted_left_list[x]])

print(total)