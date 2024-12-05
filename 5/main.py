rules = {} #In format {page_num:[all_pages_that_come_before_it]}
with open("rules.txt", "r") as file:
    for line in file:
        rule = line.split("|")
        if int(rule[0]) in rules:
            rules[int(rule[0])].append(int(rule[1]))
        else:
            rules[int(rule[0])] = [int(rule[1])]

updates = []
with open("updates.txt", "r") as file:
    for line in file:
        split_update = line.split(",")
        updates.append([int(x) for x in split_update])

def update_is_valid(update):
    for page_idx in range(len(update)):
        if update[page_idx] in rules and any(item in update[:page_idx] for item in rules[update[page_idx]]):
            return False
    return True

# Part 1
middle_num_sum = 0
for update in updates:
   if update_is_valid(update):
       middle_num_sum += update[len(update)//2]

print(middle_num_sum)

# Part 2
def find_repaired_update(bad_update):
    corrected_update = []
    for update in bad_update:
        idx_to_insert = len(corrected_update)
        for cupdate_idx in range(len(corrected_update)):
            if update in rules and corrected_update[cupdate_idx] in rules[update]:
                idx_to_insert = cupdate_idx
                break
        corrected_update.insert(idx_to_insert, update)
    return corrected_update

middle_num_sum = 0
for update in updates:
   if not update_is_valid(update):
       repaired_update = find_repaired_update(update)
       middle_num_sum += repaired_update[len(repaired_update)//2]

print(middle_num_sum)


