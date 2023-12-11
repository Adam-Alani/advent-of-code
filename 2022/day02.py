from aocd import data
data = data.split('\n')

opp = {
    "A": 1,
    "B": 2,
    "C": 3
}

me = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

outcome = {
    "X": 1, # lose
    "Y": 2, # draw
    "Z": 3  # win
}

sum = 0
score = 0
for i in range(len(data)):
    game = data[i].split(' ')
    opp_move = opp[game[0]]
    my_move = me[game[1]]
    if opp_move == my_move:
        sum += my_move + 3
    winner = (my_move - opp_move) % 3
    if winner == 1:
        sum += my_move + 6
    elif winner == 2:
        sum += my_move

    should_be = outcome[game[1]]
    if should_be == 2:
        score += opp_move + 3
    if should_be == 1: # lose
        if opp_move == 1: # rock
            score += 3
        elif opp_move == 2: # paper
            score += 1
        elif opp_move == 3: # scissors
            score += 2
    elif should_be == 3: # draw
        if opp_move == 1: # rock
            score += 2 + 6
        elif opp_move == 2: # paper
            score += 3 + 6
        elif opp_move == 3: # scissors
            score += 1 + 6


print(sum)
print(score)





