from play_game import board, player, opponent, empty
score_attack = [(-1, -1), -1]


def change_score(piece, score):
    if score > score_attack[1]:
        score_attack[0] = piece
        score_attack[1] = score


def check_around(current, direction):
    score = 2
    piece = (current[0], current[1])
    if direction == "up":
        for i in range(1, 4):
            if current[0] - i >= 0 and board[current[0] - i][current[1]] == player:
                score += 1
            if current[0] - i >= 0 and board[current[0] - i][current[1]] == opponent:
                score = -1
                break
            if current[0] - i >= 0 and board[current[0] - i][current[1]] == empty:
                piece = (current[0] - i, current[1])
                change_score(piece, score)
                break
    elif direction == "down":
        for i in range(1, 4):
            if current[0] + i < len(board) and board[current[0] + i][current[1]] == player:
                score += 1
            if current[0] + i < len(board) and board[current[0] + i][current[1]] == opponent:
                score = -1
                break
            if current[0] + i < len(board) and board[current[0] + i][current[1]] == empty:
                piece = (current[0] + i, current[1])
                change_score(piece, score)
                break
    elif direction == "left":
        for i in range(1, 4):
            if current[1] - i >= 0 and board[current[0]][current[1] - i] == player:
                score += 1
            if current[1] - i >= 0 and board[current[0]][current[1] - i] == opponent:
                score = -1
                break
            if current[1] - i >= 0 and board[current[0]][current[1] - i] == empty:
                piece = (current[0], current[1] - i)
                change_score(piece, score)
                break
    elif direction == "right":
        for i in range(1, 4):
            if current[1] + i < len(board) and board[current[0]][current[1] + i] == player:
                score += 1
            if current[1] + i < len(board) and board[current[0]][current[1] + i] == opponent:
                score = -1
                break
            if current[1] + i < len(board) and board[current[0]][current[1] + i] == empty:
                piece = (current[0], current[1] + i)
                change_score(piece, score)
                break
    elif direction == "up_left":
        for i in range(1, 4):
            if current[0] - i >= 0 and current[1] - i >= 0 and board[current[0] - i][current[1] - i] == player:
                score += 1
            if current[0] - i >= 0 and current[1] - i >= 0 and board[current[0] - i][current[1] - i] == opponent:
                score = -1
                break
            if current[0] - i >= 0 and current[1] - i >= 0 and board[current[0] - i][current[1] - i] == empty:
                piece = (current[0] - i, current[1] - i)
                change_score(piece, score)
                break
    elif direction == "up_right":
        for i in range(1, 4):
            if current[0] - i >= 0 and current[1] + i < len(board) and board[current[0] - i][current[1] + i] == player:
                score += 1
            if current[0] - i >= 0 and current[1] + i < len(board) and board[current[0] - i][current[1] + i] == opponent:
                score = -1
                break
            if current[0] - i >= 0 and current[1] + i < len(board) and board[current[0] - i][current[1] + i] == empty:
                piece = (current[0] - i, current[1] + i)
                change_score(piece, score)
                break
    elif direction == "down_left":
        for i in range(1, 4):
            if current[0] + i < len(board) and current[1] - i >= 0 and board[current[0] + i][current[1] - i] == player:
                score += 1
            if current[0] + i < len(board) and current[1] - i >= 0 and board[current[0] + i][current[1] - i] == opponent:
                score = -1
                break
            if current[0] + i < len(board) and current[1] - i >= 0 and board[current[0] + i][current[1] - i] == empty:
                piece = (current[0] + i, current[1] - i)
                change_score(piece, score)
                break
    elif direction == "down_right":
        for i in range(1, 4):
            if current[0] + i < len(board) and current[1] + i < len(board) and board[current[0] + i][current[1] + i] == player:
                score += 1
            if current[0] + i < len(board) and current[1] + i < len(board) and board[current[0] + i][current[1] + i] == opponent:
                score = -1
                break
            if current[0] + i < len(board) and current[1] + i < len(board) and board[current[0] + i][current[1] + i] == empty:
                piece = (current[0] + i, current[1] + i)
                change_score(piece, score)
                break


def attack_turn():
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == player:
                check_around((i, j), "up")
                check_around((i, j), "down")
                check_around((i, j), "left")
                check_around((i, j), "right")
                check_around((i, j), "up_left")
                check_around((i, j), "up_right")
                check_around((i, j), "down_left")
                check_around((i, j), "down_right")
    return score_attack[0]