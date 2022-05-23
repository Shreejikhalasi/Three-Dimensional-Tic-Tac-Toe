from games import *

class ThreeDimensionalTicTacToe(Game):
    def __init__(self, h=3, v=3, w=3, k=3):
        self.h = h
        self.v = v
        self.w = w
        self.k = k
        
        moves = [(x, y, z) for x in range(1, h + 1)
                 for y in range(1, v + 1)
                 for z in range(1, w + 1)]
        
        self.initial = GameState(to_move='X', utility=0, board={}, moves=moves)

    def actions(self, state):
        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return state  # Illegal move has no effect
        board = state.board.copy()
        board[move] = state.to_move
        moves = list(state.moves)
        moves.remove(move)
        return GameState(to_move=('O' if state.to_move == 'X' else 'X'),
                         utility=self.compute_utility(board, move, state.to_move),
                         board=board, moves=moves)

    def utility(self, state, player):
        return state.utility if player == 'X' else -state.utility

    def terminal_test(self, state):
        return state.utility != 0 or len(state.moves) == 0

    def display(self, state):
        board = state.board
        for z in range(1, self.w + 1):
            print("Dimension " + str(z) + ":")
            for x in range(1, self.h + 1):
                for y in range(1, self.v + 1):
                    print(board.get((x, y, z), '.'), end=' ')
                print()

    def compute_utility(self, board, move, player):
        """If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0."""
        if (self.k_in_row(board, move, player, (0, 1, 0)) or
                self.k_in_row(board, move, player, (1, 0, 0)) or
                self.k_in_row(board, move, player, (1, -1, 0)) or
                self.k_in_row(board, move, player, (1, 1, 0)) or
                self.k_in_row(board, move, player, (0, 0, 1)) or
                self.k_in_row(board, move, player, (1, 1, 1)) or
                self.k_in_row(board, move, player, (1, -1, 1)) or
                self.k_in_row(board, move, player, (1, 1, -1)) or
                self.k_in_row(board, move, player, (1, -1, -1)) or 
                self.k_in_row(board, move, player, (1, 0, 1)) or 
                self.k_in_row(board, move, player, (1, 0, -1)) or
                self.k_in_row(board, move, player, (0, 1, 1)) or 
                self.k_in_row(board, move, player, (0, 1, -1))):
            return +1 if player == 'X' else -1
        else:
            return 0

    def k_in_row(self, board, move, player, delta_x_y_z):
        """Return true if there is a line through move on board for player."""
        (delta_x, delta_y, delta_z) = delta_x_y_z
        x, y, z = move
        n = 0  # n is number of moves in row
        while board.get((x, y, z)) == player:
            n += 1
            x, y, z = x + delta_x, y + delta_y, z + delta_z
        x, y, z = move
        while board.get((x, y, z)) == player:
            n += 1
            x, y, z = x - delta_x, y - delta_y, z - delta_z
        n -= 1  # Because we counted move itself twice
        return n >= self.k
    
def k_in_row_count(board, move, player, delta_x_y_z):
    (delta_x, delta_y, delta_z) = delta_x_y_z
    x, y, z = move
    n = 0  # n is number of moves in row
    while board.get((x, y, z)) == player:
        n += 1
        x, y, z = x + delta_x, y + delta_y, z + delta_z
    x, y, z = move
    while board.get((x, y, z)) == player:
        n += 1
        x, y, z = x - delta_x, y - delta_y, z - delta_z
    n -= 1  # Because we counted move itself twice
    return n 

