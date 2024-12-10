import itertools
grid = []

with open("input.txt", "r") as file:
    for line in file:
        grid.append(list(line.replace('\n', '')))

grid_height = len(grid)
grid_width = len(grid[0])

def get_antinodes_from_positions(grid_height, grid_width, positions, include_resonance):
    position_combinations_hashtag_ariannaaaaaaa = list(itertools.combinations(positions, 2))
    antinode_positions = []

    for combination in position_combinations_hashtag_ariannaaaaaaa:
        x1 = combination[0][0]
        x2 = combination[1][0]
        y1 = combination[0][1]
        y2 = combination[1][1]
        if x1 < x2:
            antinode_x_1 = min(x1, x2) - abs(x2 - x1)
            antinode_x_2 = max(x1, x2) + abs(x2 - x1)
        else:
            antinode_x_1 = max(x1, x2) + abs(x2 - x1)
            antinode_x_2 = min(x1, x2) - abs(x2 - x1)
        antinode_y_1 = min(y1, y2) - abs(y2 - y1)
        antinode_y_2 = max(y1, y2) + abs(y2 - y1)
        antinode_positions.append((antinode_x_1, antinode_y_1))
        antinode_positions.append((antinode_x_2, antinode_y_2))
        if include_resonance:
            antinode_positions.append((x1, y1))
            antinode_positions.append((x2, y2))
            x1_step = (antinode_x_1 - x1)
            y1_step = (antinode_y_1 - y1)
            x2_step = (antinode_x_2 - x2)
            y2_step = (antinode_y_2 - y2)
            while (0 <= antinode_x_1 < grid_width) or (0 <= antinode_x_2 < grid_width) or (0 <= antinode_y_1 < grid_height) or (0 <= antinode_y_2 < grid_height):
                antinode_x_1 = antinode_x_1 + x1_step
                antinode_y_1 = antinode_y_1 + y1_step
                antinode_x_2 = antinode_x_2 + x2_step
                antinode_y_2 = antinode_y_2 + y2_step
                antinode_positions.append((antinode_x_1, antinode_y_1))
                antinode_positions.append((antinode_x_2, antinode_y_2))
    return [position for position in antinode_positions if (0 <= position[0] < grid_width) and (0 <= position[1] < grid_height)]

antenna_positions = {} # {letter: [positions]}

#Get antenna positions
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != ".":
            if grid[y][x] in antenna_positions:
                antenna_positions[grid[y][x]].append((x,y))
            else:
                antenna_positions[grid[y][x]] = [(x,y)]

# Part 1
antinode_positions = set()
for frequency, positions in antenna_positions.items():
    antinode_positions.update(get_antinodes_from_positions(grid_height, grid_width, positions, False))
print(len(antinode_positions))

# Part 2
antinode_positions = set()
for frequency, positions in antenna_positions.items():
    antinode_positions.update(get_antinodes_from_positions(grid_height, grid_width, positions, True))
print(len(antinode_positions))