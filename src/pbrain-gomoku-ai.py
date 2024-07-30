#!/usr/bin/env python3

from protocol import start_cmd, turn_cmd, begin_cmd, board_cmd, info_cmd, about_cmd, end_cmd, each_opponent_pos, each_player_pos
from play_game import player, board, opponent, empty
import sys


def check_tie():
    for x in range(0, len(board)):
        for y in range(0, len(board)):
            if board[x][y] == empty:
                return False
    return True


def check_win_opponent():
    for x in range(0, len(board)):
        for y in range(0, len(board)):
            if board[x][y] == opponent:
                if y + 2 < len(board) and board[x][y + 1] == opponent and board[x][y + 2] == opponent:
                    return True
                if x + 2 < len(board) and board[x + 1][y] == opponent and board[x + 2][y] == opponent:
                    return True
                if x + 2 < len(board) and y + 2 < len(board) and board[x + 1][y + 1] == opponent and board[x + 2][y + 2] == opponent:
                    return True
                if x + 2 < len(board) and y - 2 >= 0 and board[x + 1][y - 1] == opponent and board[x + 2][y - 2] == opponent:
                    return True
    return False


def check_win_player():
    for x in range(0, len(board)):
        for y in range(0, len(board)):
            if board[x][y] == player:
                if y + 2 < len(board) and board[x][y + 1] == player and board[x][y + 2] == player:
                    return True
                if x + 2 < len(board) and board[x + 1][y] == player and board[x + 2][y] == player:
                    return True
                if x + 2 < len(board) and y + 2 < len(board) and board[x + 1][y + 1] == player and board[x + 2][y + 2] == player:
                    return True
                if x + 2 < len(board) and y - 2 >= 0 and board[x + 1][y - 1] == player and board[x + 2][y - 2] == player:
                    return True
    return False


def min_func():
    _min = 2
    qx = None
    qy = None

    if check_win_player():
        return (1, None, None)
    elif check_win_opponent():
        return (-1, None, None)
    elif check_tie():
        return (0, None, None)
    for x in range(0, len(board)):
        for y in range(0, len(board)):
            if board[x][y] == empty:
                board[x][y] = opponent
                (m, maxx, maxy) = max_func()
                if m < _min:
                    _min = m
                    qx = x
                    qy = y
                board[x][y] = empty
    return (_min, qx, qy)


def max_func():
    _max = -2
    px = None
    py = None

    if check_win_player():
        return (1, None, None)
    elif check_win_opponent():
        return (-1, None, None)
    elif check_tie():
        return (0, None, None)
    for x in range(0, len(board)):
        for y in range(0, len(board)):
            if board[x][y] == empty:
                board[x][y] = player
                (m, minx, miny) = min_func()
                if m > _max:
                    _max = m
                    px = x
                    py = y
                board[x][y] = empty
    return (_max, px, py)


