#
# CS1010X --- Programming Methodology
#
# Contest 10.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from random import *
from puzzle_AI import *
from copy import deepcopy

def AI(mat):
    def random_move(n, mat):
        grid = {    "w": [],
                    "a": [],
                    "s": [],
                    "d": []
        }
        for i in range(n):
            score = 0
            valid = False
            first_moves = ['w', 'a', 's', 'd']
            matcopy = deepcopy(mat)
            moves = 1
            while 1:
                firstmove = choice(first_moves)
                if firstmove == 'w':
                    matcopy, valid, inscore = merge_up(matcopy)
                elif firstmove == 'a':
                    matcopy, valid, inscore = merge_left(matcopy)
                elif firstmove == 's':
                    matcopy, valid, inscore = merge_down(matcopy)
                else:
                    matcopy, valid, inscore = merge_right(matcopy)
                if valid == True:
                    matcopy = add_two(matcopy)
                    score += inscore
                    break
                else: 
                    first_moves.remove(firstmove)
            while 1:
                status = game_status(matcopy)
                if status == 'win' or status == 'lose' or moves > 12:
                    break
                step = choice(['w', 'a', 's', 'd'])
                if step == 'w':
                    matcopy, valid, inscore = merge_up(matcopy)
                elif step == 'a':
                    matcopy, valid, inscore = merge_left(matcopy)
                elif step == 's':
                    matcopy, valid, inscore = merge_down(matcopy)
                else:
                    matcopy, valid, inscore = merge_right(matcopy)
                if valid:
                    score += inscore
                    matcopy = add_two(matcopy)
                moves += 1
            grid[firstmove].append(score)
        return grid
    number_of_tries = 350 # increase the number_of_tries to increase accuracy
    grid = random_move(number_of_tries, mat)
    for i in grid.keys():
        try:
            temp = sum(grid[i]) / len(grid[i])
            if temp == 0:
                grid[i] = 1
            else:
                grid[i] = temp
        except:
            grid[i] = 0
    grid = sorted(grid.items(), key = lambda x: x[1], reverse = True)
    return grid[0][0]


# UNCOMMENT THE FOLLOWING LINES AND RUN TO WATCH YOUR SOLVER AT WORK
#game_logic['AI'] = AI
#gamegrid = GameGrid(game_logic)

# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
# Note: Your solver is expected to produce only valid moves.
get_average_AI_score(AI, True)
