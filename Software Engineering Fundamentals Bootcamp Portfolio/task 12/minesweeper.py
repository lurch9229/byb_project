"""
Create a complete minesweeper board from a template grid
using a 2d list
"""
# Create a 5x5 board
template_grid = [["-", "-", "-", "#", "#"],
                 ["-", "#", "-", "-", "-"],
                 ["-", "-", "#", "-", "-"],
                 ["-", "#", "#", "-", "-"],
                 ["-", "-", "-", "-", "-"]]


# Prints the template grid in a similar format to above
def show_template():
    row_idx = 0
    for row in template_grid:
        row_idx += 1
        for col in row:
            print(col, end="")
        print()


print("Grid to be numbered:")
show_template()


def number_grid(template):
    grid = []
    for row in range(len(template)):
        grid.append(template[row][:])
        for col in range(len(template[row])):
            if template[row][col] == "#":
                continue
                # Continue will skip the # in template row and col indexes if it = #
            nearby = 0
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1),
                              (1, -1), (-1, 1)]:
                # These determine which cardinal directions(NESW/NeNwSeSw from the current index we are looking at
                dx, dy = row + direction[0], col + direction[1]
                # Row index + direction tuples first index, column index + direction tuples second index
                try:
                    if dx >= 0 and dy >= 0 and template[dx][dy] == "#":
                        # Use of >= 0 to account for going off the board
                        # if x and y >= 0 and if template indexes x and y = #
                        nearby += 1
                except IndexError:
                    pass
            grid[row][col] = nearby
            # Update the new grid with numbers positional to bombs/#
    return grid


def show_number():
    row_index = 0
    for row in number_grid(template_grid):
        row_index += 1
        for col in row:
            print(col, end="")
        print()


print("Grid numbered:")
show_number()
