lines = []

with open("input.txt", "r") as file:
    for line in file:
        lines.append(list(line.replace('\n', '')))

grid_height = len(lines)
grid_width = len(lines[0])

def spells_xmas(x, m, a, s):
    if x == "X" and m == "M" and a == "A" and s == "S":
        return True
    return False

#Part 1
xmas_occurances = 0

for y in range(grid_height):
    for x in range(grid_width):
        if lines[y][x] == "X":
            # Check for written forwards
            if x+3 < grid_width and spells_xmas(lines[y][x], lines[y][x+1], lines[y][x+2], lines[y][x+3]):
                xmas_occurances += 1
            # Check for written backwards
            if x-3 >= 0 and spells_xmas(lines[y][x], lines[y][x-1], lines[y][x-2], lines[y][x-3]):
                xmas_occurances += 1
            # Check for vertical up
            if y-3 >= 0 and spells_xmas(lines[y][x], lines[y-1][x], lines[y-2][x], lines[y-3][x]):
                xmas_occurances += 1
            # Check for vertical down
            if y+3 < grid_height and spells_xmas(lines[y][x], lines[y+1][x], lines[y+2][x], lines[y+3][x]):
                xmas_occurances += 1
            # Check for diagonal down-left
            if y+3 < grid_height and x-3 >= 0 and spells_xmas(lines[y][x], lines[y+1][x-1], lines[y+2][x-2], lines[y+3][x-3]):
                xmas_occurances += 1
            # Check for diagonal down-right
            if y+3 < grid_height and x+3 < grid_width and spells_xmas(lines[y][x], lines[y+1][x+1], lines[y+2][x+2], lines[y+3][x+3]):
                xmas_occurances += 1
            # Check for diagonal up-left
            if y-3 >= 0 and x-3 >= 0 and spells_xmas(lines[y][x], lines[y-1][x-1], lines[y-2][x-2], lines[y-3][x-3]):
                xmas_occurances += 1
            # Check for diagonal up-right
            if y-3 >= 0 and x+3 < grid_width and spells_xmas(lines[y][x], lines[y-1][x+1], lines[y-2][x+2], lines[y-3][x+3]):
                xmas_occurances += 1
print(xmas_occurances)


#Part 2
xmas_occurances = 0

for y in range(grid_height):
    for x in range(grid_width):
        if lines[y][x] == "A":
            if y-1 >= 0 and y+1 < grid_height and x-1 >= 0 and x+1 < grid_width:
                upper_left_to_bottom_right_diagonal = lines[y-1][x-1] + lines[y][x] + lines[y+1][x+1]
                upper_right_to_bottom_left_diagonal = lines[y-1][x+1] + lines[y][x] + lines[y+1][x-1]
                if upper_left_to_bottom_right_diagonal in ['MAS','SAM'] and upper_right_to_bottom_left_diagonal in ['MAS','SAM']:
                    xmas_occurances += 1

print(xmas_occurances)