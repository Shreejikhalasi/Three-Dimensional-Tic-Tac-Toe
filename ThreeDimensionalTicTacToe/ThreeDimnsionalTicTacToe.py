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
                self.k_in_row(board, move, player, (1, -1, 1))):
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

    '''
    def compute_utility(self, board, move, player):
        if(self.winsOffMove(board, move, player)):
            return +1 if player == 'X' else -1
        else:
            return 0

    def winsOffMove(self, board, move, player):
        if move==(0,0,0):
            if (board.get((0,1,0)) == player) and (board.get((0,2,0))==player):
                return True
            if (board.get((1,0,0)) == player) and (board.get((2,0,0)) == player):
                return True
            if (board.get((1,1,0)) == player) and (board.get((2,2,0)) == player):
                return True
            if (board.get((0,0,1)) == player) and (board.get((0,0,2)) == player):
                return True
            if (board.get((1,1,1)) == player) and (board.get((2,2,2)) == player):
                return True

        elif move==(0,0,1):
            if (board.get((0,1,1)) == player) and (board.get((0,2,1)) == player):
                return True
            if (board.get((1,0,1)) == player) and (board.get((2,0,1)) == player):
                return True
            if (board.get((1,1,1)) == player) and (board.get((2,2,1)) == player):
                return True
            if (board.get((0,0,0)) == player) and (board.get((0,0,2)) == player):
                return True

        elif move==(0,0,2):
            if (board.get((0,1,2)) == player) and (board.get((0,2,2)) == player):
                return True 
            if (board.get((1,0,2)) == player) and (board.get((2,0,2)) == player):
                return True
            if (board.get((1,1,2)) == player) and (board.get((2,2,2)) == player):
                return True
            if (board.get((0,0,0)) == player) and (board.get((0,0,1)) == player):
                return True 
            if (board.get((2,2,0)) == player) and (board.get((1,1,1)) == player):
                return True 

        elif move==(0,1,0):
            if (board.get((0,0,0)) == player) and (board.get((0,2,0)) == player):
                return True
            if (board.get((1,1,0)) == player) and (board.get((2,1,0)) == player):
                return True 
            if (board.get((0,1,1)) == player) and (board.get((0,1,2)) == player):
                return True 
                
        elif move==(0,1,1):
            if (board.get((0,0,1)) == player) and (board.get((0,2,1)) == player):
                return True
            if (board.get((1,1,1)) == player) and (board.get((2,1,1)) == player):
                return True  
            if (board.get((0,1,0)) == player) and (board.get((0,1,2)) == player):
                return True
                
        elif move==(0,1,2):
            if (board.get((0,0,2)) == player) and (board.get((0,2,2)) == player):
                return True
            if (board.get((1,1,2)) == player) and (board.get((2,1,2)) == player):
                return True 
            if (board.get((0,1,0)) == player) and (board.get((0,1,1)) == player):
                return True

        elif move==(0,2,0):
            if (board.get((0,0,0)) == player) and (board.get((0,1,0)) == player):
                return True
            if (board.get((1,2,0)) == player) and (board.get((2,2,0)) == player):
                return True 
            if (board.get((1,1,0)) == player) and (board.get((2,0,0)) == player):
                return True 
            if (board.get((0,2,1)) == player) and (board.get((0,2,2)) == player):
                return True 
            if (board.get((1,1,1)) == player) and (board.get((2,0,2)) == player):
                return True 
                
        elif move==(0,2,1):
            if (board.get((0,0,1)) == player) and (board.get((0,1,1)) == player):
                return True
            if (board.get((1,2,1)) == player) and (board.get((2,2,1)) == player):
                return True 
            if (board.get((1,1,1)) == player) and (board.get((2,0,1)) == player):
                return True 
            if (board.get((0,2,0)) == player) and (board.get((0,2,2)) == player):
                return True  

        elif move==(0,2,2):
            if (board.get((0,0,2)) == player) and (board.get((0,1,2)) == player):
                return True
            if (board.get((1,2,2)) == player) and (board.get((2,2,2)) == player):
                return True
            if (board.get((1,1,2)) == player) and (board.get((2,0,2)) == player):
                return True 
            if (board.get((0,2,0)) == player) and (board.get((0,2,1)) == player):
                return True 
            if (board.get((2,0,0)) == player) and (board.get((1,1,1)) == player):
                return True 

        elif move==(1,0,0):
            if (board.get((1,1,0)) == player) and (board.get((1,2,0)) == player):
                return True
            if (board.get((0,0,0)) == player) and (board.get((2,0,0)) == player):
                return True 
            if (board.get((1,0,1)) == player) and (board.get((1,0,2)) == player):
                return True 

        elif move==(1,0,1):
            if (board.get((1,1,1)) == player) and (board.get((1,2,1)) == player):
                return True
            if (board.get((0,0,1)) == player) and (board.get((2,0,1)) == player):
                return True 
            if (board.get((1,0,0)) == player) and (board.get((1,0,2)) == player):
                return True 
            if (board.get((1,1,0)) == player) and (board.get((1,0,2)) == player):
                return True
            if (board.get((1,2,0)) == player) and (board.get((1,0,2)) == player):
                return True

        elif move==(1,0,2):
            if (board.get((1,1,2)) == player) and (board.get((1,2,2)) == player):
                return True
            if (board.get((0,0,2)) == player) and (board.get((2,0,2)) == player):
                return True 
            if (board.get((1,0,0)) == player) and (board.get((1,0,1)) == player):
                return True 
            if (board.get((1,1,0)) == player) and (board.get((1,0,1)) == player):
                return True
            if (board.get((1,2,0)) == player) and (board.get((1,0,1)) == player):
                return True
        
        elif move==(1,1,0):
            if (board.get((1,0,0)) == player) and (board.get((1,2,0)) == player):
                return True
            if (board.get((0,1,0)) == player) and (board.get((2,1,0)) == player):
                return True
            if (board.get((0,0,0)) == player) and (board.get((2,2,0)) == player):
                return True
            if (board.get((0,2,0)) == player) and (board.get((2,0,0)) == player):
                return True
            if (board.get((1,0,1)) == player) and (board.get((1,0,2)) == player):
                return True

        elif move==(1,1,1):
            if (board.get((1,0,1)) == player) and (board.get((1,2,1)) == player):
                return True
            if (board.get((0,1,1)) == player) and (board.get((2,1,1)) == player):
                return True
            if (board.get((0,0,1)) == player) and (board.get((2,2,1)) == player):
                return True
            if (board.get((0,2,1)) == player) and (board.get((2,0,1)) == player):
                return True
            if (board.get((0,0,0)) == player) and (board.get((2,2,2)) == player):
                return True
            if (board.get((2,0,0)) == player) and (board.get((0,2,2)) == player):
                return True
            if (board.get((0,2,0)) == player) and (board.get((2,0,2)) == player):
                return True
            if (board.get((2,2,0)) == player) and (board.get((0,0,2)) == player):
                return True

        elif move==(1,1,2):
            if (board.get((1,0,2)) == player) and (board.get((1,2,2))==player):
                return True
            if (board.get((0,1,2)) == player) and (board.get((2,1,2))==player):
                return True
            if (board.get((0,0,2)) == player) and (board.get((2,2,2)) == player):
                return True
            if (board.get((0,2,2)) == player) and (board.get((2,0,2)) == player):
                return True
        
        elif move==(1,2,0):
            if (board.get((1,0,0)) == player) and (board.get((1,1,0))==player):
                return True
            if (board.get((0,2,0)) == player) and (board.get((2,2,0))==player):
                return True
            if (board.get((1,0,1)) == player) and (board.get((1,0,2))==player):
                return True
            
            
        elif move==(1,2,1):
            if (board.get((1,0,1)) == player) and (board.get((1,1,1))==player):
                return True
            if (board.get((0,2,1)) == player) and (board.get((2,2,1))==player):
                return True
            
            
        elif move==(1,2,2):
            if (board.get((1,0,2)) == player) and (board.get((1,1,2))==player):
                return True
            if (board.get((0,2,2)) == player) and (board.get((2,2,2))==player):
                return True
        
        elif move==(2,0,0):
            if (board.get((2,1,0)) == player) and (board.get((2,2,0))==player):
                return True
            if (board.get((0,0,0)) == player) and (board.get((1,0,0))==player):
                return True
            if (board.get((0,2,0)) == player) and (board.get((1,1,0))==player):
                return True
            if (board.get((2,0,1)) == player) and (board.get((2,0,2))==player):
                return True
            if (board.get((1,1,1)) == player) and (board.get((0,2,2))==player):
                return True
           
        elif move==(2,0,1):
            if (board.get((2,1,1)) == player) and (board.get((2,2,1))==player):
                return True
            if (board.get((0,0,1)) == player) and (board.get((1,0,1))==player):
                return True
            if (board.get((0,2,1)) == player) and (board.get((1,1,1))==player):
                return True
            if (board.get((2,0,0)) == player) and (board.get((2,0,2))==player):
                return True
            if (board.get((2,1,0)) == player) and (board.get((2,0,2))==player):
                return True
            if (board.get((2,2,0)) == player) and (board.get((2,0,2))==player):
                return True
            
          
        elif move==(2,0,2):
            if (board.get((2,1,2)) == player) and (board.get((2,2,2))==player):
                return True
            if (board.get((0,0,2)) == player) and (board.get((1,0,2))==player):
                return True
            if (board.get((0,2,2)) == player) and (board.get((1,1,2))==player):
                return True
            if (board.get((2,0,0)) == player) and (board.get((2,0,1))==player):
                return True
            if (board.get((2,1,0)) == player) and (board.get((2,0,1))==player):
                return True
            if (board.get((2,2,0)) == player) and (board.get((2,0,1))==player):
                return True
            if (board.get((0,2,0)) == player) and (board.get((1,1,1))==player):
                return True
            
        elif move==(2,1,0):
            if (board.get((2,0,0)) == player) and (board.get((2,2,0))==player):
                return True
            if (board.get((0,1,0)) == player) and (board.get((1,1,0))==player):
                return True
            if (board.get((2,0,1)) == player) and (board.get((2,0,2))==player):
                return True
            
        elif move==(2,1,1):
            if (board.get((2,0,1)) == player) and (board.get((2,2,1))==player):
                return True
            if (board.get((0,1,1)) == player) and (board.get((1,1,1))==player):
                return True
           
        elif move==(2,1,2):
            if (board.get((2,0,2)) == player) and (board.get((2,2,2))==player):
                return True
            if (board.get((0,1,2)) == player) and (board.get((1,1,2))==player):
                return True

        elif move==(2,2,0):
            if (board.get((2,0,0)) == player) and (board.get((2,1,0))==player):
                return True
            if (board.get((0,2,0)) == player) and (board.get((1,2,0))==player):
                return True
            if (board.get((0,0,0)) == player) and (board.get((1,1,0))==player):
                return True
            if (board.get((2,0,1)) == player) and (board.get((2,0,2))==player):
                return True
            if (board.get((1,1,1)) == player) and (board.get((0,0,2))==player):
                return True
           
        elif move==(2,2,1):
            if (board.get((2,0,1)) == player) and (board.get((2,1,1))==player):
                return True
            if (board.get((0,2,1)) == player) and (board.get((1,2,1))==player):
                return True
            if (board.get((0,0,1)) == player) and (board.get((1,1,1))==player):
                return True
            
        elif move==(2,2,2):
            if (board.get((2,0,2)) == player) and (board.get((2,1,2))==player):
                return True
            if (board.get((0,2,2)) == player) and (board.get((1,2,2))==player):
                return True
            if (board.get((0,0,2)) == player) and (board.get((1,1,2))==player):
                return True
            if (board.get((0,0,0)) == player) and (board.get((1,1,1))==player):
                return True

        else:
            return False
    '''

def alpha_beta_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state, game, d=4, cutoff_test=None, eval_fn=None)
       


if __name__ == "__main__":
    
    ttt3d = ThreeDimensionalTicTacToe()
    
    utility = ttt3d.play_game(alpha_beta_cutoff_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
    '''
    tt = TicTacToe()
    print(tt.initial)
    utility = tt.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
    '''
    
    
        
   
    