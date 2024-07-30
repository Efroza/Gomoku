from play_game import defense_turn, first_play, other_random_number, player, board, empty, opponent
from check import score_attack, attack_turn


def algorithm():
    global score_attack
    first_turn = False
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == player:
                first_turn = True
                break
    if not first_turn:
        return first_play()
    else:
        check_defense = defense_turn()
        if check_defense[0] != (-1, -1):
            if isinstance(check_defense, list):
                if board[check_defense[0][0]][check_defense[0][1]] == empty:
                    return check_defense[0]
                else:
                    return check_defense[1]
            return check_defense
        check_attack = attack_turn()
        if check_attack != (-1, -1):
            score_attack = [(-1, -1), -1]
            return check_attack
    return other_random_number()