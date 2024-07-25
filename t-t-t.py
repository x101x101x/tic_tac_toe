import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.master.configure(bg='pink')

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()
        self.create_turn_label()
        self.center_window()

    def create_board(self):
        board_frame = tk.Frame(self.master, bg='pink')
        board_frame.pack(pady=10)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(board_frame, text="", font=('normal', 20, 'bold'), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_click(row, col),
                                               bg='white')
                self.buttons[i][j].grid(row=i, column=j, padx=2, pady=2)

    def create_turn_label(self):
        self.turn_label = tk.Label(self.master, text="Player X's turn", font=('normal', 14), bg='pink')
        self.turn_label.pack(pady=10)

    def center_window(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def on_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_turn_label()

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
                    all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
                all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j].config(text="")
        self.current_player = "X"
        self.update_turn_label()

    def update_turn_label(self):
        self.turn_label.config(text=f"Player {self.current_player}'s turn")


def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


if __name__ == "__main__":
    main()