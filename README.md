# 2048solver
This are the codes i submitted to win the 2048 contest for CS1010X Porgramming Methodology. It achieved an average
score of 20292.58 with 0 initial moves for 200 rounds and a win rate of 92.50%. With a random 200 initial
move, it achieved an average of 20123.76 and win rate of 93%.

### My task
Write a function AI(mat) that takes in a game matrix mat and return one of the following strings: ‘w’, ‘a’, ‘s’ or ‘d’ which represent moves in the upward, leftward, downward and rightward directions respectively. Your final submission should produce only valid moves.
Your solver should be able to continue any arbitrary game, including the one played halfway. No undos are allowed. You are also not allowed to store information using global variables (or by any other means) from call to call. Moreover, you are not allowed to affect the randomness of the creation of tiles. There will be a time limit of 2 minutes per game. Anything done after the time limit may not be counted.

### How it works
The AI plays the game based on Monte-Carlo (MC) algorithm. Since each step in 2048 will generate a new tile in random position, I chosed to use MC. There will be a total of 350 random moves at the current state and decide on which move is the best based on the highest average score for each move.

### Running the Solver
Uncomment the below lines to watch the solver’s move-by-move execution:
```
game_logic ['AI '] = AI
gamegrid = GameGrid ( game_logic )
```
Press any key to see the next move each time. Uncomment
```
get_average_AI_score ( AI , True )
```
instead to run the solver multiple times and get the average.
