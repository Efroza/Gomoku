from play_game import board, player, opponent, empty, defense_turn
from algo import algorithm
import random

each_player_pos = []
each_opponent_pos = []


def random_number():
    random_number_x = random.randint(0, len(board) - 1)
    random_number_y = random.randint(0, len(board) - 1)
    if board[random_number_x][random_number_y] == empty:
        board[random_number_x][random_number_y] = player
        print(f"{random_number_x},{random_number_y}")
    else:
        random_number()


def start_cmd(line):
    if len(line) != 2 or int(line[1]) < 5:
        print("ERROR invalid START command")
        return
    for i in range(0, int(line[1])):
        new_line = []
        for j in range(0, int(line[1])):
            new_line.append(empty)
        board.append(new_line)
    print("OK")


def board_cmd(line):
    new_line = ""
    while True:
        new_line = input()
        if new_line.find("DONE") != -1:
            break
        new_line = new_line.split(',')
        if new_line[2] == '1':
            board[int(new_line[0])][int(new_line[1])] = player
        elif new_line[2] == '2':
            board[int(new_line[0])][int(new_line[1])] = opponent
    random_number()


def begin_cmd(line):
    x = len(board) // 2
    y = len(board) // 2
    board[x][y] = player
    print(f"{x},{y}")


def turn_cmd(line):
    turn = line[1].split(',')
    board[int(turn[0])][int(turn[1])] = opponent
    each_opponent_pos.append((int(turn[0]), int(turn[1])))
    check_algorithm = algorithm()
    if check_algorithm != None:
        if isinstance(check_algorithm, list):
            tmp = check_algorithm[0]
            check_algorithm = tmp
        board[check_algorithm[0]][check_algorithm[1]] = player
        each_player_pos.append((check_algorithm[0], check_algorithm[1]))
        print(f"{check_algorithm[0]},{check_algorithm[1]}")
        return


def info_cmd(line):
    pass


def about_cmd(line):
    print("name=\"Gomoku IA\", version=\"0.0.1\", author=\"Flemme\", country=\"France\"")


def end_cmd(line):
    exit(0)
