def get_winning_move(elf_move):
    if elf_move == "A":
        return "Y"
    if elf_move == "B":
        return "Z"
    return "X"

def get_losing_move(elf_move):
    if elf_move == "A":
        return "Z"
    if elf_move == "B":
        return "X"
    return "Y"

def get_drawing_move(elf_move):
    if elf_move == "A":
        return "X"
    if elf_move == "B":
        return "Y"
    return "Z"

def get_best_move(elf_move, result_round):
    if (result_round == "X"):
        return get_losing_move(elf_move) 
    if (result_round == "Y"):
        return get_drawing_move(elf_move)
    return get_winning_move(elf_move)

def get_points_for_move(my_move):
    if my_move == 'X':
        return 1
    if my_move == 'Y':
        return 2
    else:
        return 3

def is_a_draw_for_me(elf_move, my_move):
    if (elf_move == "A" and my_move == "X") or (elf_move == "B" and my_move == "Y") or (elf_move == "C" and my_move == "Z"):
        return True
    return False

def is_a_win_for_me(elf_move, my_move):
    if (elf_move == "A" and my_move == "Y") or (elf_move == "B" and my_move == "Z") or (elf_move == "C" and my_move == "X"):
        return True
    return False

def calculate_score(elf_move, my_move):
    score = 0
    if is_a_win_for_me(elf_move, my_move):
        score += 6
    if is_a_draw_for_me(elf_move, my_move):
        score += 3
    score += get_points_for_move(my_move)
    return score

strategy_file = open("../inputs/rock_paper_scissor_strategy.txt", 'r')
strategy = strategy_file.readlines()
total_score = 0
list_moves = []

for moves in strategy:
    moves = moves.rstrip("\n")
    elf_move, my_move = moves.split(" ")
    list_moves.append((elf_move, my_move))
    total_score += calculate_score(elf_move, my_move)

print(f"The score of this games following the strategy will be {total_score}")
print("Oh shit, the elf has scammed me. Anyway, let's recalculate the score")

total_score = 0
for elf_move, result_round in list_moves:
    my_move = get_best_move(elf_move, result_round)
    total_score += calculate_score(elf_move, my_move)

print(f"The real score of this games will be {total_score}")