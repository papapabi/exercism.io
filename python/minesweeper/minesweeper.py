import re

def board(board_array):
    if not valid_board(board_array):
        raise ValueError("not a valid board")
    return __replace_with_mine_markers(board_array)

def __search_space(row, clm, board_array):
    """Returns the search space of a given tile in the board as a list.

    The search space of a tile are the tiles directly adjacent to it
    (horizontally, vertically, and diagonally).
    """
    row_visible = board_array[row-1:row] + board_array[row:row+2]
    clm_visible = (row[clm-1:clm] + row[clm:clm+2] for row in row_visible)
    return ''.join(clm_visible)

def __replace_with_mine_markers(board_array):
    out = []
    for i, row in enumerate(board_array):
        s = ""
        for j, col in enumerate(row):
            if board_array[i][j] == "*":
                s += "*"
            else:
                # Count the number of * in a tile's search space.
                num = __search_space(i, j, board_array).count("*")
                if num == 0:
                    num = ' '
                s += str(num)
        out.append(s)
    return out

def __valid_chars(board_array):
    """Returns true if a board only contains spaces and asterisks."""
    board_chars_regex = re.compile(r'[^* ]')
    return not board_chars_regex.search(''.join(board_array))

def __valid_length(board_array):
    """Returns true if every row in the board is of the same length."""
    return len({len(row) for row in board_array}) <= 1 # Empty boards are OK.

def valid_board(board_array):
    return __valid_chars(board_array) and __valid_length(board_array)
