import tkinter as tk
from tkinter import messagebox

# This class handels displaying the UI for the game
class TicTacToeGUI:
    def __init__(self, peer):
        self.peer = peer
        self.window = tk.Tk()
        self.window.title(f"Tic Tac Toe - Player {self.peer.symbol}")

        if self.peer.symbol == 'X':
            self.status_label = tk.Label(self.window, text="Your turn", font=('Arial', 14))
        else:
            self.status_label = tk.Label(self.window, text="Waiting for opponent...", font=('Arial', 14))

        self.status_label.pack()

        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()
        self.buttons = [tk.Button(self.board_frame, text=' ', font=('Arial', 24), height=2, width=5, command=lambda i=i: self.on_click(i)) for i in range(9)]
        self.create_board()

        self.quit_button = tk.Button(self.window, text="Quit", font=('Arial', 14), command=self.quit_game)
        self.quit_button.pack(pady=10)

    def create_board(self):
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)

    def on_click(self, index):
        if self.peer.game.current_turn == self.peer.symbol:
            if self.peer.game.make_move(index):
                print("Sending move")
                self.peer.send_move(index)
                self.buttons[index].config(text=self.peer.symbol)
                self.update_board()
                self.check_game_status()

    def update_board(self):
        for i, button in enumerate(self.buttons):
            button.config(text=self.peer.game.board[i])
        self.status_label.config(text=f"Current Turn: {self.peer.game.current_turn}")

    def check_game_status(self):
        winner = self.peer.game.check_winner()
        if winner:
            if winner == self.peer.symbol:
                messagebox.showinfo("Game Over", "You Win!")
            else:
                messagebox.showinfo("Game Over", "You Lose!")
        elif self.peer.game.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")

    def run(self):
        self.window.mainloop()

    def quit_game(self):
        self.window.destroy()