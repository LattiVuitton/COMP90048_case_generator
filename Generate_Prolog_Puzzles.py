import random
import string

# Copy output from terminal into Prolog after your solver predicates, and type 'testx.'  to test on these.

# Dimensions of puzzle
puzzle_width = 32
puzzle_height = 20

# Describes fraction of black squares in the grid
black_square_threshold = 0.25

################# Main
max_attempts = 100
attempt_count = 0
while attempt_count < max_attempts:
    attempt_count += 1
    grid = []
    for i in range(puzzle_height):
        row = []
        row_string = '          ['
        if i == 0:
            row_string = '\n\n\nCopy the following:\n\nwrite_puzzle([]).\nwrite_puzzle([Line|Rest]) :-\n    write(Line),\n    nl,\n    write_puzzle(Rest).\n\ntestx :-\nPuzzle = [['
            

        for j in range(puzzle_width):
            if random.random() < black_square_threshold:
                random_letter = '#'
                row_string += '#'
            else:
                random_letter = random.choice(string.ascii_lowercase)
                row_string += '_'
            row.append(random_letter)
            if j < puzzle_width - 1:
                row_string += ', '
        if i == puzzle_height - 1:
            row_string += ']'
        row_string += '],'
        grid.append(row)
        print(row_string)
    def is_isolated(grid, i, j):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
            return True
        if grid[i][j] == '#':
            return True
        return False
    can_break = True
    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            if letter != '#':
                if (is_isolated(grid, i + 1, j) and is_isolated(grid, i, j + 1) and is_isolated(grid, i - 1, j) and is_isolated(grid, i, j - 1)):
                    grid[i][j] = '.'
                    can_break = False
    print("\nWordList = [")
    for l, row in enumerate(grid):
        i = len(grid)-1-l
        row_string = ""
        for value in row:
            row_string += value
        split_row = row_string.split("#")
        words = []
        for segment in split_row:
            if len(segment) > 1:
                words.append(segment)
        for j, word in enumerate(words):
            if len(word) > 1:
                word_string = ""
                for letter in word:
                    word_string += ("'" + letter + "', ")
                word_string = word_string[:-2]
                print('           [' + word_string + '],')
    word_list = []
    printing = ""
    for word in words:
        word_list.append(word)
    for i in range(len(grid[0])):
        column_string = ""
        for j in range(len(grid)):
            column_string += grid[j][i]
        split_column = column_string.split("#")
        words = []
        for segment in split_column:
            if len(segment) > 1:
                words.append(segment)
        for j, word in enumerate(words):
            if len(word) > 1:
                word_string = ""
                for letter in word:
                    word_string += ("'" + letter + "', ")
                word_string = word_string[:-2]
                printing += ('           [' + word_string + '],\n')
        for word in words:
            word_list.append(word)
    printing = printing[:-2] + "],\n"
    print(printing + "time(puzzle_solution(Puzzle, WordList)),\nwrite_puzzle(Puzzle).")
    print("\nSolution:")
    for row in grid:
        stringy = ""
        for z in row:
            if z == '#':
                stringy += " "
            else:
                stringy += z
            stringy += " "
        print(stringy)
    myDict = {}
    dupls = []
    for word in word_list:
        if word in myDict:
            print(word)
            dupls.append(word)
        else:
            myDict[word] = 1
    if can_break and len(dupls) == 0:
        break
