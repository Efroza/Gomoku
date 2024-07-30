import random

board = []
empty = " "
player = "O"
opponent = "X"


def first_play():
    opponent_pos = None

    for x in range(0, len(board)):
        for y in range(0, len(board)):
            if board[x][y] == opponent:
                opponent_pos = (x, y)
                break
    if opponent_pos[0] > len(board) // 2:
        if opponent_pos[1] > len(board) // 2:
            return (opponent_pos[0] - 1, opponent_pos[1] - 1)
        elif opponent_pos[1] < len(board) // 2:
            return (opponent_pos[0] - 1, opponent_pos[1] + 1)
        return (opponent_pos[0] - 1, opponent_pos[1])
    elif opponent_pos[0] < len(board) // 2:
        if opponent_pos[1] > len(board) // 2:
            return (opponent_pos[0] + 1, opponent_pos[1] - 1)
        elif opponent_pos[1] < len(board) // 2:
            return (opponent_pos[0] + 1, opponent_pos[1] + 1)
        return (opponent_pos[0] + 1, opponent_pos[1])
    elif opponent_pos[1] > len(board) // 2:
        if opponent_pos[0] > len(board) // 2:
            return (opponent_pos[0] - 1, opponent_pos[1] - 1)
        elif opponent_pos[0] < len(board) // 2:
            return (opponent_pos[0] + 1, opponent_pos[1] - 1)
        return (opponent_pos[0], opponent_pos[1] - 1)
    elif opponent_pos[1] < len(board) // 2:
        if opponent_pos[0] > len(board) // 2:
            return (opponent_pos[0] - 1, opponent_pos[1] + 1)
        elif opponent_pos[0] < len(board) // 2:
            return (opponent_pos[0] + 1, opponent_pos[1] + 1)
        return (opponent_pos[0], opponent_pos[1] + 1)
    elif opponent_pos[1] == len(board) // 2 and opponent_pos[0] == len(board) // 2:
        return (opponent_pos[0], opponent_pos[1] + 1)
    return None


def other_random_number():
    x = random.randint(0, len(board) - 1)
    y = random.randint(0, len(board) - 1)
    while board[x][y] != empty:
        x = random.randint(0, len(board) - 1)
        y = random.randint(0, len(board) - 1)
    return (x, y)


def defense_turn():
    for x in range(0, len(board)):
        for y in range(0, len(board)):
            if board[x][y] == opponent:
                if y + 3 < len(board) and board[x][y + 1] == opponent and board[x][y + 2] == opponent:
                    if board[x][y + 3] == empty or board[x][y - 1] == empty:
                        return [(x, y + 3), (x, y - 1)]
                if x + 3 < len(board) and board[x + 1][y] == opponent and board[x + 2][y] == opponent:
                    if board[x + 3][y] == empty or board[x - 1][y] == empty:
                        return [(x + 3, y), (x - 1, y)]
                if x + 3 < len(board) and y + 3 < len(board) and board[x + 1][y + 1] == opponent and board[x + 2][y + 2] == opponent:
                    if board[x + 3][y + 3] == empty or board[x - 1][y - 1] == empty:
                        return [(x + 3, y + 3), (x - 1, y - 1)]
                if x + 3 < len(board) and y - 3 >= 0 and board[x + 1][y - 1] == opponent and board[x + 2][y - 2] == opponent:
                    if board[x + 3][y - 3] == empty or board[x - 1][y + 1] == empty:
                        return [(x + 3, y - 3), (x - 1, y + 1)]
    return [(-1, -1), (-1, -1)]