def game_is_winnable():
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == player:
                if i + 3 < len(board) and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][j] == empty:
                    return (i + 3, j)
                if i + 2 < len(board) and i - 1 >= 0 and board[i + 1][j] == player and board[i + 2][j] == empty and board[i - 1][j] == empty:
                    return (i + 2, j)
                if i + 1 < len(board) and i - 2 >= 0 and board[i + 1][j] == empty and board[i - 1][j] == player and board[i - 2][j] == empty:
                    return (i - 1, j)
                if i - 3 >= 0 and board[i - 1][j] == player and board[i - 2][j] == player and board[i - 3][j] == empty:
                    return (i - 3, j)
                if j + 3 < len(board) and board[i][j + 1] == player and board[i][j + 2] == player and board[i][j + 3] == empty:
                    return (i, j + 3)
                if j + 2 < len(board) and j - 1 >= 0 and board[i][j + 1] == player and board[i][j + 2] == empty and board[i][j - 1] == empty:
                    return (i, j + 2)
                if j + 1 < len(board) and j - 2 >= 0 and board[i][j + 1] == empty and board[i][j - 1] == player and board[i][j - 2] == empty:
                    return (i, j - 1)
                if j - 3 >= 0 and board[i][j - 1] == player and board[i][j - 2] == player and board[i][j - 3] == empty:
                    return (i, j - 3)
                if i + 3 < len(board) and j + 3 < len(board) and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and board[i + 3][j + 3] == empty:
                    return (i + 3, j + 3)
                if i + 2 < len(board) and i - 1 >= 0 and j + 2 < len(board) and j - 1 >= 0 and board[i + 1][j + 1] == player and board[i + 2][j + 2] == empty and board[i - 1][j - 1] == empty:
                    return (i + 2, j + 2)
                if i + 1 < len(board) and i - 2 >= 0 and j + 1 < len(board) and j - 2 >= 0 and board[i + 1][j + 1] == empty and board[i - 1][j - 1] == player and board[i - 2][j - 2] == empty:
                    return (i - 1, j - 1)
                if i - 3 >= 0 and j - 3 >= 0 and board[i - 1][j - 1] == player and board[i - 2][j - 2] == player and board[i - 3][j - 3] == empty:
                    return (i - 3, j - 3)
                if i + 3 < len(board) and j - 3 >= 0 and board[i + 1][j - 1] == player and board[i + 2][j - 2] == player and board[i + 3][j - 3] == empty:
                    return (i + 3, j - 3)
                if i + 2 < len(board) and i - 1 >= 0 and j - 2 >= 0 and j + 1 < len(board) and board[i + 1][j - 1] == player and board[i + 2][j - 2] == empty and board[i - 1][j + 1] == empty:
                    return (i + 2, j - 2)
                if i + 1 < len(board) and i - 2 >= 0 and j - 1 >= 0 and j + 2 < len(board) and board[i + 1][j - 1] == empty and board[i - 1][j + 1] == player and board[i - 2][j + 2] == empty:
                    return (i - 1, j + 1)
                if i - 3 >= 0 and j + 3 < len(board) and board[i - 1][j + 1] == player and board[i - 2][j + 2] == player and board[i - 3][j + 3] == empty:
                    return (i - 3, j + 3)
    return None


def check_aligned():
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == player:
                if i + 1 < len(board) and board[i + 1][j] == player:
                    if i + 2 < len(board) and board[i + 2][j] == player:
                        if i + 3 < len(board) and board[i + 3][j] == player:
                            if i + 4 < len(board) and board[i + 4][j] == player:
                                return True
                if j + 1 < len(board) and board[i][j + 1] == player:
                    if j + 2 < len(board) and board[i][j + 2] == player:
                        if j + 3 < len(board) and board[i][j + 3] == player:
                            if j + 4 < len(board) and board[i][j + 4] == player:
                                return True
                if i + 1 < len(board) and j + 1 < len(board) and board[i + 1][j + 1] == player:
                    if i + 2 < len(board) and j + 2 < len(board) and board[i + 2][j + 2] == player:
                        if i + 3 < len(board) and j + 3 < len(board) and board[i + 3][j + 3] == player:
                            if i + 4 < len(board) and j + 4 < len(board) and board[i + 4][j + 4] == player:
                                return True
                if i + 1 < len(board) and j - 1 >= 0 and board[i + 1][j - 1] == player:
                    if i + 2 < len(board) and j - 2 >= 0 and board[i + 2][j - 2] == player:
                        if i + 3 < len(board) and j - 3 >= 0 and board[i + 3][j - 3] == player:
                            if i + 4 < len(board) and j - 4 >= 0 and board[i + 4][j - 4] == player:
                                return True
    return False


def check_game_is_over():
    check_empty = False
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == empty:
                check_empty = True
                break
    if not check_empty:
        return True
    return check_aligned()


def main():
    actions = {"START": start_cmd, "TURN": turn_cmd, "BEGIN": begin_cmd,
               "BOARD": board_cmd, "INFO": info_cmd, "ABOUT": about_cmd, "END": end_cmd}
    while True:
        line = input()
        if not line:
            break
        line = line.split()
        if line[0] in actions:
            if len(board) == 0 and line[0] != "START" and line[0] != "END":
                print("ERROR no board")
                continue
            actions[line[0]](line)
            if check_game_is_over():
                sys.exit(0)
            # for i in board:
            #     print(i)
            # print(each_player_pos)
            # print(each_opponent_pos)
            continue
        print(f"UNKNOWN command {line[0]}")


if __name__ == '__main__':
    main()