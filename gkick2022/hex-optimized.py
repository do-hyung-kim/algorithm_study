def step(padded_board, colour, left, right):
    next_hex = get_next_hex(left, right)
    if padded_board[next_hex[0]][next_hex[1]] == colour:
        return next_hex, right
    else:
        return left, next_hex

def blue_path_south(padded_board, m):
    left, right = (m - 1, 0), (m - 1, 1)
    path = set()

    while left[1] < m - 1:
        path.add(left)
        left, right = step(padded_board, 'B', left, right)
        if right[0] == 0:
            return None
    return path

def get_next_hex(left, right):
    right_dir = (right[0] - left[0], right[1] - left[1])
    for index, direction in enumerate(DIRECTION):
        if right_dir == direction:
            next_dir = DIRECTION[(index + 1) % 6]
            return (left[0] + next_dir[0], left[1] + next_dir[1])
    raise Exception

def pad_board(board, n):
    return []

def solve2(board, n):
    num_red, num_blu = count_stones(board)
    if abs(num_red - num_blu) > 1:
        return 'Impossible'

    padded_board = pad_board(board, n)
    m = n + 2

    south_path = blue_path_south(padded_board, m)
    if south_path:
        north_path = blue_path_north(padded_board, m)
        common_blue_stones = south_path.intersection(north_path)
        if common_blue_stones and num_blu >= num_red:
            return 'Blue wins'
        else:
            return 'Impossible'

    west_path = red_path_west(padded_board, m)
    if west_path:
        east_path = red_path_east(padded_board, m)
        common_red_stones = west_path.intersection(east_path)
        if common_red_stones and num_red >= num_blu:
            return 'Red wins'
        else:
            return 'Impossible'
    return 'Nobody wins'