def count_in_a_row(board, player):
    value = 0
    count = 0
    move = (1, 1, 1)
    if (k_in_row_count(board, move, player, (0, 1, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 1, 0)) == 2 or
        k_in_row_count(board, move, player, (0, 1, 1)) == 2 or 
        k_in_row_count(board, move, player, (1, 0, 1)) == 2 or 
        k_in_row_count(board, move, player, (0, 0, 1)) == 2 or 
        k_in_row_count(board, move, player, (1, 1, 1)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1

    if (k_in_row_count(board, move, player, (0, 1, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 1, 0)) == 1 or
        k_in_row_count(board, move, player, (0, 1, 1)) == 1 or 
        k_in_row_count(board, move, player, (1, 0, 1)) == 1 or 
        k_in_row_count(board, move, player, (0, 0, 1)) == 1 or 
        k_in_row_count(board, move, player, (1, 1, 1)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (2, 2, 1)
    if (k_in_row_count(board, move, player, (0, 1, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 2 or 
        k_in_row_count(board, move, player, (0, 0, 1)) == 2 or 
        k_in_row_count(board, move, player, (1, -1, 0)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1

    if (k_in_row_count(board, move, player, (0, 1, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 1 or 
        k_in_row_count(board, move, player, (0, 0, 1)) == 1 or 
        k_in_row_count(board, move, player, (1, -1, 0)) == 1):
        #return 0.33 if player == 'X' else -0.33
        value += .33 if player == 'X' else -.33
        count += 1

    move = (3, 3, 1)
    if (k_in_row_count(board, move, player, (0, 1, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 2 or 
        k_in_row_count(board, move, player, (0, 0, 1)) == 2 or
        k_in_row_count(board, move, player, (1, 1, -1)) == 2 or
        k_in_row_count(board, move, player, (-1, 0, -1)) == 2 or
        k_in_row_count(board, move, player, (0, -1, -1)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1

    if (k_in_row_count(board, move, player, (0, 1, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 1 or 
        k_in_row_count(board, move, player, (0, 0, 1)) == 1 or
        k_in_row_count(board, move, player, (1, 1, -1)) == 1 or
        k_in_row_count(board, move, player, (-1, 0, -1)) == 1 or
        k_in_row_count(board, move, player, (0, -1, -1)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (2, 2, 2)
    if (k_in_row_count(board, move, player, (1, -1, -1)) == 2 or
        k_in_row_count(board, move, player, (-1, 1, -1)) == 2 or
        k_in_row_count(board, move, player, (0, 1, 0)) == 2 or 
        k_in_row_count(board, move, player, (1, 0, 0)) == 2 or
        k_in_row_count(board, move, player, (1, -1, 0)) == 2 or 
        k_in_row_count(board, move, player, (1, 1, 0)) == 2 or
        k_in_row_count(board, move, player, (0, 1, 1)) == 2 or
        k_in_row_count(board, move, player, (0, 1, -1)) == 2 or 
        k_in_row_count(board, move, player, (1, 0, 1)) == 2 or 
        k_in_row_count(board, move, player, (1, 0, -1)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1

    if (k_in_row_count(board, move, player, (1, -1, -1)) == 1 or
        k_in_row_count(board, move, player, (-1, 1, -1)) == 1 or
        k_in_row_count(board, move, player, (0, 1, 0)) == 1 or 
        k_in_row_count(board, move, player, (1, 0, 0)) == 1 or
        k_in_row_count(board, move, player, (1, -1, 0)) == 1 or 
        k_in_row_count(board, move, player, (1, 1, 0)) == 1 or
        k_in_row_count(board, move, player, (0, 1, 1)) == 1 or
        k_in_row_count(board, move, player, (0, 1, -1)) == 1 or 
        k_in_row_count(board, move, player, (1, 0, 1)) == 1 or 
        k_in_row_count(board, move, player, (1, 0, -1)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (1, 1, 2)
    if (k_in_row_count(board, move, player, (0, 1, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1

    if (k_in_row_count(board, move, player, (0, 1, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (3, 3, 2)
    if (k_in_row_count(board, move, player, (0, 1, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1

    if (k_in_row_count(board, move, player, (0, 1, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (1, 1, 3)
    if (k_in_row_count(board, move, player, (0, 1, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 1, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 0, -1)) == 2 or
        k_in_row_count(board, move, player, (0, 1, -1)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1
    
    if (k_in_row_count(board, move, player, (0, 1, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 1, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 0, -1)) == 1 or
        k_in_row_count(board, move, player, (0, 1, -1)) == 1):
        #return 0.33 if player == 'X' else -0.33
        value += .33 if player == 'X' else -.33
        count += 1

    move = (3, 3, 3)
    if (k_in_row_count(board, move, player, (0, 1, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 0, 1)) == 2 or
        k_in_row_count(board, move, player, (0, 1, 1)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1

    if (k_in_row_count(board, move, player, (0, 1, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 0, 1)) == 1 or
        k_in_row_count(board, move, player, (0, 1, 1)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (2, 2, 3)
    if (k_in_row_count(board, move, player, (0, 1, 0)) == 2 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 2 or 
        k_in_row_count(board, move, player, (1, -1, 0)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1

    if (k_in_row_count(board, move, player, (0, 1, 0)) == 1 or
        k_in_row_count(board, move, player, (1, 0, 0)) == 1 or 
        k_in_row_count(board, move, player, (1, -1, 0)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (1, 2, 1)
    if (k_in_row_count(board, move, player, (0, 0, 1)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1

    if (k_in_row_count(board, move, player, (0, 0, 1)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (1, 3, 1)
    if (k_in_row_count(board, move, player, (0, 0, 1)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1
    
    if (k_in_row_count(board, move, player, (0, 0, 1)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (2, 1, 1)
    if (k_in_row_count(board, move, player, (0, 0, 1)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1
    
    if (k_in_row_count(board, move, player, (0, 0, 1)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (2, 3, 1)
    if (k_in_row_count(board, move, player, (0, 0, 1)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1
    
    if (k_in_row_count(board, move, player, (0, 0, 1)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (3, 1, 1)
    if (k_in_row_count(board, move, player, (0, 0, 1)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1
    
    if (k_in_row_count(board, move, player, (0, 0, 1)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1

    move = (3, 2, 1)
    if (k_in_row_count(board, move, player, (0, 0, 1)) == 2):
        value += .66 if player == 'X' else -.66
        count += 1
    
    if (k_in_row_count(board, move, player, (0, 0, 1)) == 1):
        value += .33 if player == 'X' else -.33
        count += 1
    if count == 0:
        return value
    else:
        return value/count

def evaluation_fn(state):
    if state.utility != 0:
        return state.utility
    board=state.board
    value = count_in_a_row(board, 'X')
    return value


def alpha_beta_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state, game, d=2, cutoff_test=None, eval_fn=evaluation_fn)

if __name__ == "__main__":
    
    ttt3d = ThreeDimensionalTicTacToe()
    
    utility = ttt3d.play_game(alpha_beta_cutoff_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
    
        
   
    