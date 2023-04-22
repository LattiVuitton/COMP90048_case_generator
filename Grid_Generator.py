import random
CARDS = ['Black', 'Red', 'Empty']

################################

WIDTH = 5
HEIGHT = 4

enforce_safe = True

################################

grid = []

for i in range(HEIGHT):
    line = []
    for j in range(WIDTH):
        new_cell = random.choice(CARDS)
        line.append(new_cell)
    grid.append(line)

def cell_is_Red(i, j):
    if j < 0 or j >= len(grid[0]): return False
    if grid[i][j] == 'Red':
        return True
    return False

if enforce_safe:
    for i, row in enumerate(grid):
        if i != 0:
            for j, cell in enumerate(row):
                if cell == 'Black':
                    if cell_is_Red(i-1, j-1) or cell_is_Red(i-1, j+1):
                        grid[i][j] = 'Empty'

print_string = "safe ["
for row in grid:
    print_string += "["
    for cell in row:
        print_string += (cell + ",")
    print_string = print_string[:-1]
    print_string += "],"
print_string = print_string[:-1]
print_string += "]"

print("Copy the following:")
print(print_string)
