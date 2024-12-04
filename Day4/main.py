def is_valid(x, y, rows, cols):

    return 0 <= x < rows and 0 <= y < cols

def count_word_from_position(word_grid, word, x, y, dx, dy):

    rows, cols = len(word_grid), len(word_grid[0])
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if not is_valid(nx, ny, rows, cols) or word_grid[nx][ny] != word[i]:
            return 0
    return 1

def count_word_in_grid(word_grid, word):

    rows, cols = len(word_grid), len(word_grid[0])
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1), # diagonal up-left
        (-1, 1)   # diagonal up-right
    ]
    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                count += count_word_from_position(word_grid, word, x, y, dx, dy)
    return count

# Read grid from input file
def create_grid_from_file(input_file):
    with open(input_file, 'r') as file:
        word_search_grid = [line.strip() for line in file.readlines()]
    return word_search_grid



grid = create_grid_from_file("input.txt")
total_count = count_word_in_grid(grid, "XMAS")

print(total_count)
