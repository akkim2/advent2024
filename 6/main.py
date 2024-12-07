grid = []

with open("input.txt", "r") as file:
    for line in file:
        grid.append(list(line.replace('\n', '')))

grid_height = len(grid)
grid_width = len(grid[0])

def get_guard_position(grid):
    """
    Gets the guard's position
    :param grid: The map
    :return: (x,y) 0-indexed coordinates of the guard's position
    """
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in ["^", ">", "v", "<"]:
                return x,y

def get_new_guard_direction_if_needed(grid, guard_direction, current_position):
    """
    Checks if the guard needs to change direction, and returns the direction if so
    :param guard_direction: The current guard direction
    :param current_position: The current position of the guard
    """
    match guard_direction:
        case "^":
            if current_position[1] - 1 >= 0 and grid[current_position[1] - 1][current_position[0]] == "#":
               return ">"
            else:
                return guard_direction
        case ">":
            if current_position[0] + 1 < grid_width and grid[current_position[1]][current_position[0] + 1] == "#":
                return "v"
            else:
                return guard_direction
        case "v":
            if current_position[1] + 1 < grid_height and grid[current_position[1] + 1][current_position[0]] == "#":
                return "<"
            else:
                return guard_direction
        case "<":
            if current_position[0] - 1 >=0 and grid[current_position[1]][current_position[0] - 1] == "#":
               return "^"
            else:
                return guard_direction

def get_next_guard_coord(guard_direction, current_position):
    """
    Returns the next coordinate that guard should go to
    :param guard_direction: The current guard direction
    :param current_position: The current position of the guard
    :return: The new (x,y) position of the guard after moving
    """
    match guard_direction:
        case "^":
            return current_position[0], current_position[1] - 1
        case ">":
            return current_position[0] + 1, current_position[1]
        case "v":
            return current_position[0], current_position[1] + 1
        case "<":
            return current_position[0] - 1, current_position[1]

# Part 1
# Locate guard starting position and direction
guard_position = get_guard_position(grid)
guard_direction = grid[guard_position[1]][guard_position[0]]

visited_positions = []


# Move the guard until it moves off the grid
while 0 <= guard_position[0] < grid_width and 0 <= guard_position[1] < grid_height:
    if guard_position not in visited_positions:
        visited_positions.append(guard_position)
    new_guard_direction = get_new_guard_direction_if_needed(grid, guard_direction, guard_position)
    if new_guard_direction == guard_direction:
        guard_position = get_next_guard_coord(guard_direction, guard_position)
    guard_direction = new_guard_direction

print(len(visited_positions))

# Part 2 (unbelievably inefficient but was fast to write and I don't have the time to put more effort into this)
import copy

num_infinite_paths = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == ".":
            grid_with_obstruction = copy.deepcopy(grid)
            grid_with_obstruction[y][x] = "#"

            visited_positions = []  # Format is [[(x,y),"^"|">"|"v"|"<"]]

            guard_position = get_guard_position(grid_with_obstruction)
            guard_direction = grid_with_obstruction[guard_position[1]][guard_position[0]]

            while 0 <= guard_position[0] < grid_width and 0 <= guard_position[1] < grid_height:
                if [guard_position, guard_direction] not in visited_positions:
                    visited_positions.append([guard_position, guard_direction])
                else:
                    num_infinite_paths += 1
                    break
                new_guard_direction = get_new_guard_direction_if_needed(grid_with_obstruction, guard_direction, guard_position)
                if new_guard_direction == guard_direction:
                    guard_position = get_next_guard_coord(guard_direction, guard_position)
                guard_direction = new_guard_direction

print(num_infinite_paths)