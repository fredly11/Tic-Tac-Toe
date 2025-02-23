# game logic
class TicTacToe:
    def __init__(self, gui):
        self.board = [' '] * 9
        self.current_turn = 'X'
        self.gui = gui

# update the array to include new move
    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_turn
            self.current_turn = 'O' if self.current_turn == 'X' else 'X'
            self.gui.update_board()
            return True
        return False

#checks if a winninf state exists
    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != ' ':
                return self.board[a]
        return None

    def is_draw(self):
        return ' ' not in self.board