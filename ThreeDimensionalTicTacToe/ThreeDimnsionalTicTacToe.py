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

def evaluation_fn(state, game):
    player = game.to_move(state)
    board = state.board.copy()
    if player == 'X':
        otherPlayer = 'Y'
    else:
        otherPlayer = 'X'

    #Horizontal rows flat
    for dimension in range(1, 4):
        for row in range(1, 4):
            numInRow = 0
            for elem in (1, 4):
                if board.get(elem, row, dimension) == player:
                    numInRow+=1
                if board.get(elem, row, dimension) == otherPlayer:
                    numInRow=0
                    break
            if numInRow == 1:
                oneInRow+=1
            if numInRow == 2:
                twoInRow+=1
            if numInRow == 3:
                threeInRow+=1

    #Vertical rows flat
    for dimension in range(1, 4):
        for row in range(1, 4):
            numInRow = 0
            for elem in (1, 4):
                if board.get(row, elem, dimension) == player:
                    numInRow+=1
                if board.get(row, elem, dimension) == otherPlayer:
                    numInRow=0
                    break
            if numInRow == 1:
                oneInRow+=1
            if numInRow == 2:
                twoInRow+=1
            if numInRow == 3:
                threeInRow+=1
    
    #\ rows flat
    for dimension in range(1, 4):
        numInRow=0
        for x, y in range(1, 4):
            if board.get(x, y, dimension) == player:
                numInRow+=1
            if board.get(x, y, dimension) == otherPlayer:
                numInRow=0
                break
        if numInRow == 1:
            oneInRow+=1
        if numInRow == 2:
            twoInRow+=1
        if numInRow == 3:
            threeInRow+=1

    #/ rows flat
    for dimension in range(1, 4):
        numInRow=0
        for x, y in range(3, 0, -1):
            if board.get(x, y, dimension) == player:
                numInRow+=1
            if board.get(x, y, dimension) == otherPlayer:
                numInRow=0
                break
        if numInRow == 1:
            oneInRow+=1
        if numInRow == 2:
            twoInRow+=1
        if numInRow == 3:
            threeInRow+=1

    #Z axis
    for row in range(1, 4):
        for col in range(1, 4):
            numInRow=0
            for dim in range(1, 4):
                if board.get(row, col, dimension) == player:
                    numInRow+=1
                if board.get(row, col, dimension) == otherPlayer:
                    numInRow=0
                    break
            if numInRow == 1:
                oneInRow+=1
            if numInRow == 2:
                twoInRow+=1
            if numInRow == 3:
                threeInRow+=1

    #Side diagonal 
    for row in (1, 4):
        numInRow=0
        for col, dim in (1, 4):
            if board.get(row, col, dim) == player:
                numInRow+=1
            if board.get(row, col, dim) == otherPlayer:
                numInRow=0
                break
        if numInRow == 1:
            oneInRow+=1
        if numInRow == 2:
            twoInRow+=1
        if numInRow == 3:
            threeInRow+=1

    #Side diagonal
    for row in (1, 4):
        numInRow=0
        dim=1
        for col in (3, 0, -1):
            if board.get(row, col, dim) == player:
                numInRow+=1
            if board.get(row, col, dim) == otherPlayer:
                numInRow=0
                break
            dim+=1
        if numInRow == 1:
            oneInRow+=1
        if numInRow == 2:
            twoInRow+=1
        if numInRow == 3:
            threeInRow+=1

    #3d diagonal 1
    numInRow=0
    for rcd in (1, 4):
        if board.get(rcd, rcd, rcd) == player:
            numInRow+=1
        if board.get(rcd, rcd, rcd) == otherPlayer:
            numInRow=0
            break
    if numInRow == 1:
        oneInRow+=1
    if numInRow == 2:
        twoInRow+=1
    if numInRow == 3:
        threeInRow+=1

    #3d diagonal 2
    numInRow=0
    dim=1
    for rcd in (3, 0, -1):
        if board.get(rcd, rcd, dim) == player:
            numInRow+=1
        if board.get(rcd, rcd, dim) == otherPlayer:
            numInRow=0
            break
        dim+=1
    if numInRow == 1:
        oneInRow+=1
    if numInRow == 2:
        twoInRow+=1
    if numInRow == 3:
        threeInRow+=1

    #3d diagonal 3
    numInRow=0
    dim=1
    row=1
    col=3
    for count in (1, 4):
        if board.get(row, col, dim) == player:
            numInRow+=1
        if board.get(row, col, dim) == otherPlayer:
            numInRow=0
            break
        dim+=1
        row+=1
        col-=1
    if numInRow == 1:
        oneInRow+=1
    if numInRow == 2:
        twoInRow+=1
    if numInRow == 3:
        threeInRow+=1

    #3d diagonal 3
    numInRow=0
    dim=3
    row=1
    col=3
    for count in (1, 4):
        if board.get(row, col, dim) == player:
            numInRow+=1
        if board.get(row, col, dim) == otherPlayer:
            numInRow=0
            break
        dim-=1
        row+=1
        col-=1
    if numInRow == 1:
        oneInRow+=1
    if numInRow == 2:
        twoInRow+=1
    if numInRow == 3:
        threeInRow+=1

    oneInRow=0
    twoInRow=0
    threeInRow=0
    finalUtility=((43**2)*threeInRow)+(43*twoInRow)+oneInRow
    return finalUtility



def alpha_beta_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state, game, d=4, cutoff_test=None, eval_fn=evaluation_fn)

       


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
    
    
        
   
    