def minesweeper(grid):
    """Return a completed minesweeper grid.

    For a given grid, a square array with string entries:\n
        "-": to denote a mine-free spot,
        "#": to denote a mine,\n
    returns a completed grid where each "-" is replaced with a value to denote
    the number of adjacent mines.
    """
    # Define max bounds of grid
    max_rows = len(grid)
    max_cols = len(grid[0])

    # Begin iterating through cell given by row,col of the grid
    for row in range(max_rows):
        for col in range(max_cols):

            # Check if mine is present, if so, skip
            if grid[row][col] == "#":
                continue

            # Empty space found
            else:
                # Initialise number of mines
                grid[row][col] = 0

                # Iterate through adjacent cells
                for adj_col in range(-1, 2, 1):
                    for adj_row in range(-1, 2, 1):

                        # Declare variables to check adjacent cells. Due to
                        # how the range object is constructed, these variables
                        # take values row - 1, row + 0, row + 1 and similar for
                        # col. Hence all adjacent spaces are checked
                        check_row = row + adj_row
                        check_col = col + adj_col

                        # Check if the considered adjacent row actually exists
                        # and is not out of bounds
                        if (check_row < 0) or (check_row == max_rows):
                            continue

                        # Similar for the adjacent columns
                        elif (check_col < 0) or (check_col == max_cols):
                            continue

                        # The case where the adjacent space is in bounds
                        else:
                            # If a mine is present in adjacent space, increment
                            # the value of the current row,col
                            if grid[check_row][check_col] == "#":
                                grid[row][col] += 1

    return grid
